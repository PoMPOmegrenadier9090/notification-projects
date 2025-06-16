import config as c
import google_calendar_API
from LINE_API import broadcast

def main():
    account='me'
    event_list = google_calendar_API.main(account)
    event_info = ""
    if event_list:
        for idx,event in enumerate(event_list):
            try:
                event_info += f"{idx+1}. {event['summary']} ({event['start']['dateTime'][11:16]})\n"
            except:
                event_info += f"{idx+1}. {event['summary']} \n"

    text = f"""{{sparkle}}おはようございます！ 
本日の予定は... \n
{event_info}"""

    messages = [
            {
                "type":"textV2",
                "text": text,
                "substitution": {
                    "sparkle": {
                        "type": "emoji",
                        "productId": "5ac2213e040ab15980c9b447",
                        "emojiId": "085"
                    }
                }
            }
        ]
    broadcast(messages)

if __name__ == "__main__":
    main()