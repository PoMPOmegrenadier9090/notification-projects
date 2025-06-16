import requests
import config as c

def broadcast(messages):
    url = c.BROADCAST_URL

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {c.CHANNEL_ACCESS_TOKEN}',
    }

    data = {
        "messages":messages
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print(f"Successfully sent POST request to {url}")
        print(f"Status Code: {response.status_code}")
        print("Response Body:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending GET request to {url}: {e}")
        print(response.reason)

if __name__ == "__main__":
    broadcast([
            {
                "type":"textV2",
                "text":" Hello, world",
                "substitution": {
                    "sparkle": {
                        "type": "emoji",
                        "productId": "5ac2213e040ab15980c9b447",
                        "emojiId": "085"
                    }
                }
            }
        ])