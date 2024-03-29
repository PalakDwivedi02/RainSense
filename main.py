from predictor import *
from plotting import *
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

PLOTS = [
    "Yearly Rainfall",
    "Monthly Rainfall",
    "Temperature vs Rainfall",
    "Relative Humidity vs Rainfall",
]

@app.route('/plotform')
def plotform():
    return render_template('plotform.html', plots=PLOTS)

@app.route('/')
def index():
    return render_template('index.html', menu=MENU, months=MONTHS)

@app.route('/form')
def pred_form():
    return render_template('form.html', months=MONTHS)

@app.route('/plottedcurve', methods = ['GET', 'POST'])
def showplot():
    plot_type = request.form.get("plottype", "Yearly Rainfall")
    if plot_type == "Yearly Rainfall":
        return render_template('yrplot.html')
    elif plot_type == "Monthly Rainfall":
        return render_template('moplot.html')
    elif plot_type == "Temperature vs Rainfall":
        return render_template('tmplot.html')
    elif plot_type == "Relative Humidity vs Rainfall":
        return render_template('huplot.html')
    return render_template('plotform.html', plots=PLOTS)


@app.route('/prediction', methods=['GET', 'POST'])
def form_submit():
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
    return render_template('prediction.html',
                           month=month,
                           day=day,
                           temp=temp,
                           sphum=sphum,
                           relhum=relhum,
                           rainfall=rainfall)


@app.route('/enter-mail')
def ren_mail():
    if request.method == 'POST':
        return redirect(url_for('send_mail'))
    return render_template('askemail.html')


@app.route('/mail-Sent', methods=['GET', 'POST'])
def send_mail():
    email = request.form.get('remail', "")
    rnf_mail_alt(email, rainfall, month, day, temp, sphum, relhum)
    return render_template('mailsent.html')


@app.route('/mail-content')
def mail_content():
    return render_template('mailcontent.html', rainfall=str(f'{rainfall:.2f}'), month=month, day=day, temp=temp, sphum=sphum, relhum=relhum)


@app.route('/input')
def greet():
    return render_template('input.html')


@app.route('/Kin')
@app.route('/Kinshuk')
def hello_Kin():
    return 'Hello, Kinshuk!'


@app.route('/Palak')
def hello_Palak():
    var = 3
    return 'Hello Palak :{}'.format(var)


if __name__ == '__main__':
    app.run(debug=True)
    train_and_plot()