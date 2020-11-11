from __future__ import print_function
import datetime
import pickle
import os.path
import requests
import pytz
import gi
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



# One time initialization of libnotify

gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Notifier")

# Create the notification object
summary = "Go to work!"
body = "Meeting at 3PM!"
notification = Notify.Notification.new(
    summary,
    body, # Optional
)

# Actually show on screen
#notification.show()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming event.')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    
    events = events_result.get('items', [])

    
    
    if not events:
        print('There is no upcoming event.')
    
    for event in events:
        
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        #print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        tz = pytz.timezone('Asia/Taipei')
        dt = datetime.datetime.now()
        loc_dt = tz.localize(dt).replace(microsecond=0)
        #print(loc_dt.isoformat())
        now_time=loc_dt.isoformat()
        if start[0:14] == loc_dt.isoformat()[0:14]:
            if int(now_time[14])*10+int(now_time[15])-(int(start[14])*10+int(start[15]))<=30:
                print("Please go to work!")
                print(start, event['summary'])

        else:
            print("There's no emergency.")

  

if __name__ == '__main__':
    main()



