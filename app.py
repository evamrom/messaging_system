from flask import Flask, request, jsonify

app = Flask(__name__)
#  secret key add

import sqlite3

conn = sqlite3.connect('mysqlite.db')
c = conn.cursor()

#create table
c.execute('''CREATE TABLE IF NOT EXISTS students
             (rollno real, name text, class real)''')

c.execute('''INSERT INTO students
             VALUES(1, 'Alex', 8)''')

#commit the changes to db
conn.commit()
#close the connection
conn.close()


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == "GET":
        data_name = c.lastrowid
        print(data_name)
        return jsonify("response", "Hello Back database" + str(data_name))
    if request.method == "POST":
        req_json = request.json
        name = req_json['name']
        return jsonify("response", "Be my friend "+ name)

@app.route('/write_message', methods = ['GET', 'POST'])
def writeMessage():
    if request.method == "GET":
        return jsonify("response", "Hello Back")
    if request.method == "POST":
        req_json = request.json
        name = req_json['name']
        return jsonify("response", "Be my friend "+ name)





if __name__ == '__main__':
    app.run(host = "localhost",port= '8080',debug= True)
