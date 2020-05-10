"""
Flask App
"""
from flask import Flask
APP = Flask(__name__)


@APP.route('/v1/health')
def health():
    """
    health end point
    :return:
    """
    return 'UP'


@APP.route('/')
def hello_world():
    """
    hello world function
    :return:
    """
    return 'Udacity Capstone Project - V2'


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=80, debug=True)
