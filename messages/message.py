class Message:
    def __init__(self, sender, receiver, message, subject, creation_date):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.subject = subject
        self.creation_date = creation_date
        self.seen = False

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

    def json_output(self):
        result = {
            "sender": self.sender,
            "receiver": self.receiver,
            "message": self.message,
            "subject": self.subject,
            "creation_date": self.creation_date,
            "seen": str(self.seen)
        }
        return result
