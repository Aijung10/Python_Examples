from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "tharundintakurthi@gmail.com"
password = input("Enter the password of gmail:")
from_email = username
to_email = "tharundintakurthi@gmail.com , dintakurthitharun@gmail.com"
cc = "tharundintakurthi@gmail.com , dintakurthitharun@gmail.com"

email_conn = smtplib.SMTP(host, port)
email_conn.starttls()
email_conn.login(username, password)


the_msg = MIMEMultipart("alternative")
the_msg["Subject"] = "Hello html"
the_msg["From"] = from_email
the_msg["To"] = to_email
the_msg["Cc"] = cc

plain_text = "Just hello this is plain text"
html_text = """
<html>
    <head></head>
        <body>
            <p>Hi i am html</p>
            <h1>i am in h1 tag</h1>
        </body>
</html>
"""

part1 = MIMEText(plain_text, "plain")
part2 = MIMEText(html_text, "html")

the_msg.attach(part1)
the_msg.attach(part2)

email_conn.sendmail(the_msg["From"], the_msg["To"].split(",") + the_msg["Cc"].split(","), the_msg)
email_conn.quit()

print("Email sent successfully")
