from flask import Flask,render_template,request

app = Flask(__name__)
# localhost/?name=jack&tokens=4000
@app.route("/")
def hello_world():
    name = "ajinkya"
    token = 4000
    if "name" in request.args.keys():
        name = request.args['name']

    if "token" in request.args.keys():
        token = request.args['tokens']

    return render_template("index.html", name=name, token=token)

app.run(debug=True)