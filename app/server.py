# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


def run_server():
    app.run(host="127.0.0.1", port=8080)
