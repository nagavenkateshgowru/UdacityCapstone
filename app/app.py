"""
Flask App
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    hello world function
    :return:
    """
    return 'Udacity Capstone Project'


if __name__ == "__main__":
    app.run()
