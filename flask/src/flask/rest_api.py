__author__ = 'ycchang'

from flask import Flask
from flask import request
from flask import render_template
from flask import abort
from flask import redirect
import json


app = Flask(__name__)


@app.route('/')
def index():
    try:
<<<<<<< HEAD
        return '{"Flask":"hello2"}'
=======
        return '{"Flask":"hello world! VERSION:11 8/16/2015 1:35 PM"}'
>>>>>>> 75a7f74289f19d1340ba27d7e0e7bd086774b09b
    except Exception as e:
        return "Error"


@app.route('/cpu_high', methods=['GET'])
def users():
    if request.method == 'GET':
        a = 1
        b = 2
        for i in xrange(0, 1000000000):
            c = a
            a = b
            b = c
            
        return '{"Flask":"cpu_high"}'
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)