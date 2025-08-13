from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "john":34,
        "raj":56,
        "mark":77,
        "smash":89
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)