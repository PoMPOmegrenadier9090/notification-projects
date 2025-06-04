from scraping import scrape_html
from send_data import send_data
import functions_framework

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    data_list = scrape_html()
    if data_list:
        send_data(data_list)