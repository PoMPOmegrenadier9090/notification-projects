import datetime
import pytz

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_credential(account):
  if os.path.exists(f"token_{account}.json"):
    creds = Credentials.from_authorized_user_file(f"token_{account}.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(f"token_{account}.json", "w") as token:
      token.write(creds.to_json())
  return creds

def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  account = ''

  creds = get_credential(account)
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.


  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    jst = pytz.timezone('Asia/Tokyo')
    jst_time = datetime.datetime.now(jst)
    timeMax = jst_time + datetime.timedelta(days=1)
    timeMax = timeMax.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
    timeMin = jst_time.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
    print('jst_time:', jst_time)
    print('timeMin:', timeMin)
    
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=timeMin,
            timeMax=timeMax,
            singleEvents=True,
            timeZone="Asia/Tokyo",
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

    print()
  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()

