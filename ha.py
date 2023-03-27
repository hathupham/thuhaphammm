from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello, World! </h1>"
if __name__ == '__master__':
    app.run()
