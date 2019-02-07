from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/publication_list")
def publication_list():
    return render_template("publication_list.html")

if __name__ == '__main__':
    app.run(debug=True)
