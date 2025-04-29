#import functions_framework
import requests
from bs4 import BeautifulSoup
from config import *
from datetime import datetime, timedelta

#@functions_framework.http
def scrape_html(request):
    print("start")
    url = URL["2022"]  # スクレイピング対象のURL
    print(url)
    payload = {
        "thread_view_password": PASSWORD,  # ←ここに入力したいパスワード
        "thread_number": "30",
        "thread_view_password_submit": "認証"
    }
    print("request")
    session = requests.Session()
    session.get(url)
    response = session.post(url, data=payload)
    print("response")
    if response.status_code != 200:
        print("failed")
        print(f"Failed to fetch: {response.status_code}", 500)
        return None

    print("success")
    soup = BeautifulSoup(response.text, "html.parser")
    date = soup.find_all("font")[1].get_text()
    splitted_date = date.split(" ")
    
    date_str =splitted_date[0].split("(")[0].strip()
    time_str = splitted_date[1]
    dt_str = f"{date_str} {time_str}"  # → '2025/04/29 01:20:54'
    dt = datetime.strptime(dt_str, "%Y/%m/%d %H:%M:%S")

    now = datetime.now()

    time_diff = now - dt

    print(time_diff)
    if timedelta(hours=0) <= time_diff <= timedelta(hours=15):
        print("6時間以内なので次の処理を実行します")
        paragraphs = soup.find_all("p", class_="line-text")[1].getText()
        paragraphs = paragraphs.split("...もっと見る")[0]
        content = f"{paragraphs}{"......"}" 
        return {
            "date": dt_str,
            "main_content": content
        }

    else:
        print("対象外です")
        return None