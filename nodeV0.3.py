import os
import os.path
from os import path

import getpass
import hashlib as hlib
import datetime as date
import re

#from module import class
from json_file import kubicleJson

#Loads the blockchain
#This will be turned into a function
#That scans for json_file.py and m.json

import pprint
import json
import requests #this module allows to send data through the nodes
from flask import Flask, jsonify, request #Flask allows to always keep listening for data
app = Flask(__name__)

File = kubicleJson.load()

whoami = getpass.getuser()
nodeDIR = "/home/" + whoami + "/node"

nodes = [
    "10.0.0.240:8080"
]

def startup():
    print("Kubicle Systems\nBlockchain E-Voting\nV0.3\n\nLanguage:")
    print("Python 3\nJSON\n")
    if path.exists(nodeDIR):
        options()
              
    else:
        print("Directory: Not Found\n")
        print("Would you like to create node directory?\n")
        answer = yesno()
        if answer == "yes":
            os.mkdir("/home/" + whoami + "/node")
        elif answer == "no":
            exit(1)
            
def yesno():
    answer = input("[Y/n]")
    if answer == "Yes" or "Y" or "y" or "yes":
        answer = "yes"
        return answer
    elif answer == "No" or "N" or "n" or "no":
        answer = "no"
        return answer
    else:
        print("Please answer yes or no.\n")
        yesno()

def options():
    print("Directory: Found\n")
    print("Please select on of the options below:\n")
    print("1) Check node status\n")
    print("2) Vote\n")
    print("3) Config file")

    select = str(input())
    if select == "1":
        network()
    elif select == "2":
        vote(File)
    elif select == "3":
        config()
    else:
        options()

is_receiveing = False

@app.route("/broadcast", methods = ['POST', 'GET'])
def broadcast():
    #gets the data that was sent
    data = request.get_json()

    #in case receives multiple messages
    is_receiveing = data.get('is_receiveing', False)
    if not is_receiveing:
        print("receiveing: {}".format(is_receiveing))
        save_data(data)
    else:
        print("Wait a minute")
        
    return "Received broadcast!!"
    
def save_data(data):
    kubicleJson.write(data)

@app.route("/network", methods = ['POST'])
def network():
    #receive data from HTTP request
    data = request.get_json()

    #sends data to other nodes
    for node in nodes:
        print("sending to other nodes")
        url = "http://{}/broadcast".format(node)        
        
        #The line belows check if the node sending is not the same receiveing
        #data['is_receiveing'] = True

        requests.post(url, json=data)
    return "Broadcasted successfully"

def vote(File):
    print("What is your Voter-ID?\n")
    userIn = str(input())
    u = userIn

    #The VIDDB.txt is a simle file that has list of Voter-IDs that it checks.
    #This is the place holder for a stronger database or E-Identity
    #CURRENTLY BROKEN
    #if you type "111" you can vote, 111 not a valid VID
    DB = open("/home/" + whoami + "/Desktop/" + "VIDDB.txt", "r+").read().splitlines()
    print(DB)

    for x in range (0, len(DB)):
        if DB[x].strip('\n') == u:
            print("User is Registered")
            pass
        elif DB[x].strip('\n') != u:
            if DB[-1] == x:
                print("User Not Registered.\n")
                exit(1)
            else:
                pass
        else:
            print("Input unrecognized. Please Try again.\n")
            
    
    chain = File["chain"]
    #Example VID. This cannot be clear text.
    VID = u
    sha = hlib.sha256()
    sha.update((str(VID).encode('utf-8')))
    VIDh = sha.hexdigest()

    #This is the timestamp
    ts = date.datetime.now()

    #This is the vote
    print("Who are you voting for?")
    print("a.)Darth Vader\nb.)Bugs Bunny\nc.)Steve\nd.)Lady Liberty\n")
    vote = input()
    
    if vote == "a" or vote == "b" or vote == "c" or vote == "d":
        pass
    else:
        Print("Not a valid answer\n")
        
    ssize = len(File["chain"])
    

    #Here the File.json attributes are assigned
    if chain[0]['VIDh'] == "" and chain[0]['ts'] == "" and chain[0]['vote'] == "":
        block = chain[0]
        block['VIDh'] = VIDh
        block['ts'] = str(ts)
        block['vote'] = vote
        
        File["chain"] = chain
        kubicleJson.write(File)
    else:
        #index = (len(chain)) + 1
        block = chain[ssize-1]
        block['VIDh'] = VIDh
        block['ts'] = str(ts)
        block['vote'] = vote
        chain.append(block)
 
        File["chain"] = chain
        kubicleJson.write(File)
        

def config():
    #This can access the conn.conf file
    #may read all accessible IPs
    pass
    

#startup()

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)