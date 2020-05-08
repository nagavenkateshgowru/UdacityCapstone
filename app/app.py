"""
Flask App
"""
from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    """
    hello world function
    :return:
    """
    return 'Udacity Capstone Project'


if __name__ == "__main__":
    APP.run()
