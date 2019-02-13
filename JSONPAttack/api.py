from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=['GET'])
def get():
    return jsonify({"blah" : "merp"})

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
