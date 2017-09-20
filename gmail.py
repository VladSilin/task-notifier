import base64
import httplib2

from email.mime.text import MIMEText

from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools

CLIENT_SECRET_PATH = './config/client_secret_679339727312-7qs8ghor6dn6j0p0eqai6i86q3g9teqh.apps.googleusercontent.com.json'
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.compose'
STORAGE = Storage('./config/gmail.storage')

flow = flow_from_clientsecrets(CLIENT_SECRET_PATH, scope=OAUTH_SCOPE)
http = httplib2.Http()

credentials = STORAGE.get()
if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, STORAGE, http=http)

http = credentials.authorize(http)

gmail_service = build('gmail', 'v1', http=http)


def send_email(sender, recipient, subject, text):
    message = MIMEText(text)
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject
    body = {'raw': base64.b64encode(message.as_string())}

    try:
        message = (gmail_service.users().messages().send(userId='me', body=body).execute())
        print('The message ID is %s' % message['id'])
        print(message)
    except Exception as error:
        print 'An error has occurred: %s' % error
