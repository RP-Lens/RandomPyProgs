from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl, socket

socket.getaddrinfo('127.0.0.1', 8080)
sender_email = "kurzeschwanz@gmail.com"
receiver_email = "kurzeschwanz@gmail.com"
password = "UCIChamps18"
subject = "Hello, World!"
body = "NI SHAGU NAZAD CYKA"

with open("index.html") as f:
    html = f.read()
    f.close()

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(html, 'html'))

print("sending loser")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("sent!")