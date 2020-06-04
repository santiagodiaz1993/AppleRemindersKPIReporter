from __future__ import print_function
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os.path
import json
from apiclient import errors
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

DISCOVERY_DOC = "https://docs.googleapis.com/$discovery/rest?version=v1"
SCOPES = [
    "https://www.googleapis.com/auth/drive.activity.readonly",
    "https://www.googleapis.com/auth/documents",
    "https://mail.google.com/",
]


class GoogleAPISession:
    def __init__(self, document_id, creds_path=None):
        self.document_id = document_id
        self.service = None
        self.google_authentication(creds_path)

    def google_authentication(self, creds_path):
        """
        Authenticate user's credentials so they can access their email or
        google docs
        """
        if creds_path is None:
            creds_path = "./credentials/docs_credentials.json"
        creds = None
        if os.path.exists("./credentials/docs_token.pickle"):
            with open("./credentials/docs_token.pickle", "rb") as token:
                creds = pickle.load(token)
        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES
            )
            creds = flow.run_local_server(port=0)
            with open("./credentials/docs_token.pickle", "wb") as token:
                pickle.dump(creds, token)
        self.service = build("docs", "v1", credentials=creds)

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message["to"] = to
        message["from"] = sender
        message["subject"] = subject
        return {
            "raw": base64.urlsafe_b64encode(
                message.as_string().encode()
            ).decode()
        }

    def create_message_with_attachment(
        self, sender, to, subject, message_text, file_dir, filename
    ):
        message = MIMEMultipart()
        message["to"] = to
        message["from"] = sender
        message["subject"] = subject

        msg = MIMEText(message_text)
        message.attach(msg)

        for file in filename:

            path = os.path.join(file_dir, file)
            content_type, encoding = mimetypes.guess_type(path)

            if content_type is None or encoding is not None:
                content_type = "application/octet-stream"
            main_type, sub_type = content_type.split("/", 1)
            if main_type == "text":
                fp = open(path, "rb")
                msg = MIMEText(fp.read(), _subtype=sub_type)
                fp.close()
            elif main_type == "image":
                fp = open(path, "rb")
                msg = MIMEImage(fp.read(), _subtype=sub_type)
                fp.close()
            elif main_type == "audio":
                fp = open(path, "rb")
                msg = MIMEAudio(fp.read(), _subtype=sub_type)
                fp.close()
            else:
                fp = open(path, "rb")
                msg = MIMEBase(main_type, sub_type)
                msg.set_payload(fp.read())
                fp.close()

            msg.add_header("Content-Disposition", "attachment", filename=file)
            message.attach(msg)

        return {
            "raw": base64.urlsafe_b64encode(
                message.as_string().encode()
            ).decode()
        }

    def send_message(self, service, user_id, message):
        try:
            message = (
                service.users()
                .messages()
                .send(userId=user_id, body=message)
                .execute()
            )
            print("Message Id: %s" % message["id"])
            return message
        except errors.HttpError as error:
            print("An error occurred: %s" % error)

    def get_reminders_from_document(self):
        result = (
            self.service.documents().get(documentId=self.document_id).execute()
        )
        document = json.loads(json.dumps(result))
        reminders = []
        for reminder in document["body"]["content"]:
            if reminder.get("paragraph"):
                reminders.append(
                    reminder["paragraph"]["elements"][0]["textRun"]["content"]
                )
        reminders = [reminder.split("$$") for reminder in reminders]
        reminders = [reminder[:-1] for reminder in reminders]
        return reminders
