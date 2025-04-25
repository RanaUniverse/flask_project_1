from flask import Flask
from flask import render_template

app = Flask(__name__)


my_name = "Rana Universe"


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/help")
def help_page():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
