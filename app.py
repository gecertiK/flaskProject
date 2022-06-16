from flask import Flask, request
from faker import Faker
import pandas as pd
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return """ 
    <h1>Hello, User!</h1>
    <h2>If you would like to go to the next page, you should enter:</h2> 
    <ol type='1'>
    <li>/requirements - on this page you`ll see all libraries that used in this project,</li>
    <li>/generate-users - on this page you`ll see people`s names and their email`s,</li>
    <li>/mean - on this page you`ll see the average heights and weights persons,</li>
    <li>/space = on this page you`ll see how many peoples in space.</li>
    <ol>
    """


# Work №1 не могу понять как сделать в столбик???
@app.route("/requirements/")
def requirements():
    file = "requirements.txt"
    with open(file, "r") as data:
        text = data.read()
    return text


# Work №2 не могу понять как сделать правильную нумерацию???
@app.route("/generate-users/")
@app.route("/generate-users/<int:count>")
def gen_users():
    l = []
    count_users = request.args.get("count", default=100, type=int)
    for i in range(count_users):
        fake = Faker()
        name = fake.first_name()
        email = fake.email()
        l.append(f"<ol type='1'><li>{name} {email}</li></ol>")
    return " ".join(l)


# Work №3
@app.route("/mean/")
def read_data_scv():
    data = pd.read_csv('hw.csv')
    inches_cm = 0
    pounds_kg = 0
    for i in range(len(data)):
        inches_cm += data.iloc[i][1] / len(data) * 2.51
        pounds_kg += data.iloc[i][2] / len(data) / 2.205
    return f"""
    <p>Average (cm) = {round(inches_cm, 2)}</p> 
    Average (kg) = {round(pounds_kg, 2)}
    """


# Work №4
@app.route("/space/")
def people_in_space():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url).json()
    astronauts = ''
    for astronaut in response.get('people'):
        astronauts += f"<li>{astronaut.get('name')}</li>"
    return f"""
    <h1>Astronauts</h1>
    <h2>There are {response.get('number')} astronauts in space</h2> 
    {astronauts}
    """
