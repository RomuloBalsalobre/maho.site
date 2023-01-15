from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")
    
@app.route("/users/<username>")
def users(username):
    return render_template("users.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
    
