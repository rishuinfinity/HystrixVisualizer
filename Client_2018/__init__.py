from http import server
from flask import Flask, jsonify, request
import sys
import os
import requests
import json

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

port = 2018

def getResponseFromServerManager():
    uri = "http://localhost:5000/get-running-status"
    Jresponse=requests.get(uri)
    data = json.loads(Jresponse.text)
    return data['data']

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

@app.route('/', methods=['GET','POST'])
def mainPage():
    data = "This is a client"
    return jsonify({'data': data})


@app.route('/get-response')
def getStatus():
    data = getResponseFromServerManager()
    return data

if __name__ == '__main__':
    app.run(port=port)