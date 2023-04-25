from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html")


@app.route("/user/<name>")
def get_user(name):
    return render_template("user.html", username=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html", error=e), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("error_500.html", error=e), 500


app.run(debug=True)
