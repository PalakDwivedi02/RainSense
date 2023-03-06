from predictor import *
from flask_mail import Mail, Message
import smtplib
from modules.mailing import *

rainfall = 57.0


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def send_mail():
    email = "pd5619@srmist.edu.in"
    msg = EmailMessage()
    msg["from"] = givesender()
    msg["to"] = email
    msg["subject"] = "Rainfall Prediction Result"
    msg.set_content(
        color.BLUE+color.BOLD
        + "Hello, this is an automated message from the Rainfall Prediction Page!\n\n\t\tThe Predicted Rainfall is: {0:.4f} mm.\n\nRegards,\nKin and Bells.".format(rainfall)
        + color.END+color.END)
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
    s.send_message(msg)
    s.quit()
    return "Mail Sent!"


send_mail()


def pr():
    return color.BLUE+color.BOLD+"Hello, this is an automated message from the Rainfall Prediction Page!\n\n\t\tThe Predicted Rainfall is: {0:.2f} mm.\n\nRegards,\nKin and Bells.".format(rainfall)+color.END+color.END


print(pr())
