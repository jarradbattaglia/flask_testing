from flask import Flask, request
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello %s </h1>" % name

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return "<h1>Your browser is %s</h1>" % user_agent
    #return "<h1>Hello World </h1>"



if __name__ == "__main__":
    app.run(debug=True)
