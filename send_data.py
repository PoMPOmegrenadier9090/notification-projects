import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from config import *

def send_data(data_list):

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = FROM_EMAIL_ADDRESS 
    to_email = TO_EMAIL_ADDRESS
    password = EMAIL_PASSWORD
    subject = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}新しい投稿"

    print("create body content")
    body = ""
    for data in data_list:
        body += f"スレッド: {data['year']}\n本文: {data['main_content']}\n{URL[data['year']]}\n"

    print(body)
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    for to in to_email:
        msg["To"] = to

        # Gmail serverに送信
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()

    return