from http import server
from flask import Flask, jsonify, request
import sys
import os
import requests
import json
import time
import _thread as thread
from requests.exceptions import Timeout

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

port = 5000
lastServer = 0
ALL_SERVERS_LIST=[[8080,1,1],[8081,1,1],[8082,1,1]] # [port, success, fails]
AVAILABLE_SERVERS_LIST = ALL_SERVERS_LIST
DOWN_SERVERS_LIST = []
ACTIVITY_THRESHOLD = 0.4
WAITING_THRESHOLD = 2 # in seconds
REPLENISH_TIME=10 # in seconds

def removeServer(server):
    AVAILABLE_SERVERS_LIST.remove(server)
    DOWN_SERVERS_LIST.append(server)
    thread.start_new_thread(replenishServer, (0,server))
        

def replenishServer(num, server):
    print("Sleeping for waiting time")
    time.sleep(REPLENISH_TIME)
    print("Woke up, now replenishing port "+str(server[0]))
    DOWN_SERVERS_LIST.remove(server)
    AVAILABLE_SERVERS_LIST.append(server)

def getResponseFromServer(server):
    uri = "http://localhost:"+str(server[0])+"/get-response"
    # try:
        # Jresponse=requests.get(uri, timeout = WAITING_THRESHOLD)
    # except Timeout:
    #     server[2] +=1
    #     if server[2]/server[1] >= ACTIVITY_THRESHOLD:
    #         removeServer(server)
    Jresponse=requests.get(uri, timeout = WAITING_THRESHOLD)
    data = json.loads(Jresponse.text)
    return data['data']

def getResponseFromServers():
    global lastServer
    for i in range(len(AVAILABLE_SERVERS_LIST)):
        idx = (i+lastServer+1) % len(AVAILABLE_SERVERS_LIST)
        server = AVAILABLE_SERVERS_LIST[idx]
        try:
            # create a process to retrieve data 
            data =  getResponseFromServer(server)
            lastServer = idx
            server[1]+=1
            return data
        except Exception as e:
            print(e)
            server[2]+=1
            if server[2]/server[1] >= ACTIVITY_THRESHOLD:
                removeServer(server)
    return "All servers down"


app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

@app.route('/', methods=['GET','POST'])
def mainPage():
    data = "This is a server manager"
    return jsonify({'data': data})

@app.route('/get-running-status')
def getStatus():
    data = getResponseFromServers()
    return jsonify({'data' : data})

@app.route('/panel')
def panel():
    # servers = {
    #     'all': ALL_SERVERS_LIST,
    #     'up': AVAILABLE_SERVERS_LIST,
    #     'down': DOWN_SERVERS_LIST
    # }
    text = ""
    text += "Server Status<br/>"
    text += "Ports Running " + str([s[0] for s in ALL_SERVERS_LIST]) + "<br/>"
    text += "Ports Down " + str([s[0] for s in DOWN_SERVERS_LIST]) + "<br/>"
    text += "Ports Detailed Status: "
    text += str(ALL_SERVERS_LIST)
    return text

if __name__ == '__main__':
    app.run(port=port)