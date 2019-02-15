from functools import wraps
from flask import request, current_app, jsonify, app, Flask

app = Flask(__name__)

'''
Example of JSONP-able server from Flask's webpage
http://flask.pocoo.org/snippets/79/
'''
def jsonp(f):
    """Wraps output to JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = jsonify(f(*args, **kwargs))
        callback = request.args.get('callback', False)
        if callback:
            content = callback + '(' + result.data + ')'
            return current_app.response_class(content,
                                              mimetype='application/json')
        else:
            return result
    return decorated_function

@app.route('/', methods=['GET'])
@jsonp
def test():
    return {'foo': 'bar', "moo" : "mar"}

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)
