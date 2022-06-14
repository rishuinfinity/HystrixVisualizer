from http import server
from flask import Flask, jsonify, request
import sys
import os
import requests
import json

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

port = 8081

def giveResponseToServers():
    return "This server is running on port "+ str(port)


app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

@app.route('/', methods=['GET','POST'])
def mainPage():
    data = "This is a server"
    return jsonify({'data': data})


@app.route('/get-response')
def getStatus():
    data = giveResponseToServers()
    return jsonify({'data' : data})

if __name__ == '__main__':
    app.run(port=port)