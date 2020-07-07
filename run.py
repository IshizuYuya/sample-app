from flask import Flask, request
from app.utils import make_message


app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name')
    return make_message(name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
