from users.user import User

class Users:
    """Users class provides a singleton which contains all the users registered to the system as an User object.
    Each user contains username, password, and messages object which contains all the messages the user received.
        """
    def __init__(self):
        self.users = []

    def get_user(self, username, password):
        for other_user in self.users:
            if other_user.username == username:
                if other_user.password == password:
                    return other_user

    # def check_if_contains(self, username, password):
    #     for other_user in self.users:
    #         if other_user.username == username:
    #             if other_user.password == password:
    #                 return True
    #     return False

    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    # def check_if_contains_receiver(self, receiver_username):
    #     for other_user in self.users:
    #         other_username = other_user.username
    #         if other_username == receiver_username:
    #             return True

    def get_receiver(self, receiver_username):
        for other_user in self.users:
            other_username = other_user.username
            if other_username == receiver_username:
                return other_user


users = Users()
