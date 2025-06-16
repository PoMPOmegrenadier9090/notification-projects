import config as c
import google_calendar_API
from LINE_API import broadcast

def main():
    account='me'
    event_list = google_calendar_API.main(account)
    text = f"""
おはようございます！ 
本日の予定は... \n
{"".join(f"{event.keys()}: {event.values()}" for event in event_list)}
    """

    print(text)

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