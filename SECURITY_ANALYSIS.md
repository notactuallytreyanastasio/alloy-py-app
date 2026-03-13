# SQL Security Analysis: Python Todo App

SQL injection analysis of the Python todo app built on the Generic Temper ORM. This analysis focuses exclusively on SQL generation and execution — the core value proposition of the ORM.

**Analysis Date:** 2026-03-12
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
  → Flask request.form["title"].strip()
    → temper Map construction
      → changeset(table_def, params_map)       [factory — sealed interface]
        → .cast(allowed_fields)                 [SafeIdentifier whitelist]
          → .validate_required(fields)          [non-null enforcement]
            → .to_insert_sql()                  [type-dispatched escaping]
              → .to_string()                    [rendered SQL string]
                → db.execute(sql)               [SQLite execution]
```

For queries:
```
Route parameter (/lists/<int:list_id>)
  → Flask <int:> converter (guaranteed integer)
    → SqlBuilder.append_int32(list_id)          [bare integer]
      → from_(safe_identifier("lists")).where(fragment).to_sql()
        → db.execute(sql)
```

---

## SQL Injection Analysis

### ORM-Generated SQL: Protected

**SafeIdentifier validation** — All table/column identifiers validated against `[a-zA-Z_][a-zA-Z0-9_]*`. Flask's `<int:list_id>` route converter provides an additional layer — non-integer path segments return 404 before reaching the ORM.

**SqlString escaping** — User-provided strings (list names, todo titles) pass through `SqlString` which escapes `'` → `''`.

**Changeset field whitelisting** — `cast()` restricts which fields can appear in INSERT/UPDATE SQL.

### Raw SQL: Also Protected

All raw SQL uses Python's `sqlite3` parameterized queries with `?` placeholders and tuple binding:

```python
# Toggle — parameterized
db.execute("UPDATE todos SET completed = ? WHERE id = ?", (new_val, todo_id))

# Count — parameterized
db.execute("SELECT COUNT(*) FROM todos WHERE list_id = ?", (row["id"],))

# Rename — parameterized
db.execute("UPDATE lists SET name = ? WHERE id = ?", (name, list_id))

# Get by ID — parameterized
db.execute("SELECT * FROM lists WHERE id = ?", (list_id,))
```

### DDL: Static

Schema creation uses hardcoded `CREATE TABLE` statements. Seed data uses hardcoded literals (`WHERE name = 'Personal'`) — not user-controllable.

---

## Findings

| # | Severity | CWE | Finding |
|---|----------|-----|---------|
| PY-SQL-1 | INFO | CWE-89 | ORM SQL is executed via `db.execute(sql)` as a rendered string. The escaping is correct, but `db.execute(sql)` with pre-rendered values is escaping-based rather than parameterized. |
| PY-SQL-2 | INFO | CWE-400 | SELECT queries use `to_sql()` without limits. The ORM's `safe_to_sql(default_limit)` is available but unused. |
| PY-SQL-3 | INFO | CWE-89 | Seed code contains `WHERE name = 'Personal'` (hardcoded literal in SQL). Not user-controllable, but breaks the pattern of parameterized queries. |

### ORM-Level Concerns (shared across all apps)

| # | Severity | CWE | Finding |
|---|----------|-----|---------|
| ORM-1 | MEDIUM | CWE-89 | `to_insert_sql`/`to_update_sql` pass `pair.key` (a `String`) to `append_safe`. Safe by construction — keys come from `cast()` which requires `SafeIdentifier` — but the type system doesn't enforce this at the call site. |
| ORM-2 | LOW | CWE-89 | `SqlDate.format_to` wraps `value.to_string()` in quotes without escaping. |
| ORM-3 | LOW | CWE-20 | `SqlFloat64.format_to` can produce `NaN`/`Infinity` — not valid SQL literals. |

---

## Verdict

**No SQL injection vulnerabilities found.** The ORM handles all user-input-to-SQL paths with type-safe escaping, and raw SQL consistently uses parameterized queries with `?` placeholders. Flask's `<int:>` route converter adds an extra layer of integer validation before ORM calls.

---

## Evolution: Temper-Level Remediation

**Date:** 2026-03-12
**Commit:** [`1df8c7a`](https://github.com/notactuallytreyanastasio/generic_orm/commit/1df8c7a)

The security analysis above identified 3 ORM-level concerns (ORM-1, ORM-2, ORM-3) shared across all 6 app implementations. Because the ORM is written once in Temper and compiled to all backends, fixing these issues at the Temper source level automatically resolves them in every language — including this Python app.

### What Changed

**ORM-1 (MEDIUM → RESOLVED): Column name type safety in INSERT/UPDATE SQL**

The `to_insert_sql()` and `to_update_sql()` methods previously passed `pair.key` (a raw `str`) to `append_safe()`. While safe by construction (keys originated from `cast()` via `SafeIdentifier.sql_value`), the type system didn't enforce this. A future refactor could have silently introduced an unvalidated code path.

The fix routes column names through the looked-up `FieldDef.name.sql_value` — a `SafeIdentifier` — so the column name in the generated SQL always comes from a validated identifier, not a raw map key.

**ORM-2 (LOW → RESOLVED): SqlDate quote escaping**

`SqlDate.format_to()` previously wrapped `value.to_string()` in quotes without escaping. The fix adds character-by-character quote escaping identical to `SqlString.format_to()`, ensuring defense-in-depth against any future Date format that might contain single quotes.

**ORM-3 (LOW → RESOLVED): SqlFloat64 NaN/Infinity handling**

`SqlFloat64.format_to()` previously called `value.to_string()` directly, which could produce `nan`, `inf`, or `-inf` — none valid SQL literals. The fix checks for these values and renders `NULL` instead, which is the safest SQL representation for non-representable floating-point values.

### Why This Matters

This is the core value proposition of a cross-compiled ORM: **one fix in Temper source propagates to all 6 backends simultaneously.** The same commit that fixed the Python compiled output also fixed JavaScript, Rust, Java, Lua, and C#. No per-language patches needed. No risk of inconsistent fixes across implementations.

### Updated Status

| Finding | Original | Current | Resolution |
|---------|----------|---------|------------|
| ORM-1 | MEDIUM | RESOLVED | Column names routed through `SafeIdentifier` |
| ORM-2 | LOW | RESOLVED | `SqlDate.format_to()` now escapes quotes |
| ORM-3 | LOW | RESOLVED | `SqlFloat64.format_to()` renders NaN/Infinity as `NULL` |
| ORM-4 | INFO | ACKNOWLEDGED | Design limitation — escaping-based, not parameterized |
