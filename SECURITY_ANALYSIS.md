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
