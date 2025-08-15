from flask import Flask,flash,render_template,redirect

app = Flask(__name__)

#RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
app.secret_key = "3256ywgvdnfiuve86w8"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("logged out","success")
    return render_template("logout.html")

app.run(debug=True)

#RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.