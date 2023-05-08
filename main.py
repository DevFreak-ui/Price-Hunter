from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/user/<username>")
def user(username):
    return f'Hi! My name is {username}'