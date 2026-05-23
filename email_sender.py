import smtplib

sender = "your_email@gmail.com"
password = "your_password"

receiver = "friend@gmail.com"

message = "Hello from automation"

server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    sender,
    password
)

server.sendmail(
    sender,
    receiver,
    message
)

print("Email sent")