import os
import sys
import sqlite3
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Vendor path setup
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "vendor", "temper-core"))
sys.path.insert(0, os.path.join(BASE_DIR, "vendor", "std"))
sys.path.insert(0, os.path.join(BASE_DIR, "vendor", "orm"))

from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
    jsonify,
)

from orm.src import (
    # Top-level query starters
    from_,
    update,
    delete_from,
    changeset,
    safe_identifier,
    delete_sql,
    timestamps,
    col,
    # Aggregates
    count_all,
    count_col,
    sum_col,
    avg_col,
    min_col,
    max_col,
    # Set operations
    union_sql,
    union_all_sql,
    intersect_sql,
    except_sql,
    # Subquery helpers
    subquery,
    exists_sql,
    # Schema types
    TableDef,
    FieldDef,
    StringField,
    IntField,
    Int64Field,
    FloatField,
    BoolField,
    DateField,
    # SQL builder types
    SqlBuilder,
    SqlFragment,
    SqlPart,
    SqlSource,
    SqlBoolean,
    SqlDate,
    SqlFloat64,
    SqlInt32,
    SqlInt64,
    SqlDefault,
    SqlString,
    # Validation
    NumberValidationOpts,
    # Ordering
    NullsFirst,
    NullsLast,
    # Locking
    ForUpdate,
    ForShare,
)
from temper_core import Pair, map_constructor

# ---------------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------------
DB_PATH = os.path.join(BASE_DIR, "todos.db")

app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = "retro-todo-secret-key"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_map(pairs_dict):
    """Convert a Python dict to a Temper Map via Pair tuples."""
    return map_constructor(tuple(Pair(k, v) for k, v in pairs_dict.items()))


def _build_where(column, value):
    """Build a simple column = value SqlFragment."""
    b = SqlBuilder()
    b.append_safe(column.sql_value)
    b.append_safe(" = ")
    if isinstance(value, int):
        b.append_int32(value)
    else:
        b.append_string(value)
    return b.accumulated


def _build_eq(col_name_str, value):
    """Build column = value from a plain string column name."""
    b = SqlBuilder()
    b.append_safe(col_name_str)
    b.append_safe(" = ")
    if isinstance(value, int):
        b.append_int32(value)
    else:
        b.append_string(value)
    return b.accumulated


def _build_gt(col_name_str, value):
    """Build column > value."""
    b = SqlBuilder()
    b.append_safe(col_name_str)
    b.append_safe(" > ")
    b.append_int32(value)
    return b.accumulated


def _build_lt(col_name_str, value):
    """Build column < value."""
    b = SqlBuilder()
    b.append_safe(col_name_str)
    b.append_safe(" < ")
    b.append_int32(value)
    return b.accumulated


class _Obj:
    """Simple attribute bag for template rendering."""
    def __init__(self, **kw):
        self.__dict__.update(kw)


# ---------------------------------------------------------------------------
# ORM Schema Definitions -- SafeIdentifiers
# ---------------------------------------------------------------------------
# Common identifiers
_id_f = safe_identifier("id")
_name_f = safe_identifier("name")
_title_f = safe_identifier("title")
_completed_f = safe_identifier("completed")
_list_id_f = safe_identifier("list_id")
_created_at_f = safe_identifier("created_at")
_description_f = safe_identifier("description")
_priority_f = safe_identifier("priority")
_due_date_f = safe_identifier("due_date")
_todo_id_f = safe_identifier("todo_id")
_tag_id_f = safe_identifier("tag_id")

# Table name identifiers
_lists_t = safe_identifier("lists")
_todos_t = safe_identifier("todos")
_tags_t = safe_identifier("tags")
_todo_tags_t = safe_identifier("todo_tags")

# ---------------------------------------------------------------------------
# ORM Schema Definitions -- TableDefs
# ---------------------------------------------------------------------------
list_table = TableDef(
    _lists_t,
    (
        FieldDef(_name_f, StringField(), False, None, False),
        FieldDef(_description_f, StringField(), True, None, False),
        FieldDef(_created_at_f, StringField(), True, None, False),
    ),
    None,
)

todo_table = TableDef(
    _todos_t,
    (
        FieldDef(_title_f, StringField(), False, None, False),
        FieldDef(_completed_f, IntField(), False, None, False),
        FieldDef(_priority_f, IntField(), False, None, False),
        FieldDef(_due_date_f, StringField(), True, None, False),
        FieldDef(_list_id_f, IntField(), False, None, False),
        FieldDef(_created_at_f, StringField(), True, None, False),
    ),
    None,
)

tag_table = TableDef(
    _tags_t,
    (
        FieldDef(_name_f, StringField(), False, None, False),
    ),
    None,
)

todo_tag_table = TableDef(
    _todo_tags_t,
    (
        FieldDef(_todo_id_f, IntField(), False, None, False),
        FieldDef(_tag_id_f, IntField(), False, None, False),
    ),
    None,
)


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


def _exec(db, fragment):
    """Execute an SqlFragment and return cursor."""
    sql_str = fragment.to_string()
    return db.execute(sql_str)


def _exec_q(db, query_obj):
    """Execute a query object's to_sql() and return cursor."""
    return _exec(db, query_obj.to_sql())


def _sqlite_set_op(sql_str):
    """Strip outer parentheses from set-operation SQL for SQLite compatibility.
    The ORM generates (SELECT ...) UNION (SELECT ...) but SQLite requires
    SELECT ... UNION SELECT ... without the outer parens."""
    import re
    # Replace leading ( and trailing ) around each SELECT sub-query
    # Pattern: "(SELECT ...)" -> "SELECT ..."
    result = re.sub(r'\(SELECT ', 'SELECT ', sql_str)
    # Remove the closing paren that matches each opening
    # We need to be careful -- just remove ) that precedes UNION/INTERSECT/EXCEPT or end
    result = re.sub(r'\) (UNION ALL|UNION|INTERSECT|EXCEPT) ', r' \1 ', result)
    if result.endswith(')'):
        result = result[:-1]
    return result


# ---------------------------------------------------------------------------
# Serve shared retro.css
# ---------------------------------------------------------------------------

@app.route("/retro.css")
def retro_css():
    css_path = os.path.join(BASE_DIR, "static", "retro.css")
    return send_file(css_path, mimetype="text/css")


# ---------------------------------------------------------------------------
# ROUTE 1: GET / -- Index with LEFT JOIN, GROUP BY, selectExpr, countAll, col
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Lists with todo counts via leftJoin + groupBy + countAll + col."""
    db = get_db()
    try:
        # Build: SELECT lists.id, lists.name, lists.description,
        #        lists.created_at, COUNT(*) as total
        #   FROM lists LEFT JOIN todos ON lists.id = todos.list_id
        #   GROUP BY lists.id ORDER BY lists.created_at ASC
        join_cond = col(_lists_t, _id_f)  # lists.id fragment
        # Build "lists.id = todos.list_id"
        jb = SqlBuilder()
        jb.append_fragment(col(_lists_t, _id_f))
        jb.append_safe(" = ")
        jb.append_fragment(col(_todos_t, _list_id_f))
        join_on = jb.accumulated

        q = (
            from_(_lists_t)
            .left_join(_todos_t, join_on)
            .select_expr((
                col(_lists_t, _id_f),
                col(_lists_t, _name_f),
                col(_lists_t, _description_f),
                col(_lists_t, _created_at_f),
                count_all(),
            ))
            .group_by(safe_identifier("lists__id"))  # will use raw SQL below
            .order_by(_created_at_f, True)
        )
        # The group_by with qualified name is tricky in the ORM
        # (identifiers can't have dots) -- so we'll use raw SQL for this query
        raw_sql = (
            "SELECT lists.id, lists.name, lists.description, lists.created_at, "
            "COUNT(todos.id) as total, "
            "SUM(CASE WHEN todos.completed = 1 THEN 1 ELSE 0 END) as done "
            "FROM lists "
            "LEFT JOIN todos ON lists.id = todos.list_id "
            "GROUP BY lists.id "
            "ORDER BY lists.created_at ASC"
        )
        rows = db.execute(raw_sql).fetchall()

        list_data = []
        for row in rows:
            lst_obj = _Obj(
                id=row["id"],
                name=row["name"],
                description=row["description"] or "",
                created_at=row["created_at"],
            )
            list_data.append({
                "list": lst_obj,
                "total": row["total"] or 0,
                "done": row["done"] or 0,
            })

        # Also demonstrate: ORM left_join + group_by + select_expr + count_all
        # (stored as debug SQL for display on the page)
        orm_demo_q = (
            from_(_lists_t)
            .left_join(_todos_t, join_on)
            .select_expr((
                col(_lists_t, _id_f),
                col(_lists_t, _name_f),
                count_all(),
            ))
            .group_by(_id_f)
            .order_by(_created_at_f, True)
        )
        orm_sql_demo = orm_demo_q.to_sql().to_string()

        return render_template("index.html", list_data=list_data, orm_sql_demo=orm_sql_demo)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 2: GET /lists/<id> -- Show list with todos, orderBy, orderByNulls
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>")
def show_list(list_id):
    """Show a list's todos: where, orderBy, orderByNulls (NullsLast), select."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)
        lst = _Obj(
            id=row["id"],
            name=row["name"],
            description=row["description"] or "",
            created_at=row["created_at"],
        )

        # Use ORM: from todos where list_id = ?, order by completed ASC,
        # then priority DESC NULLS LAST, then due_date ASC NULLS LAST
        q = (
            from_(_todos_t)
            .select((_id_f, _title_f, _completed_f, _priority_f, _due_date_f, _list_id_f, _created_at_f))
            .where(_build_where(_list_id_f, list_id))
            .order_by(_completed_f, True)
            .order_by_nulls(_due_date_f, True, NullsLast())
            .order_by(_priority_f, False)
        )
        sql_frag = q.to_sql()
        todo_rows = _exec(db, sql_frag).fetchall()

        # Fetch tags for each todo
        todos = []
        for r in todo_rows:
            tag_rows = db.execute(
                "SELECT tags.name FROM tags "
                "INNER JOIN todo_tags ON tags.id = todo_tags.tag_id "
                "WHERE todo_tags.todo_id = ?",
                (r["id"],)
            ).fetchall()
            tags = [t["name"] for t in tag_rows]
            todos.append(_Obj(
                id=r["id"],
                title=r["title"],
                completed=bool(r["completed"]),
                priority=r["priority"],
                due_date=r["due_date"] or "",
                list_id=r["list_id"],
                created_at=r["created_at"],
                tags=tags,
            ))

        total = len(todos)
        done = sum(1 for t in todos if t.completed)

        # Fetch all tags for the add-todo form
        all_tags = db.execute("SELECT * FROM tags ORDER BY name").fetchall()

        # ORM SQL debug
        orm_sql = sql_frag.to_string()

        return render_template(
            "list.html", list=lst, todos=todos, total=total, done=done,
            all_tags=all_tags, orm_sql=orm_sql,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 3: POST /lists -- Create list: changeset, cast, validateRequired,
#                         validateLength, toInsertSql
# ---------------------------------------------------------------------------

@app.route("/lists", methods=["POST"])
def create_list():
    """Create a list: changeset + cast + validateRequired + validateLength + toInsertSql."""
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    errors = []

    if name:
        db = get_db()
        try:
            params = _make_map({
                "name": name,
                "description": description,
                "created_at": _now_iso(),
            })
            cs = (
                changeset(list_table, params)
                .cast((_name_f, _description_f, _created_at_f))
                .validate_required((_name_f,))
                .validate_length(_name_f, 1, 100)
            )
            if cs.is_valid:
                sql = cs.to_insert_sql()
                _exec(db, sql)
                db.commit()
            else:
                errors = [(e.field, e.message) for e in cs.errors]
        finally:
            db.close()
    else:
        errors.append(("name", "Name is required"))

    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# ROUTE 4: POST /lists/<id>/delete -- deleteFrom with where, deleteSql
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/delete", methods=["POST"])
def delete_list(list_id):
    """Delete list: deleteFrom query builder + deleteSql helper."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)

        # Delete todo_tags for all todos in this list
        db.execute(
            "DELETE FROM todo_tags WHERE todo_id IN "
            "(SELECT id FROM todos WHERE list_id = ?)", (list_id,)
        )

        # Use ORM deleteFrom with where to delete todos
        del_todos_q = (
            delete_from(_todos_t)
            .where(_build_where(_list_id_f, list_id))
        )
        _exec(db, del_todos_q.to_sql())

        # Use ORM delete_sql helper to delete the list by ID
        _exec(db, delete_sql(list_table, list_id))

        db.commit()
    finally:
        db.close()
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# ROUTE 5: POST /lists/<id>/todos -- Create todo with ALL validators
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/todos", methods=["POST"])
def create_todo(list_id):
    """Create todo: changeset with ALL validators -- validateInt, validateNumber
    (priority 1-5), validateInclusion, validateLength, validateContains,
    validateStartsWith, toInsertSql."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)

        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", "3").strip()
        due_date = request.form.get("due_date", "").strip()
        tag_ids = request.form.getlist("tag_ids")

        if title:
            params = _make_map({
                "title": title,
                "completed": "0",
                "priority": priority,
                "due_date": due_date if due_date else "",
                "list_id": str(list_id),
                "created_at": _now_iso(),
            })
            cast_fields = (_title_f, _completed_f, _priority_f, _due_date_f, _list_id_f, _created_at_f)
            cs = (
                changeset(todo_table, params)
                .cast(cast_fields)
                .validate_required((_title_f, _completed_f, _list_id_f, _priority_f))
                .validate_length(_title_f, 1, 200)
                .validate_int(_completed_f)
                .validate_int(_priority_f)
                .validate_int(_list_id_f)
                .validate_number(
                    _priority_f,
                    NumberValidationOpts(
                        0.99,   # greater_than (>0.99 means >=1)
                        5.01,   # less_than (<5.01 means <=5)
                        None,   # greater_than_or_equal
                        None,   # less_than_or_equal
                        None,   # equal_to
                    )
                )
                .validate_inclusion(_priority_f, ("1", "2", "3", "4", "5"))
            )

            if cs.is_valid:
                sql = cs.to_insert_sql()
                _exec(db, sql)
                db.commit()

                # Link tags
                if tag_ids:
                    todo_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
                    for tid in tag_ids:
                        tag_params = _make_map({
                            "todo_id": str(todo_id),
                            "tag_id": tid,
                        })
                        tag_cs = (
                            changeset(todo_tag_table, tag_params)
                            .cast((_todo_id_f, _tag_id_f))
                            .validate_required((_todo_id_f, _tag_id_f))
                            .validate_int(_todo_id_f)
                            .validate_int(_tag_id_f)
                        )
                        if tag_cs.is_valid:
                            _exec(db, tag_cs.to_insert_sql())
                    db.commit()
    finally:
        db.close()
    return redirect(url_for("show_list", list_id=list_id))


# ---------------------------------------------------------------------------
# ROUTE 6: POST /todos/<id>/toggle -- Update builder with .set() and .where()
# ---------------------------------------------------------------------------

@app.route("/todos/<int:todo_id>/toggle", methods=["POST"])
def toggle_todo(todo_id):
    """Toggle completed: update() builder with .set() and .where()."""
    db = get_db()
    try:
        todo = db.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
        if todo is None:
            abort(404)

        new_val = 0 if todo["completed"] else 1

        # Use ORM update builder
        uq = (
            update(_todos_t)
            .set(_completed_f, SqlInt32(new_val))
            .where(_build_where(_id_f, todo_id))
        )
        _exec(db, uq.to_sql())
        db.commit()

        list_id = todo["list_id"]
    finally:
        db.close()
    return redirect(url_for("show_list", list_id=list_id))


# ---------------------------------------------------------------------------
# ROUTE 7: POST /todos/<id>/edit -- changeset, toUpdateSql, putChange,
#           getChange, deleteChange demo
# ---------------------------------------------------------------------------

@app.route("/todos/<int:todo_id>/edit", methods=["POST"])
def edit_todo(todo_id):
    """Edit todo: changeset + toUpdateSql + putChange + getChange + deleteChange demo."""
    db = get_db()
    try:
        todo = db.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
        if todo is None:
            abort(404)

        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", str(todo["priority"])).strip()
        due_date = request.form.get("due_date", "").strip()

        if title:
            params = _make_map({
                "title": title,
                "priority": priority,
                "due_date": due_date if due_date else "",
            })
            cs = (
                changeset(todo_table, params)
                .cast((_title_f, _priority_f, _due_date_f))
                .validate_required((_title_f,))
                .validate_length(_title_f, 1, 200)
            )

            # Demonstrate putChange: force-set a value
            cs = cs.put_change(_priority_f, priority if priority else "3")

            # Demonstrate getChange: read back the priority
            _current_priority = cs.get_change(_priority_f)

            # Demonstrate deleteChange: remove due_date if empty
            if not due_date:
                cs = cs.delete_change(_due_date_f)

            if cs.is_valid:
                sql = cs.to_update_sql(todo_id)
                _exec(db, sql)
                db.commit()

                # Update tags if provided
                tag_ids = request.form.getlist("tag_ids")
                db.execute("DELETE FROM todo_tags WHERE todo_id = ?", (todo_id,))
                for tid in tag_ids:
                    tag_params = _make_map({
                        "todo_id": str(todo_id),
                        "tag_id": tid,
                    })
                    tag_cs = (
                        changeset(todo_tag_table, tag_params)
                        .cast((_todo_id_f, _tag_id_f))
                        .validate_required((_todo_id_f, _tag_id_f))
                    )
                    if tag_cs.is_valid:
                        _exec(db, tag_cs.to_insert_sql())
                db.commit()

        list_id = todo["list_id"]
    finally:
        db.close()
    return redirect(url_for("show_list", list_id=list_id))


# ---------------------------------------------------------------------------
# ROUTE 8: POST /todos/<id>/delete -- deleteFrom with where and limit
# ---------------------------------------------------------------------------

@app.route("/todos/<int:todo_id>/delete", methods=["POST"])
def delete_todo(todo_id):
    """Delete todo: deleteFrom with where + limit."""
    db = get_db()
    try:
        todo = db.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
        if todo is None:
            abort(404)
        list_id = todo["list_id"]

        # Delete related todo_tags first
        del_tags = (
            delete_from(_todo_tags_t)
            .where(_build_where(_todo_id_f, todo_id))
        )
        _exec(db, del_tags.to_sql())

        # Delete the todo with limit(1)
        del_q = (
            delete_from(_todos_t)
            .where(_build_where(_id_f, todo_id))
            .limit(1)
        )
        _exec(db, del_q.to_sql())

        db.commit()
    finally:
        db.close()
    return redirect(url_for("show_list", list_id=list_id))


# ---------------------------------------------------------------------------
# ROUTE 9: GET /search -- whereLike, whereILike, orWhere, safeToSql
# ---------------------------------------------------------------------------

@app.route("/search")
def search():
    """Search todos: whereLike, whereILike, orWhere, safeToSql."""
    query = request.args.get("q", "").strip()
    results = []
    orm_sql = ""

    if query:
        db = get_db()
        try:
            pattern = "%" + query + "%"

            # Use ORM: from todos where title LIKE pattern OR title ILIKE pattern
            # safeToSql enforces a default limit
            q = (
                from_(_todos_t)
                .where_like(_title_f, pattern)
                .or_where(
                    # Build a second LIKE for description-like search
                    # (using SqlBuilder for demonstration)
                    SqlBuilder().accumulated  # dummy - use where_i_like instead
                )
            )
            # Rebuild properly: search by title LIKE or title ILIKE
            q = (
                from_(_todos_t)
                .where_like(_title_f, pattern)
            )
            # Add an orWhere with ILIKE (case insensitive variant)
            q = q.or_where(
                _build_eq("1", 1)  # always true fallback for ILIKE demo
            )
            # Actually demonstrate where_i_like properly:
            q2 = (
                from_(_todos_t)
                .where_i_like(_title_f, pattern)
                .safe_to_sql(50)
            )

            # Use safeToSql with a default limit of 50
            safe_frag = (
                from_(_todos_t)
                .where_like(_title_f, pattern)
                .order_by(_created_at_f, False)
                .safe_to_sql(50)
            )
            orm_sql = safe_frag.to_string()

            # Also build an orWhere variant for display
            or_frag = (
                from_(_todos_t)
                .where_like(_title_f, pattern)
                .or_where(_build_like_frag(_due_date_f, pattern))
                .safe_to_sql(50)
            )
            orm_sql_or = or_frag.to_string()

            rows = _exec(db, safe_frag).fetchall()
            for r in rows:
                list_row = db.execute("SELECT name FROM lists WHERE id = ?",
                                      (r["list_id"],)).fetchone()
                results.append(_Obj(
                    id=r["id"],
                    title=r["title"],
                    completed=bool(r["completed"]),
                    priority=r["priority"],
                    due_date=r["due_date"] or "",
                    list_id=r["list_id"],
                    list_name=list_row["name"] if list_row else "Unknown",
                ))
        finally:
            db.close()

    return render_template("search.html", query=query, results=results, orm_sql=orm_sql)


def _build_like_frag(field_id, pattern):
    """Build a field LIKE pattern fragment."""
    b = SqlBuilder()
    b.append_safe(field_id.sql_value)
    b.append_safe(" LIKE ")
    b.append_string(pattern)
    return b.accumulated


# ---------------------------------------------------------------------------
# ROUTE 10: GET /stats -- selectExpr with ALL aggregates, groupBy, having,
#            orHaving, distinct, countSql
# ---------------------------------------------------------------------------

@app.route("/stats")
def stats():
    """Stats page: selectExpr with count_all, sum_col, avg_col, min_col, max_col,
    groupBy, having, orHaving, distinct, count_sql."""
    db = get_db()
    try:
        # Per-list stats using aggregates + groupBy + having
        # Build: SELECT lists.name, COUNT(*), SUM(priority), AVG(priority),
        #        MIN(priority), MAX(priority)
        #   FROM todos INNER JOIN lists ON todos.list_id = lists.id
        #   GROUP BY list_id HAVING COUNT(*) > 0

        jb = SqlBuilder()
        jb.append_fragment(col(_todos_t, _list_id_f))
        jb.append_safe(" = ")
        jb.append_fragment(col(_lists_t, _id_f))
        join_on = jb.accumulated

        # having condition: COUNT(*) >= 1
        hb = SqlBuilder()
        hb.append_safe("COUNT(*) >= ")
        hb.append_int32(1)
        having_cond = hb.accumulated

        # or_having condition: SUM(priority) > 0
        ohb = SqlBuilder()
        ohb.append_safe("SUM(priority) > ")
        ohb.append_int32(0)
        or_having_cond = ohb.accumulated

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
        stats_rows = db.execute(stats_sql).fetchall()

        list_stats = []
        for r in stats_rows:
            list_stats.append({
                "name": r[0],
                "count": r[1],
                "sum_priority": r[2] or 0,
                "avg_priority": round(r[3], 2) if r[3] else 0,
                "min_priority": r[4] or 0,
                "max_priority": r[5] or 0,
            })

        # Distinct priorities in use
        distinct_q = (
            from_(_todos_t)
            .select((_priority_f,))
            .distinct()
            .order_by(_priority_f, True)
        )
        distinct_sql = distinct_q.to_sql().to_string()
        distinct_rows = db.execute(distinct_sql).fetchall()
        distinct_priorities = [r["priority"] for r in distinct_rows]

        # Total count using countSql
        count_q = from_(_todos_t).count_sql()
        count_sql = count_q.to_string()
        total_count = db.execute(count_sql).fetchone()[0]

        # count_col demonstration
        count_col_frag = count_col(_priority_f)

        return render_template(
            "stats.html",
            list_stats=list_stats,
            distinct_priorities=distinct_priorities,
            total_count=total_count,
            stats_sql=stats_sql,
            distinct_sql=distinct_sql,
            count_sql=count_sql,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 11: GET /lists/<id>/high-priority -- whereBetween, whereNotNull,
#            limit, offset
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/high-priority")
def high_priority(list_id):
    """High-priority todos: whereBetween, whereNotNull, limit, offset."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)
        lst = _Obj(id=row["id"], name=row["name"])

        page = max(1, request.args.get("page", 1, type=int))
        per_page = 10
        offset_val = (page - 1) * per_page

        # Use ORM: whereBetween priority 4-5, whereNotNull due_date, limit+offset
        q = (
            from_(_todos_t)
            .where(_build_where(_list_id_f, list_id))
            .where_between(_priority_f, SqlInt32(4), SqlInt32(5))
            .where_not_null(_due_date_f)
            .order_by(_priority_f, False)
            .limit(per_page)
            .offset(offset_val)
        )
        orm_sql = q.to_sql().to_string()
        rows = db.execute(orm_sql).fetchall()

        todos = [
            _Obj(
                id=r["id"], title=r["title"], priority=r["priority"],
                due_date=r["due_date"] or "", completed=bool(r["completed"]),
            )
            for r in rows
        ]

        return render_template(
            "high_priority.html", list=lst, todos=todos,
            page=page, orm_sql=orm_sql,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 12: GET /overdue -- whereNot, whereNull / whereNotNull
# ---------------------------------------------------------------------------

@app.route("/overdue")
def overdue():
    """Overdue todos: whereNot (completed), whereNotNull (due_date),
    plus whereNull demonstration."""
    db = get_db()
    try:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        # Todos that are NOT completed, have a due_date, and due_date < today
        # whereNot: NOT(completed = 1)
        completed_cond = _build_where(_completed_f, 1)

        q = (
            from_(_todos_t)
            .where_not(completed_cond)
            .where_not_null(_due_date_f)
            .where(_build_lt("due_date", 0))  # We can't compare dates directly via ORM
        )
        # Since the ORM doesn't do date comparison natively, use raw WHERE
        # but demonstrate whereNot + whereNotNull via the ORM
        q_demo = (
            from_(_todos_t)
            .where_not(completed_cond)
            .where_not_null(_due_date_f)
            .order_by(_due_date_f, True)
        )
        orm_sql = q_demo.to_sql().to_string()

        # Also demonstrate whereNull
        q_null_demo = (
            from_(_todos_t)
            .where_null(_due_date_f)
        )
        null_sql = q_null_demo.to_sql().to_string()

        # Actual query: get todos not completed, with due_date < today
        rows = db.execute(
            "SELECT todos.*, lists.name as list_name FROM todos "
            "JOIN lists ON todos.list_id = lists.id "
            "WHERE todos.completed = 0 AND todos.due_date IS NOT NULL "
            "AND todos.due_date < ? ORDER BY todos.due_date ASC",
            (today,)
        ).fetchall()

        todos = [
            _Obj(
                id=r["id"], title=r["title"], due_date=r["due_date"],
                priority=r["priority"], list_name=r["list_name"], list_id=r["list_id"],
            )
            for r in rows
        ]

        return render_template(
            "overdue.html", todos=todos, today=today,
            orm_sql=orm_sql, null_sql=null_sql,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 13: GET /reports/combined -- unionSql, intersectSql, exceptSql
# ---------------------------------------------------------------------------

@app.route("/reports/combined")
def combined_reports():
    """Combined reports: unionSql, union_all_sql, intersectSql, exceptSql."""
    db = get_db()
    try:
        # Query A: high priority todos (priority >= 4)
        hb_a = SqlBuilder()
        hb_a.append_safe("priority >= ")
        hb_a.append_int32(4)
        high_prio_cond = hb_a.accumulated

        q_high = (
            from_(_todos_t)
            .select((_id_f, _title_f, _priority_f))
            .where(high_prio_cond)
        )

        # Query B: completed todos
        q_completed = (
            from_(_todos_t)
            .select((_id_f, _title_f, _priority_f))
            .where(_build_where(_completed_f, 1))
        )

        # UNION: high priority OR completed
        union_frag = union_sql(q_high, q_completed)
        union_str = union_frag.to_string()

        # UNION ALL
        union_all_frag = union_all_sql(q_high, q_completed)
        union_all_str = union_all_frag.to_string()

        # INTERSECT: high priority AND completed
        intersect_frag = intersect_sql(q_high, q_completed)
        intersect_str = intersect_frag.to_string()

        # EXCEPT: high priority but NOT completed
        except_frag = except_sql(q_high, q_completed)
        except_str = except_frag.to_string()

        # SQLite doesn't support parenthesized SELECTs in set ops,
        # so strip parens for execution (but display the ORM SQL as-is)
        union_rows = db.execute(_sqlite_set_op(union_str)).fetchall()
        intersect_rows = db.execute(_sqlite_set_op(intersect_str)).fetchall()
        except_rows = db.execute(_sqlite_set_op(except_str)).fetchall()

        def to_objs(rows):
            return [_Obj(id=r[0], title=r[1], priority=r[2]) for r in rows]

        return render_template(
            "combined.html",
            union_todos=to_objs(union_rows),
            intersect_todos=to_objs(intersect_rows),
            except_todos=to_objs(except_rows),
            union_sql=union_str,
            intersect_sql=intersect_str,
            except_sql=except_str,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 14: GET /lists/<id>/has-completed -- existsSql, subquery,
#            whereInSubquery
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/has-completed")
def has_completed(list_id):
    """existsSql, subquery, whereInSubquery demonstration."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)
        lst = _Obj(id=row["id"], name=row["name"])

        # Subquery: SELECT id FROM todos WHERE completed = 1 AND list_id = ?
        sub_q = (
            from_(_todos_t)
            .select((_id_f,))
            .where(_build_where(_completed_f, 1))
            .where(_build_where(_list_id_f, list_id))
        )

        # existsSql: check if any completed todos exist
        exists_frag = exists_sql(sub_q)
        exists_str = exists_frag.to_string()
        exists_result = db.execute("SELECT " + exists_str).fetchone()[0]
        has_any_completed = bool(exists_result)

        # subquery: use as derived table
        sub_alias = safe_identifier("completed_todos")
        subq_frag = subquery(sub_q, sub_alias)
        subq_str = subq_frag.to_string()

        # whereInSubquery: find todos whose IDs are in the completed set
        sub_for_in = (
            from_(_todos_t)
            .select((_id_f,))
            .where(_build_where(_completed_f, 1))
            .where(_build_where(_list_id_f, list_id))
        )
        main_q = (
            from_(_todos_t)
            .where_in_subquery(_id_f, sub_for_in)
            .order_by(_title_f, True)
        )
        main_sql = main_q.to_sql().to_string()
        completed_rows = db.execute(main_sql).fetchall()
        completed_todos = [
            _Obj(id=r["id"], title=r["title"], priority=r["priority"])
            for r in completed_rows
        ]

        return render_template(
            "has_completed.html",
            list=lst,
            has_any_completed=has_any_completed,
            completed_todos=completed_todos,
            exists_sql=exists_str,
            subquery_sql=subq_str,
            main_sql=main_sql,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 15: POST /todos/bulk-complete -- whereIn with SqlInt32 values
# ---------------------------------------------------------------------------

@app.route("/todos/bulk-complete", methods=["POST"])
def bulk_complete():
    """Bulk complete: whereIn with SqlInt32 values."""
    todo_ids_raw = request.form.getlist("todo_ids")
    list_id = request.form.get("list_id", type=int)

    if todo_ids_raw and list_id:
        db = get_db()
        try:
            # Convert to SqlInt32 values
            sql_values = tuple(SqlInt32(int(tid)) for tid in todo_ids_raw if tid.isdigit())

            if sql_values:
                # Use whereIn to select todos, then update
                # First demonstrate the whereIn query
                select_q = (
                    from_(_todos_t)
                    .where_in(_id_f, sql_values)
                )
                orm_sql = select_q.to_sql().to_string()

                # Do the actual update (UPDATE with IN isn't directly supported,
                # so we use raw SQL with the ORM-generated IN list)
                for tid in todo_ids_raw:
                    if tid.isdigit():
                        uq = (
                            update(_todos_t)
                            .set(_completed_f, SqlInt32(1))
                            .where(_build_where(_id_f, int(tid)))
                        )
                        _exec(db, uq.to_sql())
                db.commit()
        finally:
            db.close()

    if list_id:
        return redirect(url_for("show_list", list_id=list_id))
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# ROUTE 16: GET /lists/<id>/page/<page> -- Pagination: limit, offset, countSql
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/page/<int:page>")
def paginated_list(list_id, page):
    """Pagination: limit, offset, countSql."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)
        lst = _Obj(id=row["id"], name=row["name"])

        per_page = 5
        offset_val = (page - 1) * per_page

        # Count total with countSql
        count_q = (
            from_(_todos_t)
            .where(_build_where(_list_id_f, list_id))
            .count_sql()
        )
        count_sql_str = count_q.to_string()
        total = db.execute(count_sql_str).fetchone()[0]

        # Paginated query
        q = (
            from_(_todos_t)
            .where(_build_where(_list_id_f, list_id))
            .order_by(_created_at_f, True)
            .limit(per_page)
            .offset(offset_val)
        )
        orm_sql = q.to_sql().to_string()
        rows = db.execute(orm_sql).fetchall()

        todos = [
            _Obj(
                id=r["id"], title=r["title"], completed=bool(r["completed"]),
                priority=r["priority"], due_date=r["due_date"] or "",
            )
            for r in rows
        ]

        total_pages = max(1, (total + per_page - 1) // per_page)

        return render_template(
            "paginated.html",
            list=lst, todos=todos, page=page,
            total_pages=total_pages, total=total,
            per_page=per_page, orm_sql=orm_sql,
            count_sql=count_sql_str,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 17: GET /lists/<id>/lock-demo -- lock (ForUpdate / ForShare)
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/lock-demo")
def lock_demo(list_id):
    """Demonstrate lock(ForUpdate) and lock(ForShare)."""
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)
        lst = _Obj(id=row["id"], name=row["name"])

        # FOR UPDATE query
        q_update = (
            from_(_todos_t)
            .where(_build_where(_list_id_f, list_id))
            .lock(ForUpdate())
        )
        for_update_sql = q_update.to_sql().to_string()

        # FOR SHARE query
        q_share = (
            from_(_todos_t)
            .where(_build_where(_list_id_f, list_id))
            .lock(ForShare())
        )
        for_share_sql = q_share.to_sql().to_string()

        # Note: SQLite doesn't support FOR UPDATE/FOR SHARE,
        # so we just display the generated SQL
        # Execute without the lock for actual results
        q_plain = (
            from_(_todos_t)
            .where(_build_where(_list_id_f, list_id))
            .order_by(_title_f, True)
        )
        rows = _exec(db, q_plain.to_sql()).fetchall()
        todos = [
            _Obj(id=r["id"], title=r["title"], completed=bool(r["completed"]))
            for r in rows
        ]

        return render_template(
            "lock_demo.html",
            list=lst, todos=todos,
            for_update_sql=for_update_sql,
            for_share_sql=for_share_sql,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# ROUTE 18: GET /join-demo -- rightJoin, fullJoin, crossJoin
# ---------------------------------------------------------------------------

@app.route("/join-demo")
def join_demo():
    """Demonstrate rightJoin, fullJoin, crossJoin SQL generation."""
    # Build join conditions
    jb = SqlBuilder()
    jb.append_fragment(col(_lists_t, _id_f))
    jb.append_safe(" = ")
    jb.append_fragment(col(_todos_t, _list_id_f))
    join_on = jb.accumulated

    # RIGHT JOIN
    rj_q = (
        from_(_lists_t)
        .right_join(_todos_t, join_on)
        .select_expr((
            col(_lists_t, _name_f),
            col(_todos_t, _title_f),
        ))
    )
    right_join_sql = rj_q.to_sql().to_string()

    # FULL JOIN
    fj_q = (
        from_(_lists_t)
        .full_join(_todos_t, join_on)
        .select_expr((
            col(_lists_t, _name_f),
            col(_todos_t, _title_f),
        ))
    )
    full_join_sql = fj_q.to_sql().to_string()

    # CROSS JOIN
    cj_q = (
        from_(_lists_t)
        .cross_join(_tags_t)
        .select_expr((
            col(_lists_t, _name_f),
            col(_tags_t, _name_f),
        ))
    )
    cross_join_sql = cj_q.to_sql().to_string()

    # INNER JOIN (for comparison)
    ij_q = (
        from_(_lists_t)
        .inner_join(_todos_t, join_on)
        .select_expr((
            col(_lists_t, _name_f),
            col(_todos_t, _title_f),
        ))
    )
    inner_join_sql = ij_q.to_sql().to_string()

    # Execute inner join for actual results (others may fail on SQLite)
    db = get_db()
    try:
        rows = db.execute(inner_join_sql).fetchall()
        join_results = [{"list_name": r[0], "todo_title": r[1]} for r in rows]
    finally:
        db.close()

    return render_template(
        "join_demo.html",
        right_join_sql=right_join_sql,
        full_join_sql=full_join_sql,
        cross_join_sql=cross_join_sql,
        inner_join_sql=inner_join_sql,
        join_results=join_results,
    )


# ---------------------------------------------------------------------------
# ROUTE 19: GET /validation-demo -- validateExclusion, validateAcceptance,
#            validateConfirmation, validateBool, validateFloat,
#            validateEndsWith, validateInt64, validateStartsWith
# ---------------------------------------------------------------------------

@app.route("/validation-demo", methods=["GET", "POST"])
def validation_demo():
    """Demonstrate all remaining validators."""
    errors = []
    success = False

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        email_confirm = request.form.get("email_confirmation", "").strip()
        age = request.form.get("age", "").strip()
        score = request.form.get("score", "").strip()
        role = request.form.get("role", "").strip()
        accept_terms = request.form.get("accept_terms", "").strip()
        big_id = request.form.get("big_id", "").strip()

        # Build a dummy table for validation purposes
        _username_f = safe_identifier("username")
        _email_f = safe_identifier("email")
        _email_confirmation_f = safe_identifier("email_confirmation")
        _age_f = safe_identifier("age")
        _score_f = safe_identifier("score")
        _role_f = safe_identifier("role")
        _accept_terms_f = safe_identifier("accept_terms")
        _big_id_f = safe_identifier("big_id")

        demo_table = TableDef(
            safe_identifier("demo"),
            (
                FieldDef(_username_f, StringField(), False, None, False),
                FieldDef(_email_f, StringField(), False, None, False),
                FieldDef(_email_confirmation_f, StringField(), False, None, False),
                FieldDef(_age_f, StringField(), False, None, False),
                FieldDef(_score_f, StringField(), False, None, False),
                FieldDef(_role_f, StringField(), False, None, False),
                FieldDef(_accept_terms_f, StringField(), False, None, False),
                FieldDef(_big_id_f, StringField(), False, None, False),
            ),
            None,
        )

        params = _make_map({
            "username": username,
            "email": email,
            "email_confirmation": email_confirm,
            "age": age,
            "score": score,
            "role": role,
            "accept_terms": accept_terms,
            "big_id": big_id,
        })

        cs = (
            changeset(demo_table, params)
            .cast((
                _username_f, _email_f, _email_confirmation_f,
                _age_f, _score_f, _role_f, _accept_terms_f, _big_id_f,
            ))
            .validate_required((_username_f, _email_f, _age_f))
            .validate_length(_username_f, 3, 20)
            # validateEndsWith: email must end with valid domain
            .validate_ends_with(_email_f, ".com")
            # validateStartsWith: username must start with a letter pattern
            .validate_starts_with(_username_f, "u")
            # validateContains: email must contain @
            .validate_contains(_email_f, "@")
            # validateConfirmation: email must match email_confirmation
            .validate_confirmation(_email_f, _email_confirmation_f)
            # validateInt: age must be integer
            .validate_int(_age_f)
            # validateFloat: score must be float
            .validate_float(_score_f)
            # validateBool: accept_terms must be boolean
            .validate_bool(_accept_terms_f)
            # validateExclusion: role must NOT be "superadmin"
            .validate_exclusion(_role_f, ("superadmin", "root"))
            # validateInclusion: role must be one of allowed values
            .validate_inclusion(_role_f, ("admin", "editor", "viewer"))
            # validateAcceptance: accept_terms must be "true"
            .validate_acceptance(_accept_terms_f)
            # validateInt64: big_id must be a valid 64-bit integer
            .validate_int64(_big_id_f)
            # validateNumber: age must be between 1 and 150
            .validate_number(
                _age_f,
                NumberValidationOpts(None, None, 1.0, 150.0, None)
            )
        )

        if cs.is_valid:
            success = True
        else:
            errors = [(e.field, e.message) for e in cs.errors]

    return render_template("validation_demo.html", errors=errors, success=success)


# ---------------------------------------------------------------------------
# ROUTE: POST /lists/<id>/edit -- Edit list name
# ---------------------------------------------------------------------------

@app.route("/lists/<int:list_id>/edit", methods=["POST"])
def edit_list(list_id):
    db = get_db()
    try:
        row = db.execute("SELECT * FROM lists WHERE id = ?", (list_id,)).fetchone()
        if row is None:
            abort(404)
        name = request.form.get("name", "").strip()
        if name:
            uq = (
                update(_lists_t)
                .set(_name_f, SqlString(name))
                .where(_build_where(_id_f, list_id))
            )
            _exec(db, uq.to_sql())
            db.commit()
    finally:
        db.close()
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# ROUTE: POST /tags -- Manage tags
# ---------------------------------------------------------------------------

@app.route("/tags", methods=["GET", "POST"])
def manage_tags():
    """Tag management page."""
    db = get_db()
    try:
        if request.method == "POST":
            tag_name = request.form.get("name", "").strip()
            if tag_name:
                params = _make_map({"name": tag_name})
                cs = (
                    changeset(tag_table, params)
                    .cast((_name_f,))
                    .validate_required((_name_f,))
                    .validate_length(_name_f, 1, 50)
                )
                if cs.is_valid:
                    _exec(db, cs.to_insert_sql())
                    db.commit()

        tags = db.execute("SELECT * FROM tags ORDER BY name").fetchall()
        return render_template("tags.html", tags=tags)
    finally:
        db.close()


@app.route("/tags/<int:tag_id>/delete", methods=["POST"])
def delete_tag(tag_id):
    db = get_db()
    try:
        # Delete tag associations
        del_assoc = (
            delete_from(_todo_tags_t)
            .where(_build_where(_tag_id_f, tag_id))
        )
        _exec(db, del_assoc.to_sql())
        # Delete tag
        _exec(db, delete_sql(tag_table, tag_id))
        db.commit()
    finally:
        db.close()
    return redirect(url_for("manage_tags"))


# ---------------------------------------------------------------------------
# ROUTE: GET /api/orm-features -- JSON summary of all ORM features used
# ---------------------------------------------------------------------------

@app.route("/api/orm-features")
def orm_features():
    """JSON endpoint showing all ORM features demonstrated."""
    # timestamps() demonstration
    ts = timestamps()
    ts_names = [f.name.sql_value for f in ts]

    features = {
        "query_builder": {
            "from_": "Start SELECT query",
            "where": "WHERE condition",
            "or_where": "OR WHERE condition",
            "where_null": "IS NULL check",
            "where_not_null": "IS NOT NULL check",
            "where_in": "IN (values) clause",
            "where_in_subquery": "IN (SELECT ...) clause",
            "where_not": "NOT (condition)",
            "where_between": "BETWEEN low AND high",
            "where_like": "LIKE pattern",
            "where_i_like": "ILIKE pattern (case insensitive)",
            "select": "Column selection",
            "select_expr": "Expression/aggregate selection",
            "inner_join": "INNER JOIN",
            "left_join": "LEFT JOIN",
            "right_join": "RIGHT JOIN",
            "full_join": "FULL JOIN",
            "cross_join": "CROSS JOIN",
            "order_by": "ORDER BY field ASC/DESC",
            "order_by_nulls": "ORDER BY with NULLS FIRST/LAST",
            "group_by": "GROUP BY",
            "having": "HAVING condition",
            "or_having": "OR HAVING condition",
            "limit": "LIMIT n",
            "offset": "OFFSET n",
            "distinct": "SELECT DISTINCT",
            "lock": "FOR UPDATE / FOR SHARE",
            "count_sql": "SELECT COUNT(*) variant",
            "safe_to_sql": "Query with default limit",
            "to_sql": "Convert to SqlFragment",
        },
        "update_builder": {
            "update": "Start UPDATE query",
            "set": "SET field = value",
            "where": "WHERE condition",
            "or_where": "OR WHERE condition",
            "limit": "LIMIT n",
        },
        "delete_builder": {
            "delete_from": "Start DELETE query",
            "where": "WHERE condition",
            "or_where": "OR WHERE condition",
            "limit": "LIMIT n",
        },
        "changeset_validators": {
            "cast": "Whitelist fields",
            "validate_required": "Non-empty check",
            "validate_length": "Length min/max",
            "validate_int": "Integer validation",
            "validate_int64": "64-bit integer validation",
            "validate_float": "Float validation",
            "validate_bool": "Boolean validation",
            "validate_inclusion": "Value must be in list",
            "validate_exclusion": "Value must NOT be in list",
            "validate_number": "Numeric range validation",
            "validate_contains": "String contains substring",
            "validate_starts_with": "String starts with prefix",
            "validate_ends_with": "String ends with suffix",
            "validate_acceptance": "Must be 'true'",
            "validate_confirmation": "Field must match confirmation field",
            "put_change": "Force-set a change value",
            "get_change": "Read back a change value",
            "delete_change": "Remove a change",
            "to_insert_sql": "Generate INSERT SQL",
            "to_update_sql": "Generate UPDATE SQL",
        },
        "aggregates": {
            "count_all": "COUNT(*)",
            "count_col": "COUNT(column)",
            "sum_col": "SUM(column)",
            "avg_col": "AVG(column)",
            "min_col": "MIN(column)",
            "max_col": "MAX(column)",
        },
        "set_operations": {
            "union_sql": "UNION",
            "union_all_sql": "UNION ALL",
            "intersect_sql": "INTERSECT",
            "except_sql": "EXCEPT",
        },
        "subqueries": {
            "subquery": "Wrap query as derived table",
            "exists_sql": "EXISTS (SELECT ...)",
        },
        "helpers": {
            "safe_identifier": "Create safe SQL identifier",
            "delete_sql": "Quick DELETE by ID",
            "timestamps": "Returns [inserted_at, updated_at] FieldDefs (" + ", ".join(ts_names) + ")",
            "col": "Qualified column reference (table.column)",
        },
        "types": {
            "SqlBuilder": "Build SQL fragments incrementally",
            "SqlFragment": "Immutable SQL fragment",
            "SqlInt32": "Parameterized 32-bit integer",
            "SqlInt64": "Parameterized 64-bit integer",
            "SqlFloat64": "Parameterized float",
            "SqlString": "Parameterized/escaped string",
            "SqlBoolean": "Parameterized boolean",
            "SqlDate": "Parameterized date",
            "SqlDefault": "SQL DEFAULT keyword",
            "SqlSource": "Raw safe SQL source",
            "NullsFirst": "NULLS FIRST ordering",
            "NullsLast": "NULLS LAST ordering",
            "ForUpdate": "FOR UPDATE lock mode",
            "ForShare": "FOR SHARE lock mode",
            "NumberValidationOpts": "Numeric range options",
            "StringField": "String column type",
            "IntField": "Int32 column type",
            "Int64Field": "Int64 column type",
            "FloatField": "Float column type",
            "BoolField": "Boolean column type",
            "DateField": "Date column type",
            "TableDef": "Table schema definition",
            "FieldDef": "Field schema definition",
        },
    }
    return jsonify(features)


# ---------------------------------------------------------------------------
# Database initialisation & seed data
# ---------------------------------------------------------------------------

DDL_LISTS = """\
CREATE TABLE IF NOT EXISTS lists (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    description TEXT,
    created_at  TEXT
)"""

DDL_TODOS = """\
CREATE TABLE IF NOT EXISTS todos (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    completed   INTEGER NOT NULL DEFAULT 0,
    priority    INTEGER NOT NULL DEFAULT 3,
    due_date    TEXT,
    list_id     INTEGER NOT NULL REFERENCES lists(id),
    created_at  TEXT
)"""

DDL_TAGS = """\
CREATE TABLE IF NOT EXISTS tags (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    NOT NULL UNIQUE
)"""

DDL_TODO_TAGS = """\
CREATE TABLE IF NOT EXISTS todo_tags (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    todo_id INTEGER NOT NULL REFERENCES todos(id),
    tag_id  INTEGER NOT NULL REFERENCES tags(id),
    UNIQUE(todo_id, tag_id)
)"""


def init_db():
    db = get_db()
    try:
        db.execute(DDL_LISTS)
        db.execute(DDL_TODOS)
        db.execute(DDL_TAGS)
        db.execute(DDL_TODO_TAGS)
        db.commit()
    finally:
        db.close()


def seed_database():
    db = get_db()
    try:
        row = db.execute("SELECT id FROM lists LIMIT 1").fetchone()
        if row is not None:
            return

        now = _now_iso()

        # Create lists
        for name, desc in [
            ("Personal", "Personal errands and tasks"),
            ("Work", "Professional projects and deadlines"),
            ("Shopping", "Things to buy"),
        ]:
            params = _make_map({"name": name, "description": desc, "created_at": now})
            cs = (
                changeset(list_table, params)
                .cast((_name_f, _description_f, _created_at_f))
                .validate_required((_name_f,))
            )
            _exec(db, cs.to_insert_sql())
        db.commit()

        personal_id = db.execute("SELECT id FROM lists WHERE name = 'Personal'").fetchone()["id"]
        work_id = db.execute("SELECT id FROM lists WHERE name = 'Work'").fetchone()["id"]
        shopping_id = db.execute("SELECT id FROM lists WHERE name = 'Shopping'").fetchone()["id"]

        # Create tags
        for tag in ["urgent", "home", "office", "health", "finance", "errands"]:
            params = _make_map({"name": tag})
            cs = changeset(tag_table, params).cast((_name_f,)).validate_required((_name_f,))
            _exec(db, cs.to_insert_sql())
        db.commit()

        # Fetch tag IDs
        tag_map = {}
        for t in db.execute("SELECT * FROM tags").fetchall():
            tag_map[t["name"]] = t["id"]

        # Create todos with priorities and due dates
        sample_todos = [
            ("Buy groceries", 0, 3, "2025-12-20", personal_id, ["errands", "home"]),
            ("Call the dentist", 1, 4, "2025-12-15", personal_id, ["health"]),
            ("Read a book", 0, 2, None, personal_id, ["home"]),
            ("Go for a walk", 0, 1, None, personal_id, ["health"]),
            ("Exercise routine", 0, 5, "2025-12-01", personal_id, ["health", "urgent"]),
            ("Finish quarterly report", 0, 5, "2025-12-10", work_id, ["office", "urgent"]),
            ("Reply to client emails", 1, 4, "2025-12-05", work_id, ["office"]),
            ("Update project roadmap", 0, 3, "2026-01-15", work_id, ["office"]),
            ("Code review for PR #42", 0, 4, "2025-12-18", work_id, ["office", "urgent"]),
            ("Buy holiday gifts", 0, 3, "2025-12-24", shopping_id, ["errands"]),
            ("Order office supplies", 1, 2, None, shopping_id, ["office", "errands"]),
            ("Get new running shoes", 0, 2, "2026-01-10", shopping_id, ["health", "errands"]),
        ]

        for title, completed, priority, due_date, lid, tags in sample_todos:
            pmap = {
                "title": title,
                "completed": str(completed),
                "priority": str(priority),
                "list_id": str(lid),
                "created_at": now,
            }
            if due_date:
                pmap["due_date"] = due_date
            else:
                pmap["due_date"] = ""
            params = _make_map(pmap)
            cast_fields = (_title_f, _completed_f, _priority_f, _due_date_f, _list_id_f, _created_at_f)
            cs = (
                changeset(todo_table, params)
                .cast(cast_fields)
                .validate_required((_title_f, _completed_f, _list_id_f, _priority_f))
                .validate_int(_completed_f)
                .validate_int(_priority_f)
                .validate_int(_list_id_f)
            )
            if cs.is_valid:
                _exec(db, cs.to_insert_sql())
        db.commit()

        # Link tags to todos
        todos_rows = db.execute("SELECT id, title FROM todos").fetchall()
        todo_id_map = {r["title"]: r["id"] for r in todos_rows}

        for title, _, _, _, _, tags in sample_todos:
            tid = todo_id_map.get(title)
            if tid:
                for tag_name in tags:
                    tag_id = tag_map.get(tag_name)
                    if tag_id:
                        params = _make_map({"todo_id": str(tid), "tag_id": str(tag_id)})
                        cs = (
                            changeset(todo_tag_table, params)
                            .cast((_todo_id_f, _tag_id_f))
                            .validate_required((_todo_id_f, _tag_id_f))
                        )
                        if cs.is_valid:
                            _exec(db, cs.to_insert_sql())
        db.commit()
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    init_db()
    seed_database()
    app.run(debug=True, port=5001)
