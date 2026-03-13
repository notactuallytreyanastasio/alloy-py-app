# SQL Security Analysis: Python Todo App

SQL injection analysis of the Python todo app built on the Generic Temper ORM. This analysis focuses exclusively on SQL generation and execution -- the core value proposition of the ORM.

**Analysis Date:** 2026-03-12
**Updated:** 2026-03-13 (MITRE ATT&CK / CWE Top 25 mapping, JOIN feature analysis)
**Framework:** Flask + Jinja2 + sqlite3
**ORM:** Generic Temper ORM (compiled to Python)

---

## How This App Uses the ORM

All user-facing CRUD operations flow through the Temper ORM's type-safe SQL generation:

| Operation | Method | SQL Source |
|-----------|--------|------------|
| SELECT lists/todos | `from_(safe_identifier("...")).where(...).to_sql()` | ORM |
| INSERT list/todo | `changeset(table, params).cast(fields).validate_required(fields).to_insert_sql()` | ORM |
| UPDATE todo title | `changeset(table, params).cast(fields).to_update_sql(id)` | ORM |
| DELETE list/todo | `delete_sql(table, id)` | ORM |
| WHERE clauses | `SqlBuilder.append_safe()` + `append_int32()` | ORM |
| Toggle completed | `UPDATE todos SET completed = ? WHERE id = ?` | Raw (parameterized) |
| Counts per list | `SELECT COUNT(*) FROM todos WHERE list_id = ?` | Raw (parameterized) |
| Rename list | `UPDATE lists SET name = ? WHERE id = ?` | Raw (parameterized) |
| Get by ID | `SELECT * FROM lists WHERE id = ?` | Raw (parameterized) |
| DDL | `CREATE TABLE IF NOT EXISTS ...` | Raw (static) |

### ORM SQL Generation Path

```
User input (form field)
  -> Flask request.form["title"].strip()
    -> temper Map construction
      -> changeset(table_def, params_map)       [factory -- sealed interface]
        -> .cast(allowed_fields)                 [SafeIdentifier whitelist]
          -> .validate_required(fields)          [non-null enforcement]
            -> .to_insert_sql()                  [type-dispatched escaping]
              -> .to_string()                    [rendered SQL string]
                -> db.execute(sql)               [SQLite execution]
```

For queries:
```
Route parameter (/lists/<int:list_id>)
  -> Flask <int:> converter (guaranteed integer)
    -> SqlBuilder.append_int32(list_id)          [bare integer]
      -> from_(safe_identifier("lists")).where(fragment).to_sql()
        -> db.execute(sql)
```

---

## SQL Injection Analysis

### ORM-Generated SQL: Protected

**SafeIdentifier validation** -- All table/column identifiers validated against `[a-zA-Z_][a-zA-Z0-9_]*`. Flask's `<int:list_id>` route converter provides an additional layer -- non-integer path segments return 404 before reaching the ORM.

**SqlString escaping** -- User-provided strings (list names, todo titles) pass through `SqlString` which escapes `'` to `''`.

**Changeset field whitelisting** -- `cast()` restricts which fields can appear in INSERT/UPDATE SQL.

### Raw SQL: Also Protected

All raw SQL uses Python's `sqlite3` parameterized queries with `?` placeholders and tuple binding:

```python
# Toggle -- parameterized
db.execute("UPDATE todos SET completed = ? WHERE id = ?", (new_val, todo_id))

# Count -- parameterized
db.execute("SELECT COUNT(*) FROM todos WHERE list_id = ?", (row["id"],))

# Rename -- parameterized
db.execute("UPDATE lists SET name = ? WHERE id = ?", (name, list_id))

# Get by ID -- parameterized
db.execute("SELECT * FROM lists WHERE id = ?", (list_id,))
```

### DDL: Static

Schema creation uses hardcoded `CREATE TABLE` statements. Seed data uses hardcoded literals (`WHERE name = 'Personal'`) -- not user-controllable.

---

## Findings

| # | Severity | CWE | Finding |
|---|----------|-----|---------|
| PY-SQL-1 | INFO | CWE-89 | ORM SQL is executed via `db.execute(sql)` as a rendered string. The escaping is correct, but `db.execute(sql)` with pre-rendered values is escaping-based rather than parameterized. |
| PY-SQL-2 | INFO | CWE-400 | SELECT queries use `to_sql()` without limits. The ORM's `safe_to_sql(default_limit)` is available but unused. |
| PY-SQL-3 | INFO | CWE-89 | Seed code contains `WHERE name = 'Personal'` (hardcoded literal in SQL). Not user-controllable, but breaks the pattern of parameterized queries. |
| PY-WEB-1 | HIGH | CWE-352 | No CSRF protection. Flask-WTF is not installed, and no CSRF tokens are generated or validated on any POST form. All 6 state-mutating POST routes (`/lists`, `/lists/<id>/edit`, `/lists/<id>/delete`, `/lists/<id>/todos`, `/todos/<id>/toggle`, `/todos/<id>/edit`, `/todos/<id>/delete`) accept unauthenticated form submissions from any origin. |
| PY-WEB-2 | MEDIUM | CWE-798 | `app.config["SECRET_KEY"] = "retro-todo-secret-key"` is a hardcoded secret. While Flask currently uses this only for session signing (and sessions are not actively used), any future session/cookie usage would be insecure with a publicly visible key. |
| PY-WEB-3 | MEDIUM | CWE-862 | No authentication or authorization. Any network-reachable client can perform all CRUD operations on all data. |
| PY-WEB-4 | MEDIUM | CWE-489 | `app.run(debug=True, port=5001)` enables Flask's debug mode. In production, this exposes the Werkzeug interactive debugger, which allows arbitrary Python code execution. The debugger is PIN-protected but the PIN is guessable from system information. |
| PY-WEB-5 | LOW | CWE-79 | Jinja2 auto-escapes `{{ }}` interpolations in HTML context. However, `index.html` passes user data into JavaScript `onclick` handlers: `startEditList({{ item.list.id }}, '{{ item.list.name|e }}')`. While `|e` HTML-escapes the name, this is HTML escaping in a JavaScript string context -- a list name containing `\` or line breaks could break the JS string. Similarly, `list.html` uses `{{ todo.title|replace("'", "\\'")|e }}` which applies both JS quote escaping and HTML escaping, creating a layered but fragile defense. Low severity because Jinja2's auto-escape prevents the most dangerous XSS vectors. |
| PY-WEB-6 | INFO | CWE-693 | No security headers set. Missing `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`. Flask does not add these by default; `flask-talisman` or manual header setting would be needed. |

### ORM-Level Concerns (shared across all apps)

| # | Severity | CWE | Finding |
|---|----------|-----|---------|
| ORM-1 | MEDIUM | CWE-89 | `to_insert_sql`/`to_update_sql` pass `pair.key` (a `String`) to `append_safe`. Safe by construction -- keys come from `cast()` which requires `SafeIdentifier` -- but the type system doesn't enforce this at the call site. |
| ORM-2 | LOW | CWE-89 | `SqlDate.format_to` wraps `value.to_string()` in quotes without escaping. |
| ORM-3 | LOW | CWE-20 | `SqlFloat64.format_to` can produce `NaN`/`Infinity` -- not valid SQL literals. |

---

## MITRE Top 25 CWE Analysis (2024)

Full mapping of the MITRE/CWE Top 25 Most Dangerous Software Weaknesses (2024 edition) against this application.

### Assessment Methodology

Each CWE is evaluated against the application codebase (`app.py`), templates (`templates/*.html`), the vendored ORM (`vendor/orm/`), and the deployment configuration. Status categories:

- **Mitigated** -- The app has adequate protection against this weakness.
- **Partially Mitigated** -- Some protection exists but gaps remain.
- **Vulnerable** -- The app is susceptible to this weakness.
- **N/A** -- The weakness category does not apply to this app's architecture.

### Full Mapping Table

| Rank | CWE ID | CWE Name | Status | Details |
|------|--------|----------|--------|---------|
| 1 | CWE-787 | Out-of-bounds Write | N/A | Python is memory-managed. No native buffer operations, no C extensions in application code. Not applicable. |
| 2 | CWE-79 | Improper Neutralization of Input During Web Page Generation (XSS) | **Partially Mitigated** | Jinja2 auto-escapes all `{{ }}` interpolations in HTML context by default. User-controlled values (`item.list.name`, `todo.title`, IDs, counts) are all rendered through auto-escaped `{{ }}`. No use of `|safe` or `{% autoescape false %}` for user data. However, user data is interpolated into JavaScript `onclick` handlers in `index.html` and `list.html` (e.g., `startEditList({{ item.list.id }}, '{{ item.list.name|e }}')`), where HTML escaping is applied in a JavaScript string context -- a layered but imperfect defense. See PY-WEB-5. |
| 3 | CWE-89 | Improper Neutralization of Special Elements used in an SQL Command (SQL Injection) | **Mitigated** | All user input to SQL goes through either (a) the ORM's `SafeIdentifier` + `SqlString`/`SqlInt32` escaping pipeline or (b) Python `sqlite3` parameterized queries (`?` placeholders with tuple binding). No string concatenation of user input into SQL anywhere in the application. Flask's `<int:>` route converter provides an additional layer -- non-integer path segments return 404 before reaching SQL code. See detailed SQL analysis above. |
| 4 | CWE-416 | Use After Free | N/A | Python is garbage-collected. Not applicable. |
| 5 | CWE-78 | Improper Neutralization of Special Elements used in an OS Command (OS Command Injection) | N/A | No `subprocess`, `os.system()`, `os.popen()`, `eval()`, or shell commands anywhere in the application. |
| 6 | CWE-20 | Improper Input Validation | **Partially Mitigated** | Flask's `<int:list_id>` route converter enforces integer types for route parameters. Form inputs are trimmed via `.strip()` and checked for emptiness before use. The ORM's `cast()` whitelists allowed fields and `validate_required()` checks for non-null. However, no length limits are enforced on user-provided `name` or `title` strings. No content validation beyond non-empty. The ORM's `append_int32()` accepts Python `int` which has arbitrary precision -- values exceeding 32-bit range would be rendered directly into SQL. |
| 7 | CWE-125 | Out-of-bounds Read | N/A | Python is memory-managed. Not applicable. |
| 8 | CWE-22 | Improper Limitation of a Pathname to a Restricted Directory (Path Traversal) | **Mitigated** | The only file serving is the static CSS route (`send_file(css_path)`) with a hardcoded path constructed from `BASE_DIR`. No user-controlled file paths. The database path is hardcoded. Flask's `static_folder` serves from a fixed directory. No user-supplied path segments reach any file operation. |
| 9 | CWE-352 | Cross-Site Request Forgery (CSRF) | **Vulnerable** | No CSRF protection of any kind. Flask-WTF is not installed. No CSRF tokens are generated or validated. All 7 POST endpoints accept plain HTML form submissions without any token, origin, or referer validation. An attacker could craft a cross-origin form to create lists, delete data, or modify todos if the app is running on the user's machine. **Finding PY-WEB-1.** |
| 10 | CWE-434 | Unrestricted Upload of File with Dangerous Type | N/A | No file upload functionality exists. No `request.files` usage. |
| 11 | CWE-862 | Missing Authorization | **Vulnerable** | No authentication or authorization mechanism. All routes are publicly accessible. Any network-reachable client can perform all CRUD operations on all data. **Finding PY-WEB-3.** |
| 12 | CWE-476 | NULL Pointer Dereference | N/A | Python raises `TypeError`/`AttributeError` on None attribute access. The app checks `if row is None: abort(404)` before accessing row data. Flask catches unhandled exceptions as 500 errors. Not a meaningful risk. |
| 13 | CWE-287 | Improper Authentication | **Vulnerable** | No authentication system exists. No login, no sessions, no API keys, no tokens. This is by design for a local demo app, but means the app has zero authentication. |
| 14 | CWE-190 | Integer Overflow or Wraparound | **Mitigated** | Python integers have arbitrary precision -- no overflow is possible. Flask's `<int:>` converter produces Python `int` which is always exact. SQLite handles large integers natively. The ORM's `append_int32()` renders via string conversion, which produces the correct decimal for any Python int. |
| 15 | CWE-502 | Deserialization of Untrusted Data | N/A | No `pickle.loads()`, `yaml.load()`, `eval()`, or other deserialization of user-controlled data. Flask's `request.form` produces simple string key-value pairs from URL-encoded form data. |
| 16 | CWE-77 | Improper Neutralization of Special Elements used in a Command (Command Injection) | N/A | No command execution. No `eval()`, no `exec()`, no `compile()` with user input. |
| 17 | CWE-119 | Improper Restriction of Operations within the Bounds of a Memory Buffer | N/A | Python is memory-safe. Not applicable. |
| 18 | CWE-798 | Use of Hard-coded Credentials | **Vulnerable** | `app.config["SECRET_KEY"] = "retro-todo-secret-key"` is a hardcoded, publicly visible secret key. While Flask sessions are not actively used in this app, the key is set and would be used to sign any session cookies. An attacker who knows the SECRET_KEY can forge session data. **Finding PY-WEB-2.** |
| 19 | CWE-918 | Server-Side Request Forgery (SSRF) | N/A | No outbound HTTP requests. No `requests`, `urllib`, `httpx`, or URL-based resource loading from user input. |
| 20 | CWE-306 | Missing Authentication for Critical Function | **Vulnerable** | DELETE operations (`/lists/<id>/delete`, `/todos/<id>/delete`) and all other state-mutating endpoints are available without authentication. Same scope as CWE-287/862 above. |
| 21 | CWE-362 | Concurrent Execution using Shared Resource with Improper Synchronization (Race Condition) | **Partially Mitigated** | Flask's development server is single-threaded by default. SQLite's WAL mode provides good read concurrency. However, the toggle pattern (read `completed` status, compute new value, write update) is not atomic at the application level. With a multi-threaded or multi-process deployment (gunicorn, uwsgi), concurrent toggles could read stale data. Low practical risk for the demo app's intended usage. |
| 22 | CWE-269 | Improper Privilege Management | N/A | Single-tier app with no privilege levels. No admin/user distinction exists. |
| 23 | CWE-94 | Improper Control of Generation of Code (Code Injection) | **Partially Mitigated** | No `eval()` or dynamic code generation from user input. Jinja2 templates are loaded from the filesystem, not from user data. However, Flask's `debug=True` enables the Werkzeug interactive debugger, which provides a Python REPL accessible via the browser. The debugger is PIN-protected but the PIN can be computed from system information (`/proc/self/cgroup`, MAC address, machine-id). **Finding PY-WEB-4.** |
| 24 | CWE-863 | Incorrect Authorization | N/A (prerequisite missing) | No authorization logic exists to be incorrect. This is subsumed by CWE-862 (missing authorization entirely). |
| 25 | CWE-276 | Incorrect Default Permissions | **Partially Mitigated** | The SQLite database file (`todos.db`) is created with Python's default permissions (typically 0644 on Unix). On a multi-user system, other users could read the database. No explicit permission setting via `os.chmod()` is performed. Flask's development server binds to `127.0.0.1` by default (unlike some other framework defaults), which limits network exposure. |

### Summary

| Status | Count | CWEs |
|--------|-------|------|
| **Mitigated** | 3 | CWE-89, CWE-22, CWE-190 |
| **Partially Mitigated** | 4 | CWE-79, CWE-20, CWE-362, CWE-276 |
| **Vulnerable** | 5 | CWE-352, CWE-862, CWE-287, CWE-798, CWE-306 |
| **N/A** | 13 | CWE-787, CWE-416, CWE-78, CWE-125, CWE-434, CWE-476, CWE-502, CWE-77, CWE-119, CWE-918, CWE-269, CWE-94 (partially), CWE-863 |

### Risk Assessment

The app's **core data-handling security is strong**: SQL injection is comprehensively mitigated through the ORM's type-safe SQL generation and parameterized raw queries, and XSS is largely mitigated by Jinja2's auto-escaping. The primary vulnerabilities are **infrastructure-level concerns**: missing CSRF protection, missing authentication, a hardcoded SECRET_KEY, and Flask's debug mode enabled at the entry point. These are typical of demo/prototype applications not yet hardened for production deployment.

The **hardcoded SECRET_KEY** (CWE-798) is a Python/Flask-specific finding not present in the other language apps. The **debug=True** entry point (CWE-489/94) is also Python-specific -- Flask's Werkzeug debugger provides a browser-accessible Python REPL that effectively grants remote code execution to anyone who can guess the debugger PIN.

---

## JOIN Feature Security Analysis

**Date:** 2026-03-13
**Feature:** JOIN support (INNER, LEFT, RIGHT, FULL OUTER) added to the Temper ORM's Query builder.

### Architecture

The ORM's JOIN implementation follows the same security model as the rest of the query builder:

```
Query.inner_join(table: SafeIdentifier, on_condition: SqlFragment) -> Query
Query.left_join(table: SafeIdentifier, on_condition: SqlFragment) -> Query
Query.right_join(table: SafeIdentifier, on_condition: SqlFragment) -> Query
Query.full_join(table: SafeIdentifier, on_condition: SqlFragment) -> Query
```

The generic `join()` method takes three arguments:
1. `join_type: JoinType` -- a **sealed interface** with exactly 4 implementations (`InnerJoin`, `LeftJoin`, `RightJoin`, `FullJoin`). Each returns a hardcoded keyword string (`"INNER JOIN"`, `"LEFT JOIN"`, `"RIGHT JOIN"`, `"FULL OUTER JOIN"`).
2. `table: SafeIdentifier` -- the joined table name, validated against `[a-zA-Z_][a-zA-Z0-9_]*`.
3. `on_condition: SqlFragment` -- the ON clause, which must be constructed via `SqlBuilder` methods (type-safe escaping).

### SQL Generation Path for JOINs

```
Query.inner_join(table, on_condition)
  -> JoinClause(InnerJoin(), table, on_condition)
    -> to_sql() renders:
      b.append_safe(" ")                     [hardcoded space]
      b.append_safe(jc.join_type.keyword())  [hardcoded "INNER JOIN"]
      b.append_safe(" ")                     [hardcoded space]
      b.append_safe(jc.table.sql_value)      [SafeIdentifier-validated table name]
      b.append_safe(" ON ")                  [hardcoded keyword]
      b.append_fragment(jc.on_condition)     [SqlFragment -- pre-built safe SQL]
```

### Security Properties

| Component | Input Type | Validation | Injection Risk |
|-----------|-----------|------------|----------------|
| JOIN keyword | `JoinType.keyword()` | Sealed interface, hardcoded strings only | None -- `"INNER JOIN"`, `"LEFT JOIN"`, `"RIGHT JOIN"`, `"FULL OUTER JOIN"` are compile-time constants |
| Table name | `SafeIdentifier` | `[a-zA-Z_][a-zA-Z0-9_]*` regex validation at construction | None -- validated at creation; `ValidatedIdentifier` is not exported |
| ON condition | `SqlFragment` | Must be constructed via `SqlBuilder` methods (`append_safe`, `append_string`, `append_int32`, etc.) | Depends on how the caller constructs the fragment (see below) |

### ON Condition Analysis

The `on_condition` parameter accepts a `SqlFragment`. This is the same type used for `WHERE` conditions, so the security properties are identical:

**Safe usage patterns (as demonstrated in tests):**
```python
# Using col() helper -- both sides are SafeIdentifier-validated
cond = col(safe_identifier("users"), safe_identifier("id"))
# Renders: users.id

# Building ON condition with SqlBuilder
b = SqlBuilder()
b.append_fragment(col(safe_identifier("users"), safe_identifier("id")))
b.append_safe(" = ")
b.append_fragment(col(safe_identifier("orders"), safe_identifier("user_id")))
query.inner_join(safe_identifier("orders"), b.accumulated)
# Renders: INNER JOIN orders ON users.id = orders.user_id
```

**The `col()` helper** is a new addition that produces qualified column references (`table.column`) with both components validated as `SafeIdentifier`. This is the recommended way to build ON conditions.

**Potential misuse pattern (not present in this app):**
```python
# DANGEROUS -- if someone passed raw user input to append_safe
b = SqlBuilder()
b.append_safe(user_input)  # BAD -- append_safe trusts its input
query.inner_join(safe_identifier("orders"), b.accumulated)
```

This is the same risk as exists for WHERE conditions -- `append_safe` is inherently trusted. The ORM's security model relies on developers never passing user input to `append_safe`. This is documented in the ORM's security comments and enforced by convention, not by the type system.

### Current App Usage

The Python todo app does **not** currently use the ORM's JOIN feature in any route. The count queries in the `index` route use separate parameterized SQL queries per list:

```python
# In index() -- separate parameterized queries, not JOINs
total = db.execute("SELECT COUNT(*) FROM todos WHERE list_id = ?", (row["id"],)).fetchone()[0]
done = db.execute("SELECT COUNT(*) FROM todos WHERE list_id = ? AND completed = 1", (row["id"],)).fetchone()[0]
```

If the app were updated to use the ORM's new JOIN API, it would look like:

```python
on_cond_builder = SqlBuilder()
on_cond_builder.append_fragment(col(safe_identifier("todos"), safe_identifier("list_id")))
on_cond_builder.append_safe(" = ")
on_cond_builder.append_fragment(col(safe_identifier("lists"), safe_identifier("id")))

q = (from_(safe_identifier("lists"))
     .left_join(safe_identifier("todos"), on_cond_builder.accumulated)
     .to_sql())
```

This would provide the same safety guarantees with the added benefit of validated table names and the ability to eliminate the N+1 query pattern in the index route.

### Threat Analysis

| Threat | Status | Rationale |
|--------|--------|-----------|
| SQL injection via JOIN table name | **Mitigated** | `SafeIdentifier` rejects all non-`[a-zA-Z_][a-zA-Z0-9_]*` input. `safe_identifier("users; DROP TABLE users; --")` raises an error. |
| SQL injection via ON condition | **Mitigated** | ON conditions are `SqlFragment` values assembled via `SqlBuilder`. String interpolation uses `SqlString` (quote escaping). Integer interpolation uses `SqlInt32`/`SqlInt64` (bare numeric rendering). No raw string concatenation path exists. |
| JOIN type confusion | **Mitigated** | `JoinType` is a sealed interface. Only the 4 built-in implementations exist. No user-provided join type string is possible. |
| Unbounded JOIN result sets | **Partially Mitigated** | JOINs can produce large result sets (Cartesian products in worst case). The `safe_to_sql(default_limit)` method would apply a LIMIT, but this app uses `to_sql()` without limits for its existing queries. Same concern as PY-SQL-2. |
| Information disclosure via JOIN | **N/A in current app** | The app does not yet use the ORM's JOIN feature. When adopted, JOIN queries could expose data from related tables. This is a data modeling concern, not an injection concern. |

### JOIN-Specific Findings

| # | Severity | CWE | Finding |
|---|----------|-----|---------|
| JOIN-1 | INFO | CWE-89 | The `JoinType` sealed interface is well-designed -- the JOIN keyword is a hardcoded string from a closed set of implementations. No user input can influence the JOIN type keyword. |
| JOIN-2 | INFO | CWE-89 | The joined table name requires `SafeIdentifier`, enforcing the same `[a-zA-Z_][a-zA-Z0-9_]*` validation as the primary table. No injection possible through table names. |
| JOIN-3 | LOW | CWE-89 | The ON condition uses `SqlFragment`, which is trusted by construction. The `col()` helper provides a safe way to build qualified column references. However, if a future developer passes raw user input to `SqlBuilder.append_safe()` when building ON conditions, it would bypass all escaping. This is a design limitation (convention-based safety) shared with WHERE conditions. |
| JOIN-4 | INFO | CWE-400 | JOIN operations can amplify result set sizes (e.g., a many-to-many join can produce O(n*m) rows). The existing `safe_to_sql(default_limit)` mechanism applies LIMIT to the final result, which bounds output size, but intermediate join processing in SQLite is unbounded. For this app, table sizes are small (user-created todo lists) so this is informational only. |
| JOIN-5 | INFO | N/A | This todo app does not currently use the ORM's JOIN feature in any route. The aggregate queries in `index()` use separate parameterized SQL queries per list instead. The JOIN feature is available via the vendored ORM but unused. |

### JOIN Feature Verdict

The JOIN implementation follows the same security patterns as the rest of the ORM. Table names are `SafeIdentifier`-validated, JOIN keywords are hardcoded from a sealed interface, and ON conditions use the same `SqlFragment` type as WHERE conditions. No new attack surface is introduced beyond what already exists in the Query builder.

The `col()` helper function is a positive security addition -- it provides a convenient, safe way to build qualified column references for ON conditions without resorting to raw string manipulation.

---

## Verdict

**No SQL injection vulnerabilities found.** The ORM handles all user-input-to-SQL paths with type-safe escaping, and raw SQL consistently uses parameterized queries with `?` placeholders. Flask's `<int:>` route converter adds an extra layer of integer validation before ORM calls.

**5 web-layer vulnerabilities identified** (CSRF, hardcoded SECRET_KEY, missing auth, missing authentication, debug mode) that are typical of demo/prototype applications. The **hardcoded SECRET_KEY** and **debug=True** are Python/Flask-specific risks not present in the other language implementations.

**Total findings: 17** (9 app-level, 3 ORM-level, 5 JOIN-specific)

| Category | Critical | High | Medium | Low | Info |
|----------|----------|------|--------|-----|------|
| SQL Injection | 0 | 0 | 0 | 0 | 3 |
| Web Security | 0 | 1 | 3 | 1 | 1 |
| ORM Core | 0 | 0 | 1 | 2 | 0 |
| JOIN Feature | 0 | 0 | 0 | 1 | 4 |
| **Total** | **0** | **1** | **4** | **4** | **8** |

---

## Evolution: Temper-Level Remediation

**Date:** 2026-03-12
**Commit:** [`1df8c7a`](https://github.com/notactuallytreyanastasio/generic_orm/commit/1df8c7a)

The security analysis above identified 3 ORM-level concerns (ORM-1, ORM-2, ORM-3) shared across all 6 app implementations. Because the ORM is written once in Temper and compiled to all backends, fixing these issues at the Temper source level automatically resolves them in every language -- including this Python app.

### What Changed

**ORM-1 (MEDIUM -> RESOLVED): Column name type safety in INSERT/UPDATE SQL**

The `to_insert_sql()` and `to_update_sql()` methods previously passed `pair.key` (a raw `str`) to `append_safe()`. While safe by construction (keys originated from `cast()` via `SafeIdentifier.sql_value`), the type system didn't enforce this. A future refactor could have silently introduced an unvalidated code path.

The fix routes column names through the looked-up `FieldDef.name.sql_value` -- a `SafeIdentifier` -- so the column name in the generated SQL always comes from a validated identifier, not a raw map key.

**ORM-2 (LOW -> RESOLVED): SqlDate quote escaping**

`SqlDate.format_to()` previously wrapped `value.to_string()` in quotes without escaping. The fix adds character-by-character quote escaping identical to `SqlString.format_to()`, ensuring defense-in-depth against any future Date format that might contain single quotes.

**ORM-3 (LOW -> RESOLVED): SqlFloat64 NaN/Infinity handling**

`SqlFloat64.format_to()` previously called `value.to_string()` directly, which could produce `nan`, `inf`, or `-inf` -- none valid SQL literals. The fix checks for these values and renders `NULL` instead, which is the safest SQL representation for non-representable floating-point values.

### Why This Matters

This is the core value proposition of a cross-compiled ORM: **one fix in Temper source propagates to all 6 backends simultaneously.** The same commit that fixed the Python compiled output also fixed JavaScript, Rust, Java, Lua, and C#. No per-language patches needed. No risk of inconsistent fixes across implementations.

### Updated Status

| Finding | Original | Current | Resolution |
|---------|----------|---------|------------|
| ORM-1 | MEDIUM | RESOLVED | Column names routed through `SafeIdentifier` |
| ORM-2 | LOW | RESOLVED | `SqlDate.format_to()` now escapes quotes |
| ORM-3 | LOW | RESOLVED | `SqlFloat64.format_to()` renders NaN/Infinity as `NULL` |
| ORM-4 | INFO | ACKNOWLEDGED | Design limitation -- escaping-based, not parameterized |
