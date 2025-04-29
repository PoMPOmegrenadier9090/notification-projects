from scraping import scrape_html
from send_data import send_data

def main():
    data = scrape_html("")
    if data:
        send_data(data)
    else:
        print("No data to send")

if __name__ == "__main__":
    main()
