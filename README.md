# Alloy Todo App -- Python

A full-featured todo list manager built with **Flask + Jinja2 + sqlite3** that demonstrates **every feature** of the [Alloy ORM](https://github.com/notactuallytreyanastasio/alloy) compiled from Temper to Python. The app exercises all **15 changeset validators** and the complete query builder API across **19+ routes** with a retro Mac System 6 + Windows 95 hybrid UI theme.

## Overview

This application is a complete, working todo list manager with lists, todos, tags, priorities, due dates, search, stats, pagination, lock demos, join demos, and a validation showcase. Every database interaction -- from simple lookups to complex aggregate queries with set operations -- is built through the Alloy ORM's type-safe query builder and changeset validation pipeline. No hand-written SQL touches user input.

The UI features a retro aesthetic blending Windows 95 chrome (beveled borders, grey panels, classic button styles) with a Mac System 6 desktop feel. Inline editing, confirmation dialogs, priority badges (color-coded 1-5), due date pickers, and tag chips are all supported.

## Data Model

Four tables with foreign key relationships:

```sql
lists (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    description TEXT,
    created_at  TEXT
)

todos (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
    completed   INTEGER NOT NULL DEFAULT 0,
    priority    INTEGER NOT NULL DEFAULT 3,
    due_date    TEXT,
    list_id     INTEGER NOT NULL REFERENCES lists(id),
    created_at  TEXT
)

tags (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)

todo_tags (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    todo_id INTEGER NOT NULL REFERENCES todos(id),
    tag_id  INTEGER NOT NULL REFERENCES tags(id),
    UNIQUE(todo_id, tag_id)
)
```

All four tables have corresponding `TableDef` and `FieldDef` schema definitions in `app.py` using `safe_identifier()` for every table and column name.

## Complete ORM Feature Coverage

### Query Builder

| ORM Feature | Route / Location | Description |
|---|---|---|
| `from_` | `GET /`, `GET /lists/{id}`, all queries | Start SELECT query on a table |
| `select` | `GET /lists/{id}` (column selection) | Select specific columns by `SafeIdentifier` |
| `select_expr` | `GET /` (list counts), `GET /stats` | Select with aggregate expressions and `col()` refs |
| `where` | `GET /lists/{id}`, `POST /todos/{id}/toggle` | WHERE with `SqlBuilder`-generated conditions |
| `or_where` | `GET /search` (OR search), `GET /stats` | OR WHERE for compound conditions |
| `where_null` | `GET /overdue` (demo), template display | `IS NULL` check on `due_date` |
| `where_not_null` | `GET /overdue`, `GET /lists/{id}/high-priority` | `IS NOT NULL` check on `due_date` |
| `where_in` | `POST /bulk-complete` | `IN (values)` with `SqlInt32` list |
| `where_in_subquery` | `GET /lists/{id}/has-completed` | `IN (SELECT ...)` for subquery filtering |
| `where_not` | `GET /overdue` | `NOT (condition)` for negation |
| `where_between` | `GET /lists/{id}/high-priority` | `BETWEEN low AND high` with `SqlInt32` bounds |
| `where_like` | `GET /search?q=...` | `LIKE` pattern matching on title |
| `where_i_like` | `GET /search` (case-insensitive demo) | Case-insensitive `ILIKE` pattern matching |
| `order_by` | `GET /lists/{id}`, `GET /stats` | `ORDER BY` with ASC/DESC control |
| `order_by_nulls` | `GET /lists/{id}` (`NullsLast` on due_date) | `NULLS FIRST` / `NULLS LAST` ordering |
| `group_by` | `GET /`, `GET /stats` | `GROUP BY` for aggregate grouping |
| `having` | `GET /stats` | `HAVING` with count threshold |
| `or_having` | `GET /stats` | `OR HAVING` for compound group filters |
| `limit` | `GET /lists/{id}` (single lookup), `POST /todos/{id}/delete` | `LIMIT n` for result capping |
| `offset` | `GET /lists/{id}/high-priority`, `GET /lists/{id}/page/{page}` | `OFFSET n` for pagination |
| `distinct` | `GET /stats` (distinct priorities) | `SELECT DISTINCT` for unique values |
| `lock (ForUpdate)` | `GET /lock-demo/{id}` | `FOR UPDATE` row-level locking (SQL display) |
| `lock (ForShare)` | `GET /lock-demo/{id}` | `FOR SHARE` row-level locking (SQL display) |
| `count_sql` | `GET /stats`, `GET /lists/{id}/page/{page}` | `SELECT COUNT(*)` variant |
| `safe_to_sql` | `GET /search` | Query with enforced default limit |
| `to_sql` | All routes | Convert query to `SqlFragment` for execution |

### Joins

| ORM Feature | Route / Location | Description |
|---|---|---|
| `inner_join` | `GET /stats` (todos with lists) | Todos joined with lists for aggregate stats |
| `left_join` | `GET /` (lists with counts) | Lists left-joined with todos for counts |
| `right_join` | `GET /join-demo` | SQL generation demo (RIGHT JOIN) |
| `full_join` | `GET /join-demo` | SQL generation demo (FULL OUTER JOIN) |
| `cross_join` | `GET /join-demo` | SQL generation demo (CROSS JOIN lists x tags) |

### Aggregates

| ORM Feature | Route / Location | Description |
|---|---|---|
| `count_all` | `GET /` (list counts), `GET /stats` | `COUNT(*)` for total counts |
| `count_col` | `GET /stats` (count_col demo) | `COUNT(column)` for non-null counts |
| `sum_col` | `GET /stats` (sum priorities) | `SUM(priority)` across all todos |
| `avg_col` | `GET /stats` (average priority) | `AVG(priority)` average computation |
| `min_col` | `GET /stats` (min priority) | `MIN(priority)` minimum value |
| `max_col` | `GET /stats` (max priority) | `MAX(priority)` maximum value |

### Set Operations

| ORM Feature | Route / Location | Description |
|---|---|---|
| `union_sql` | `GET /combined` | UNION of high-priority and completed queries |
| `union_all_sql` | `GET /combined` | UNION ALL (preserves duplicates) |
| `intersect_sql` | `GET /combined` | INTERSECT -- high-priority AND completed |
| `except_sql` | `GET /combined` | EXCEPT -- high-priority but NOT completed |

### Subqueries

| ORM Feature | Route / Location | Description |
|---|---|---|
| `subquery` | `GET /lists/{id}/has-completed` | Wrap query as derived table with alias |
| `exists_sql` | `GET /lists/{id}/has-completed` | `EXISTS (SELECT ...)` for existence checks |

### Mutations

| ORM Feature | Route / Location | Description |
|---|---|---|
| `update().set().where().to_sql()` | `POST /todos/{id}/toggle`, `POST /lists/{id}/edit` | UPDATE with `SqlInt32` / `SqlString` values |
| `delete_from().where().to_sql()` | `POST /todos/{id}/delete`, `POST /tags/{id}/delete` | DELETE with WHERE conditions and limit |
| `delete_sql` | `POST /lists/{id}/delete`, `POST /tags/{id}/delete` | Quick DELETE by primary key ID |

### Changeset Validation

| ORM Feature | Route / Location | Description |
|---|---|---|
| `changeset` | `POST /lists/create`, `POST /lists/{id}/todos`, `POST /tags/create` | Create changeset from TableDef + params |
| `cast` | All POST routes | Whitelist allowed fields |
| `validate_required` | `POST /lists/create`, `POST /lists/{id}/todos` | Non-empty field check |
| `validate_length` | `POST /lists/create`, `POST /lists/{id}/todos`, `POST /tags/create` | Min/max string length |
| `validate_int` | `POST /lists/{id}/todos` | Integer parsing validation |
| `validate_int64` | `GET /validation-demo` | 64-bit integer validation |
| `validate_float` | `GET /validation-demo` | Float parsing validation |
| `validate_bool` | `GET /validation-demo` | Boolean parsing validation |
| `validate_inclusion` | `POST /lists/{id}/todos`, `GET /validation-demo` | Value must be in allowed list |
| `validate_exclusion` | `GET /validation-demo` | Value must NOT be in blocked list |
| `validate_number` | `POST /lists/{id}/todos`, `GET /validation-demo` | Numeric range with `NumberValidationOpts` |
| `validate_acceptance` | `GET /validation-demo` | Must be truthy ("true", "1", "yes") |
| `validate_confirmation` | `GET /validation-demo` | Two fields must match |
| `validate_contains` | `GET /validation-demo` | String must contain substring |
| `validate_starts_with` | `GET /validation-demo` | String must start with prefix |
| `validate_ends_with` | `GET /validation-demo` | String must end with suffix |
| `put_change` | `POST /todos/{id}/edit` | Programmatically set a changeset value |
| `get_change` | `POST /todos/{id}/edit` | Read back a changeset value |
| `delete_change` | `POST /todos/{id}/edit` | Remove a change (due_date if empty) |
| `to_insert_sql` | All create routes | Generate INSERT SQL |
| `to_update_sql` | `POST /todos/{id}/edit` | Generate UPDATE SQL for a given ID |

### Types Used

| Type | Usage |
|---|---|
| `SafeIdentifier` | Every table and column name (`safe_identifier()`) |
| `TableDef` | Schema for `lists`, `todos`, `tags`, `todo_tags` |
| `FieldDef` | Each column in every table |
| `StringField` | `name`, `title`, `description`, `due_date`, `created_at` |
| `IntField` | `completed`, `priority`, `list_id`, `todo_id`, `tag_id` |
| `Int64Field` | Available, used in validation demo schema |
| `FloatField` | Available, used in validation demo schema |
| `BoolField` | Available, used in validation demo schema |
| `DateField` | Date column type |
| `SqlBuilder` | Manual fragment construction (join conditions, WHERE clauses, HAVING) |
| `SqlFragment` | Immutable SQL fragments from `to_sql()` |
| `SqlString` | Parameterized string values (`SqlString(name)` in SET clauses) |
| `SqlInt32` | Parameterized integer values (priority, completed toggle, WHERE IN) |
| `SqlInt64` | 64-bit integer type |
| `SqlFloat64` | Float type (used in `or_having` condition: `append_float64`) |
| `SqlBoolean` | Boolean type |
| `SqlDate` | Date type |
| `SqlDefault` | SQL DEFAULT keyword |
| `SqlSource` | Raw safe SQL source |
| `NumberValidationOpts` | Priority range validation (`greater_than`, `less_than`, `gte`, `lte`, `equal_to`) |
| `NullsFirst` | NULLS FIRST ordering mode |
| `NullsLast` | NULLS LAST ordering mode |
| `ForUpdate` | FOR UPDATE lock mode |
| `ForShare` | FOR SHARE lock mode |

## Route Reference

| Route | Method | Description | Key ORM Features |
|---|---|---|---|
| `/` | GET | Lists index with counts | `from_`, `left_join`, `select_expr`, `group_by`, `order_by`, `count_all`, `col` |
| `/lists/create` | POST | Create a new list | `changeset`, `cast`, `validate_required`, `validate_length`, `to_insert_sql` |
| `/lists/{id}` | GET | Show list with todos | `from_`, `select`, `where`, `order_by`, `order_by_nulls`, `NullsLast` |
| `/lists/{id}/edit` | POST | Edit list name | `update`, `set` with `SqlString`, `where` |
| `/lists/{id}/delete` | POST | Delete list and cascade | `delete_from().where()`, `delete_sql` |
| `/lists/{id}/todos` | POST | Create todo (full validation) | `changeset`, `cast`, `validate_required`, `validate_int`, `validate_number`, `validate_inclusion`, `validate_length`, `to_insert_sql` |
| `/todos/{id}/toggle` | POST | Toggle completed state | `update().set().where()`, `SqlInt32` |
| `/todos/{id}/edit` | POST | Edit todo (changeset mutation) | `changeset`, `put_change`, `get_change`, `delete_change`, `to_update_sql` |
| `/todos/{id}/delete` | POST | Delete a todo | `delete_from().where().limit()`, `delete_sql` |
| `/search` | GET | Search by title | `where_like`, `where_i_like`, `or_where`, `safe_to_sql` |
| `/stats` | GET | Aggregate statistics | `select_expr`, `count_all`, `count_col`, `sum_col`, `avg_col`, `min_col`, `max_col`, `inner_join`, `group_by`, `having`, `or_having`, `distinct`, `count_sql` |
| `/lists/{id}/high-priority` | GET | High-priority with due dates | `where_between`, `where_not_null`, `limit`, `offset` |
| `/overdue` | GET | Overdue todos | `where_not`, `where_not_null`, `where_null` (demo) |
| `/combined` | GET | Set operations report | `union_sql`, `union_all_sql`, `intersect_sql`, `except_sql` |
| `/lists/{id}/has-completed` | GET | Subquery demos | `exists_sql`, `subquery`, `where_in_subquery` |
| `/bulk-complete` | POST | Bulk mark complete | `where_in` with `SqlInt32` values |
| `/lists/{id}/page/{page}` | GET | Paginated todos | `limit`, `offset`, `count_sql` |
| `/lock-demo/{id}` | GET | Lock mode demos | `lock(ForUpdate())`, `lock(ForShare())` |
| `/join-demo` | GET | All join types | `inner_join`, `right_join`, `full_join`, `cross_join` |
| `/tags` | GET/POST | Tag management | `changeset`, `validate_required`, `validate_length`, `to_insert_sql` |
| `/tags/{id}/delete` | POST | Delete tag | `delete_from().where()`, `delete_sql` |
| `/todos/{id}/tag` | POST | Tag a todo | `changeset` on `todo_tag_table` |
| `/todos/{id}/untag/{tag_id}` | POST | Remove tag | `delete_from().where()` |
| `/validation-demo` | GET/POST | All 15 validators | `validate_required`, `validate_length`, `validate_int`, `validate_int64`, `validate_float`, `validate_bool`, `validate_inclusion`, `validate_exclusion`, `validate_number`, `validate_acceptance`, `validate_confirmation`, `validate_contains`, `validate_starts_with`, `validate_ends_with` |

## Code Examples

### Query Builder -- Aggregates with Inner Join, GroupBy, Having

```python
# From app.py -- per-list stats using all aggregate functions
stats_q = (
    from_(_todos_t)
    .inner_join(_lists_t, join_on)
    .select_expr((
        col(_lists_t, _name_f),
        count_all(),
        sum_col(_priority_f),
        avg_col(_priority_f),
        min_col(_priority_f),
        max_col(_priority_f),
    ))
    .group_by(_list_id_f)
    .having(having_cond)
    .or_having(or_having_cond)
    .order_by(_list_id_f, True)
)
stats_sql = stats_q.to_sql().to_string()
```

### Changeset -- Full Validation Pipeline with All 15 Validators

```python
# From app.py -- validation demo exercising every validator
cs = (
    changeset(demo_table, params)
    .cast((fields...))
    .validate_required((_username_f, _email_f, _age_f))
    .validate_length(_username_f, 3, 20)
    .validate_ends_with(_email_f, ".com")
    .validate_starts_with(_username_f, "u")
    .validate_contains(_email_f, "@")
    .validate_confirmation(_email_f, _email_confirmation_f)
    .validate_int(_age_f)
    .validate_float(_score_f)
    .validate_bool(_accept_terms_f)
    .validate_exclusion(_role_f, ("superadmin", "root"))
    .validate_inclusion(_role_f, ("admin", "editor", "viewer"))
    .validate_acceptance(_accept_terms_f)
    .validate_int64(_big_id_f)
    .validate_number(_age_f, NumberValidationOpts(None, None, 1.0, 150.0, None))
)
```

### Set Operations -- Union, Intersect, Except

```python
# From app.py -- combined reports page
q_high = from_(_todos_t).select((_id_f, _title_f, _priority_f)).where(high_prio_cond)
q_completed = from_(_todos_t).select((_id_f, _title_f, _priority_f)).where(completed_cond)

union_frag     = union_sql(q_high, q_completed)
intersect_frag = intersect_sql(q_high, q_completed)
except_frag    = except_sql(q_high, q_completed)
```

### Subquery + EXISTS + WHERE IN SUBQUERY

```python
# From app.py -- check for completed todos using three subquery patterns
sub_q = from_(_todos_t).select((_id_f,)).where(completed_cond).where(list_cond)

# EXISTS: does any completed todo exist?
exists_frag = exists_sql(sub_q)

# Subquery: use as derived table
subq_frag = subquery(sub_q, safe_identifier("completed_todos"))

# WHERE IN SUBQUERY: find todos whose IDs are in the completed set
main_q = from_(_todos_t).where_in_subquery(_id_f, sub_for_in).order_by(_title_f, True)
```

## Security Model

The Alloy ORM enforces **5 layers of defense** against SQL injection and mass-assignment attacks:

1. **SafeIdentifier** -- Table and column names are validated against `[a-zA-Z_][a-zA-Z0-9_]*` at construction time. Invalid identifiers throw immediately.
2. **SqlBuilder / SqlFragment** -- All values are type-dispatched through `SqlPart` subclasses (`SqlString`, `SqlInt32`, `SqlFloat64`, etc.) that handle escaping per type. No string interpolation.
3. **Changeset `cast()`** -- Field whitelisting prevents mass-assignment (CWE-915). Only explicitly listed fields are accepted from user input.
4. **Changeset validators** -- 15 validators catch invalid data before any SQL is generated. Invalid changesets refuse to produce SQL.
5. **No raw SQL with user input** -- DDL (`CREATE TABLE`) is the only raw SQL in the codebase, using static strings with zero user input.

For the full MITRE CWE analysis, see [SECURITY_ANALYSIS.md](SECURITY_ANALYSIS.md) or the [main Alloy repository](https://github.com/notactuallytreyanastasio/alloy).

## Running the App

### Prerequisites

- Python 3.9+
- Flask (`pip install flask`)

### Install and Run

```bash
pip install -r requirements.txt
python app.py
```

The app starts at **http://localhost:5001** with seeded sample data (3 lists, 12 todos, 6 tags).

## Source

- **Alloy ORM (Temper source):** [github.com/notactuallytreyanastasio/alloy](https://github.com/notactuallytreyanastasio/alloy)
- **Compiled Python library:** [github.com/notactuallytreyanastasio/alloy-py](https://github.com/notactuallytreyanastasio/alloy-py)

The `vendor/` directory contains the ORM compiled from Temper to Python 3 modules. Updated automatically by CI when the ORM source changes.

---

Part of the [Alloy](https://github.com/notactuallytreyanastasio/alloy) project -- write once in Temper, compile to Java/Python/Lua/JS, secure everywhere.
