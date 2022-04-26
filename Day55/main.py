from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/<name>/<age>')
def new(name, age):
    return f"<h1> my name is {name} and im {age}<h1>"

if __name__ == "__main__":
    app.run(debug=True)