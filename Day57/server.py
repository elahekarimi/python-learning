from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)



@app.route('/')
def new():
    random_num = random.randint(1, 10)
    my_time = datetime.datetime.now()
    return render_template("index.html", num=random_num, t=my_time)

@app.route('/guss/<name>')
def guss(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_recponse = requests.get(gender_url)
    gender_data = gender_recponse.json()
    gender = gender_data['gender']
    age_url = f"https://api.agify.io?name={name}"
    age_responce = requests.get(age_url)
    age_data = age_responce.json()
    age = age_data["age"]
    return render_template("guss.html", person_name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)