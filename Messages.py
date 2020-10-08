class Messages:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


    def print_all_messages(self):
        for message in self.messages:
            message.print_message()

    def print_unread_messages(self):
        for message in self.messages:
            if message.read_or_unread():
                message.print_message()

    def delete_message(self):
        self.messages.pop()

    def get_one_message(self):
        last_message = self.messages[-1]
        last_message.set_seen()
        return last_message

    def get_all_message(self):
        return self.messages

    def get_all_unread_message(self):
        filtered = filter(lambda message: message.get_seen() == False, self.messages)
        return list(filtered)
