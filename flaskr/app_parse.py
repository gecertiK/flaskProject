from flask import request, Blueprint, render_template
from faker import Faker
import pandas as pd
import requests

bp = Blueprint("app_parse", __name__)


@bp.route('/')
def hello_world():  # put application's code here
    return render_template("first_page.html")


# Work №1 не могу понять как сделать в столбик???
@bp.route("/requirements/")
def requirements():
    file = "requirements.txt"
    with open(file, "r") as data:
        text = data.readlines()
    return render_template("requirement.html", text=text)


# Work №2 не могу понять как сделать правильную нумерацию???
@bp.route("/generate-users/")
def gen_users():
    count_users = request.args.get("count", default=100, type=int)
    fake = Faker()
    return render_template("gen_users.html", count=count_users, fake=fake)


# Work №3
@bp.route("/mean/")
def read_data_scv():
    data = pd.read_csv('hw.csv')
    inches_cm = round(data[' "Height(Inches)"'].mean() * 2.51, 2)
    pounds_kg = round(data[' "Weight(Pounds)"'].mean() / 2.205, 2)
    # inches_cm = 0
    # pounds_kg = 0
    # for i in range(len(data)):
    #     inches_cm += data.iloc[i][1] / len(data) * 2.51
    #     pounds_kg += data.iloc[i][2] / len(data) / 2.205
    return render_template("read_csv.html", inches_cm=inches_cm, pounds_kg=pounds_kg)


# Work №4
@bp.route("/space/")
def people_in_space():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url).json()
    return render_template("space.html", response=response)
