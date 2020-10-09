from messages.message import Message
from messages.messages import Messages


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False
        self.messages = Messages()

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_logged_in(self):
        return self.logged_in

    def get_messages(self):
        return self.messages

    def set_login(self):
        self.logged_in = True

    def set_logout(self):
        self.logged_in = False

    def write_message(self, sender, receiver, message, subject, creation_date, receiver_user):
        message = Message(sender, receiver, message, subject, creation_date)
        receiver_user.get_messages().add_message(message)
