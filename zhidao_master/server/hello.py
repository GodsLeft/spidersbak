#!/usr/bin/env python
# -*- coding:utf-8 -*-

import flask
from flask import Flask
from flask import Blueprint

app = Flask(__name__)

@app.route("/")
def hello():
    print "hello"
    return "hello world!"


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5405, debug=True)
