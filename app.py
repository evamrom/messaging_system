from datetime import datetime
from time import strftime
from flask import Flask, jsonify, request
from users.current_user import current_user
from users.users import users

app = Flask(__name__)


@app.route('/register', methods=["POST"])
def register():
    """Register the user to system. If the user already exists it return me a message.
    The user need to have a unique username and password.
        """
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if users.get_user(username, password):
            return jsonify({"status": "user already exists"})
        else:
            users.add_user(username, password)
            return jsonify({"status": "succeed to register"})
    except:
        return jsonify({"status": "error"})


@app.route('/login', methods=["POST"])
def login():
    """Login to the system with username and password. If the user doest exists in the system or
    the password or username incorrect the system will alert and the user can try again.
    The system initialize a current user so from now it will be the user logged it.
        """
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        new_current_user = users.get_user(username, password)
        if new_current_user:
            current_user.set_current_user(new_current_user)
            curr = current_user.get_current_user()
            if not curr.get_logged_in():
                curr.set_login()
                return jsonify({"status": "successfully logged in"})
            else:
                return jsonify({"status": "user already logged in"})
        else:
            return jsonify({"status": "username or password not correct"})
    except:
        return jsonify({"status": "error"})


@app.route('/logout', methods=["GET"])
def logout():
    """Logout from the system. It means the current user return to be None
        """
    try:
        current_user.get_current_user().set_logout()
        current_user.set_current_user(None)
    except:
        return jsonify({"status": "error"})
    return jsonify({"status": "successfully logged out"})


@app.route('/write_message', methods=["POST"])
def write_message():
    try:
        curr = current_user.get_current_user()
        data = request.get_json()
        sender = curr.get_username()
        receiver = data.get("receiver")
        message = data.get("message")
        subject = data.get("subject")
        creation_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        if curr.get_username() == sender:
            receiver_user = users.get_receiver(receiver)
            if receiver_user:
                curr.write_message(sender, receiver, message, subject, creation_date, receiver_user)
            else:
                return jsonify({"status": "the receiver not registered yet"})
        else:
            return jsonify({"status": "you are not the sender in the message"})

        return jsonify({"status": "successfully written message"})
    except:
        return jsonify({"status": "error"})


@app.route('/get_all_messages', methods=["GET"])
def get_all_messages():
    """Get all messages from the user currently logged in
        """
    try:
        curr = current_user.get_current_user()
    except:
        return jsonify({"status": "error"})

    return jsonify(curr.get_messages().output_json_all_messages())


@app.route('/get_all_unread_messages', methods=["GET"])
def get_all_unread_messages():
    """Get all the unread messages from the user currently logged in
        """
    try:
        curr = current_user.get_current_user()
    except:
        return jsonify({"status": "register error"})

    return jsonify(curr.get_messages().output_json_all_unread_messages())


@app.route('/read_message', methods=["GET"])
def read_message():
    """Read the last message of the logged in user, no matter if its read or not.
        """
    try:
        curr = current_user.get_current_user()
        message = curr.get_messages().get_one_message()
    except:
        return jsonify({"status": "register error"})

    return jsonify(message.json_output())


@app.route('/delete_message', methods=["GET"])
def delete_message():
    """Delete the last message of the logged in user, no matter if its read or not.
        """
    try:
        curr = current_user.get_current_user()
        curr.get_messages().delete_message()
    except:
        return jsonify({"status": "delete message error"})
    return jsonify({"status": "message deleted successfully"})


if __name__ == '__main__':
    app.run(host="localhost", port='8080', debug="true")
    # app.run( port='8080', debug="true")
