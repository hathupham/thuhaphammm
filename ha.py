from flask import Flask

app = Flask(__name__)

@app.route("/hathuphammm")
def home():
    return "<h1> Hello, World! </h1>"
