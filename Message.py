import json

from flask import Response


class Message:
    def __init__(self, sender, receiver, message, subject, creation_date):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.subject = subject
        self.creation_date = creation_date
        self.seen = False

    #     check how to print
    def json_output(self):
        js = {
            "sender": self.get_sender(),
            "receiver": self.get_receiver(),
            "message": self.get_message(),
            "subject": self.get_subject(),
            "creation_date": self.get_creation_date(),
            "seen": str(self.get_seen())
        }
        return js


    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_message(self):
        return self.message

    def get_subject(self):
        return self.subject

    def get_creation_date(self):
        return self.creation_date

    def get_seen(self):
        return self.seen

    def set_seen(self):
        self.seen = True