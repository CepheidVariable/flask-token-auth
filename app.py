from flask import Flask

#inialize flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>A simple token auth server.</h1>"

if __name__ == "__main__":
    app.run(debug=True)