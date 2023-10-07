"""
Finance index (main) view.

URLs include:
/
"""
import flask
import finance


@finance.app.route('/')
def show_index():
    """Display / route."""

     # Connect to database
    connection = finance.model.get_db()

    # Query database
    cur = connection.execute(
        "SELECT * "
        "FROM transactions"
    )
    trnz = cur.fetchall()

    balance=0
    for trn in trnz:
        balance += trn["amount"]
    context = {"trnz": trnz, "balance": balance}
    return flask.render_template("index.html", **context)