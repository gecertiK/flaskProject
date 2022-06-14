from flask import Flask
from faker import Faker

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/requirements")
def requirements():
    file = "requirements.txt"  # requirements выдает в строку, а я хочу чтоб был в столбик, найти реение?
    with open(file, "r") as data:
        text = data.read()
    return f"<p>{text}<p>"


@app.route("/email")
def gen_mail():
    fake = Faker()
    name = fake.first_name()
    email = fake.email()
    return f"{name} {email}"
