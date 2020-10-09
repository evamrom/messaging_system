class CurrentUser:
    def __init__(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user

    def set_current_user(self, new_current_user):
        self.current_user = new_current_user

# singleton
current_user = CurrentUser()