def generate_mail(rainfall, month, day, temp, sphum, relhum):
    mail_content = f"""\
            <html>
                <head>
                    <div style="font-weight: 1000"><u>Rainfall Prediction Result</u></div>
                </head>

                <body>
                    <p style="color: green;">
                        <b>
                            Hello, this is an automated message from the Rainfall Prediction Page!
                        </b>
                    </p>
                    <p>
                    <div style="color: black">
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
                    <p style="color: black;">
                        (Feel free to leave us feedback on our <a
                            href="https://github.com/PalakDwivedi02/Rainfall-Prediction-using-ML">Github Page</a>!)
                    </p>
                    <p>
                    <div style="color: green;">
                        Thank you for using our service!
                        <div style="color: royalblue; font-weight: 750;"> <br>
                            Regards,<br>
                            <a href="https://www.linkedin.com/in/kinshuk-goel/">Kin</a> and <a
                                href="https://www.linkedin.com/in/palak-dwivedi-017437247/">Bells</a> :3
                        </div>
                        </p>
                </body>
            </html>
        """#.format(month, day, temp, sphum, relhum, rainfall)
    return mail_content