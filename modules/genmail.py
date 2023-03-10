def generate_mail(rainfall, month, day, temp, sphum, relhum):
    mail_content = f"""\
            <html>

            <head>
                <div style="font-weight: 1000; color: white;"><u>Rainfall Prediction Result</u></div>
            </head>
            
            <body style="background-color: black;">
                <br> <img src="https://i.imgur.com/PiZMOCp.png" width="36%" height="56%"
                    style="vertical-align:middle; align-items: center;">
                <p style="color: green;">
                    <b>
                        Hello, this is an automated message from the Rainfall Prediction Page!
                    </b>
                </p>
                <p>
                <div style="color: white">
                    According to the entered data: <br>
                </div>
                <div style="color: goldenrod; font-weight: 520;">
                    The Date is: {month}, {day}. <br>
                    The Temperature is: {temp} degrees Celsius. <br>
                    The Specific Humidity is: {sphum} g/kg. <br>
                    The Relative Humidity is: {relhum} %. <br>
                </div>
                </p>
                <p style="color: red; font-weight: 750;">
                    The Predicted Rainfall is: {rainfall:.2f} mm.
                </p>
                <p style="color: white;">
                    (Feel free to leave us feedback on our
                    <a href="mailto:kg3479@srmist.edu.in,
                                pd5619@srmist.edu.in?
                                &cc=
                                &bcc=
                                &subject=Feedback for Rainfall Prediction Page
                                &body=Add whatever suggestions or message you would like to send here" 
                                target="_blank">
                        Mail
                    </a> or our
                    <a href="https://github.com/PalakDwivedi02/Rainfall-Prediction-using-ML" target="_blank"> Github Page</a>!)
                </p>
                <p>
                <div style="color: limegreen;">
                    Thank you for using our service!
                </div>
                <div style="color: white; font-weight: 750;"> <br>
                    <div style="color:white;">Regards,</div>
                    <a href="https://www.linkedin.com/in/kinshuk-goel/" target="_blank" style="color: rgb(13, 13, 191);">Kinshuk</a> 
                    and 
                    <a href="https://www.linkedin.com/in/palak-dwivedi-017437247/" target="_blank" style="color: rgb(13, 13, 191);">Palak</a>
                    <br> 
                    <div style="color:red">Neural Archmages</div>
                </div>
                </p>
            </body>
            
            </html>
        """  # .format(month, day, temp, sphum, relhum, rainfall)
    return mail_content
