import json
from flask import Flask, jsonify, request, Response
from Users import users

app = Flask(__name__)


class CurrentUser:
    def __init__(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user

    def set_current_user(self, new_current_user):
        self.current_user = new_current_user


current_user = CurrentUser()


@app.route('/register', methods=["POST"])
def register():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if users.check_if_contains(username, password):
            return jsonify({"ststus": "user already exists"})
        else:
            users.add_user(username, password)
            return jsonify({"status": "succeed to register"})
    except:
        return jsonify({"status": "error"})


@app.route('/login', methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if users.check_if_contains(username, password):
            new_current_user = users.get_user(username, password)
            current_user.set_current_user(new_current_user)
            # logged_in = current_user.get_logged_in()
            # if not logged_in:
            # current_user.set_login()
            return jsonify({"status": "successfully logged in"})
            # else:
            #     return jsonify({"status": "user already logged in"})
        else:
            return jsonify({"status": "username or password not correct"})
    except:
        return jsonify({"status": "error"})


@app.route('/logout', methods=["GET"])
def logout():
    # try:
    # current_user.get_current_user().set_logout()
    # except:
    #     jsonify({"status": "error"})
    jsonify({"status": "successfully logged out"})


@app.route('/write_message', methods=["POST"])
def write_message():
    try:
        data = request.get_json()
        sender = data.get("sender")
        receiver = data.get("receiver")
        message = data.get("message")
        subject = data.get("subject")
        creation_date = "0-0-0"
        if users.check_if_contains_reciever(receiver):
            receiver_user = users.get_reciever(receiver)
            current_user.get_current_user().write_message(sender, receiver, message, subject, creation_date,
                                                          receiver_user)
        else:
            return jsonify({"status": "the receiver not registered yet"})
    except:
        return jsonify({"status": "error"})

    return jsonify({"status": "successfully written message"})


@app.route('/get_all_messages', methods=["GET"])
def get_all_messages():
    try:
        all_messages = current_user.get_current_user().get_messages().get_all_message()
    except:
        return jsonify({"status": "error"})

    results = []
    for message in all_messages:
        results.append(message.json_output())

    return jsonify(results)


@app.route('/get_all_unread_message', methods=["GET"])
def get_all_unread_messages():
    try:
        all_unread_messages = current_user.get_current_user().get_messages().get_all_unread_message()
    except:
        return jsonify({"status": "register error"})

    results = []
    for message in all_unread_messages:
        results.append(message.json_output())
    return Response(json.dumps(results))


@app.route('/read_message', methods=["GET"])
def read_message():
    try:
        message = current_user.get_current_user().get_messages().get_one_message()
    except:
        return jsonify({"status": "register error"})

    return jsonify(message.json_output())


@app.route('/delete_message', methods=["GET"])
def delete_message():
    try:
        current_user.current_user().get_messages().delete_message()
    except:
        return jsonify({"status": "delete message error"})
    return jsonify({"status": "delete message error"})


if __name__ == '__main__':
    app.run(host="localhost", port='8080', debug="true")
