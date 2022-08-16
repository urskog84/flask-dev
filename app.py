from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

init_data = {"first": "Svante", "last": "Testssin"}


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", data=init_data)

@app.route("/run", methods=["POST"])
def run():
    y = request.form['lname']
    x =    {
        "first" : y,
        "last"  : "Fors"
    }
    return render_template("index.html", data=x)

