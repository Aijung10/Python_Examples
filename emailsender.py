import smtplib
host = "smtp.gmail.com"
port = 587
username = "tharundintakurthi@gmail.com"
password = input("Enter the password of gmail:")
from_email = username
to = "tharundintakurthi@gmail.com"

email_conn = smtplib.SMTP(host, port)
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to, "Hello I am from python!!!!")
email_conn.quit()
