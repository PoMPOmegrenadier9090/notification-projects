import datetime
import pytz

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import config as c


def get_credential(account):
  creds = None
  if os.path.exists(f"secrets/token_{account}.json"):
    creds = Credentials.from_authorized_user_file(f"secrets/token_{account}.json", c.SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if (creds is None) or (not creds.valid):
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "secrets/credentials.json", c.SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(f"secrets/token_{account}.json", "w") as token:
      token.write(creds.to_json())
  return creds

def main(account):
  """Shows basic usage of the Google Calendar API.
  """
  creds = None

  creds = get_credential(account)
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.

  try:
    service = build("calendar", "v3", credentials=creds)

    # set the time length
    jst = pytz.timezone('Asia/Tokyo')
    jst_time = datetime.datetime.now(jst)
    timeMax = jst_time.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
    timeMin = jst_time.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
    print('jst_time:', jst_time)
    print('timeMin:', timeMin)
    
    print("fetching today's events")
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
      return None

    # Prints the start and name of the next 10 events
    else:
      return events

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main('me')

