
from Message import Message
from User import User


class Users:
    def __init__(self):
        self.users = []

    def get_user(self, username, password):
        for other_user in self.users:
            if other_user.username == username:
                if other_user.password == password:
                    return other_user

    def check_if_contains(self, username, password):
        for other_user in self.users:
            if other_user.username == username:
                if other_user.password == password:
                    return True
        return False

    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def check_if_contains_reciever(self, reciever_username):
        for other_user in self.users:
            other_username = other_user.username
            if other_username == reciever_username:
                return True

    def get_reciever(self, reciever_username):
        for other_user in self.users:
            other_username = other_user.username
            if other_username == reciever_username:
                return other_user

    def print_users(self):
        for user in self.users:
            user.print_user()

    def write_message(self, sender, receiver, message, subject, creation_date):
        message = Message(sender, receiver, message, subject, creation_date)
        if users.check_if_contains(receiver):
            receiver = users.get_reciever(receiver)
            receiver.get_messages.add_message(message)


users = Users()

