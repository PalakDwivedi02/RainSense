from predictor import *
from plot import train_and_plot
from flask import Flask, render_template, request, redirect, url_for
from email.message import EmailMessage
import smtplib
# from flask_mail import Mail, Message

train_and_plot()

app = Flask(__name__)

# mail = Mail(app)
# app.config["MAIL_DEFAULT_SENDER"] = "kg3479@srmist.edu.in"
# app.config["MAIL_PASSWORD"] = givepw()
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = "Kinshuk"
# mail = Mail(app)

rainfall = 0

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
    # name = request.form.get("name", "world")
    month = (request.form.get("month", "January"))
    m = int(MONTHS.index(month) + 1)
    day = request.form.get("day", 0)
    temp = request.form.get("temp", 0)
    sphum = request.form.get("sphum", 0)
    relhum = request.form.get("relhum", 0)
    global rainfall
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
    message = EmailMessage()
    message["from"] = givesender()
    message["to"] = email
    message["subject"] = "Rainfall Prediction Result"
    message.set_content(
        "Hello, this is an automated message from the Rainfall Prediction Page!\n\n\t\tThe Predicted Rainfall is: {0:.2f} mm.\n\nRegards,\nKin and Bells :3".format(rainfall))
    # msg = Message(
    #             'Hello',
    #             sender = givesender(),
    #             recipients = email
    #            )
    # msg.body = 'Hello Flask message sent from Flask-Mail, RnF: {}'.format(rainfall)
    # mail.send(msg)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(givesender(), givepw())
    s.send_message(message)
    s.quit()
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
