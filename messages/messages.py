class Messages:
    def __init__(self):
        self.messages = []

    def get_one_message(self):
        last_message = self.messages[-1]
        last_message.set_seen()
        return last_message

    def get_all_message(self):
        return self.messages

    def get_all_unread_message(self):
        filtered = filter(lambda message: message.get_seen() == False, self.messages)
        return list(filtered)

    def add_message(self, message):
        self.messages.append(message)

    def delete_message(self):
        self.messages.pop()

    def output_json_all_messages(self):
        results = []
        for message in self.get_all_message():
            results.append(message.json_output())
        return results

    def output_json_all_unread_messages(self):
        results = []
        for message in self.get_all_unread_message():
            results.append(message.json_output())
        return results
