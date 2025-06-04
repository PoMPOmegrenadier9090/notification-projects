import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from config import *

def send_data(data_list):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = FROM_EMAIL_ADDRESS 
    to_email = TO_EMAIL_ADDRESS
    password = EMAIL_PASSWORD
    now = datetime.now() + timedelta(hours=9)
    subject = f"{now.strftime('%Y-%m-%d %H:%M')}  掲示板通知メール"

    body = ""
    for data in data_list:
        body += f"スレッド: {data['year']}\n本文: {data['main_content']}\n{URL[data['year']]}\n\n------------------------------------\n"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = "undisclosed-recipients:;"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    # Gmail serverに送信
    server.sendmail(from_email, to_email, msg.as_string())
    print("sent")
    server.quit()
    return