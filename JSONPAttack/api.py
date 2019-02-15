from functools import wraps
from flask import request, current_app, jsonify, app, Flask

app = Flask(__name__)


def support_jsonp(f):
    """Wraps output to JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = jsonify(f(*args, **kwargs))
        callback = request.args.get('callback', False)
        if callback:
            print(str(result.data))
            content = callback + '(' + result.data + ')'
            return current_app.response_class(content,
                                              mimetype='application/json')
        else:
            return result
    return decorated_function


# then in your view
@app.route('/', methods=['GET'])
@support_jsonp
def test():
    return {'foo': 'bar', "moo" : "mar"}

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)