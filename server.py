"""Skills 5: SQLAlchemy & AJAX

This file is used to run the server for Part 4 of Skills 5: SQLAlchemy & AJAX.

You do not need to edit this file for Part 4. Please do you work in
templates/index.html instead.
"""

from flask import Flask, jsonify, render_template
from model import connect_to_db, Human


app = Flask(__name__)


@app.route("/")
def homepage():
    """Show the homepage."""

    return render_template("index.html")
    

@app.route("/api/human/<int:human_id>")
def get_human(human_id):
    """Return a human from the database as JSON."""

    human = Human.query.get(human_id)

    if human:
        return jsonify({"status": "success",
                        "human_id": human.human_id,
                        "fname": human.fname,
                        "lname": human.lname,
                        "email": human.email})
    else:
        return jsonify({"status": "error",
                        "message": "No human found with that ID"})


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
