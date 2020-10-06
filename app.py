from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == "GET":
        return jsonify("response", "Hello Back")
    if request.method == "POST":
        req_json = request.json
        name = req_json['name']
        return jsonify("response", "Be my friend "+ name)


if __name__ == '__app__':
    app.run(debug= True, port = 8080)
