# Alloy — Python Demo App

A todo-list application built with Flask, demonstrating the [Alloy](https://github.com/notactuallytreyanastasio/alloy) compiled from Temper to Python.

## Stack

| Component | Technology |
|-----------|-----------|
| Framework | Flask 3.1 |
| Templates | Jinja2 |
| Database | SQLite via stdlib sqlite3 |
| ORM | [Alloy](https://github.com/notactuallytreyanastasio/alloy) (vendored) |
| Port | 5001 |

## ORM Usage

```python
from orm.src import safe_identifier, from_, changeset, delete_sql, SqlBuilder

# SELECT
q = (from_(safe_identifier("todos"))
     .where(where_fragment)
     .order_by(safe_identifier("created_at"), True)
     .to_sql().to_string())

# INSERT via changeset
cs = (changeset(table_def, params)
      .cast([safe_identifier("title"), safe_identifier("list_id")])
      .validate_required([safe_identifier("title")]))
sql = cs.to_insert_sql().to_string()
```

## Security Model

- **Zero SQL injection vulnerabilities** — all queries generated through the ORM
- `safe_identifier()` validates table/column names against `[a-zA-Z_][a-zA-Z0-9_]*`
- Sealed `SqlPart` hierarchy handles per-type value escaping
- `Changeset.cast()` enforces field whitelisting (CWE-915 prevention)
- DDL (`CREATE TABLE`) is the only raw SQL — static strings with no user input

## Running

```bash
pip install flask
python app.py
# Open http://localhost:5001
```

## Vendored ORM

The `vendor/` directory contains the ORM compiled from Temper to Python 3 modules. Updated automatically by CI when the ORM source changes.

---

Part of the [Alloy](https://github.com/notactuallytreyanastasio/alloy) project — write once in Temper, secure everywhere.
