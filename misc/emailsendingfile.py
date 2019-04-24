import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def emailverification(email, auth, data):
    try:
        msg = MIMEMultipart()
        msg['From'] = 'shopanytime.sat@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'verification link'
        if data == "link":
            body = "Your Verification Link For Signup is "+auth
        elif data == "otp":
            body = "Your One Time Password is:"+auth
        msg.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Transport layer security : converts insecure connection to secure connection
        server.login(msg['From'], "jalebibai")
        text = msg.as_string()  # converts M+IMEMultipart msg to string as text should be string
        server.sendmail(msg['From'], msg['To'], text)
        #server.quit()
        return True
    except:
        return False

#emailverification("tajinderkumar0408@gmail.com", "linktest")
