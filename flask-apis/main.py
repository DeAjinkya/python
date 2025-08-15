from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
        "ajinkya":100,
        "rohan":67,
        "aakash":78
    }
    values = [1,marks,45,"bye"]
    return jsonify(values)

app.run(debug=True)