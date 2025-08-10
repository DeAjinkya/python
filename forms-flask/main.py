from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    print(request.method)
    print(request.form)

    if (request.method == "POST"):
        # handle the form
        with open("file.txt","w") as f:
            f.write(f"the name is {request.form['name']} and email is {request.form['email']}")

    return render_template("contact.html")

app.run(debug=True)