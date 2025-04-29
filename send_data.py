import smtplib
from email.mime.text import MIMEText
from config import *

def send_data(data):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    from_email = EMAIL_ADDRESS 
    to_email = EMAIL_ADDRESS
    password = EMAIL_PASSWORD

    subject = "新しい投稿"
    body = f"対象時刻: {data["date"]}\n\n本文: {data["main_content"]}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    # Gmail serverに送信
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

    return