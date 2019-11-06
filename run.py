from flask import Flask, request
from app.utils import make_message


app = Flask(__name__)


@app.route('/hello')
def hello():
    """sample api"""
    print('START /hello')
    name = request.args.get('name')
    print('END /hello')
    return make_message(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
