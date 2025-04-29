from scraping import scrape_html
from send_data import send_data

def main():
    data_list = scrape_html("")
    if data_list:
        send_data(data_list)
    else:
        print("No data to send")

if __name__ == "__main__":
    main()
