from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def new():
    return render_template("myindex.html")


if __name__ == "__main__":
    app.run(debug=True)