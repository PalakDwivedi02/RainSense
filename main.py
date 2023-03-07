from predictor import *
from plot import train_and_plot
from flask import Flask, render_template, request, redirect, url_for
from modules.mailing import *

app = Flask(__name__)

rainfall = 0
month = 'January'
day = 1
temp = 0
sphum = 0
relhum = 0

MENU = [
    "Google Search",
    "Sorting Algos",
    "Rainfall Prediction"
]

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


@app.route('/')
def index():
    return render_template('index.html', menu=MENU, months=MONTHS)


@app.route('/output', methods=['GET', 'POST'])
def webpage():
    global rainfall
    global month
    global day
    global temp
    global sphum
    global relhum
    month = request.form.get("month", "January")
    m = int(MONTHS.index(month) + 1)
    day = request.form.get("day", 1)
    temp = request.form.get("temp", 0)
    sphum = request.form.get("sphum", 0)
    relhum = request.form.get("relhum", 0)
    rainfall = predict_rainfall(int(m), int(
        day), float(sphum), float(relhum), float(temp))
    return render_template('output.html',
                           month=month,
                           day=day,
                           temp=temp,
                           sphum=sphum,
                           relhum=relhum,
                           rainfall=rainfall)


@app.route('/mail')
def ren_mail():
    if request.method == 'POST':
        return redirect(url_for('send_mail'))
    return render_template('mail.html')


@app.route('/Sent', methods=['GET', 'POST'])
def send_mail():
    email = request.form.get("remail", "")
    rnf_mail_alt(email, rainfall, month, day, temp, sphum, relhum)
    return "Mail Sent!"


@app.route("/input")
def greet():
    return render_template("input.html")


@app.route('/Kin')
@app.route('/Kinshuk')
def hello_Kin():
    return 'Hello, Kinshuk!'


@app.route('/Palak')
def hello_Palak():
    var = 3
    return 'Hello Palak :{}'.format(var)


if __name__ == '__main__':
    app.run()
