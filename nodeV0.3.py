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
File = kubicleJson.load()

whoami = getpass.getuser()
nodeDIR = "/home/" + whoami + "/node"

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

def network():
    pass

def vote(File):

    print("voting..")
    
    chain = File["chain"]
    
    #Example VID. This cannot be clear text.
    VID = "5555"
    sha = hlib.sha256()
    sha.update((str(VID).encode('utf-8')))
    VIDh = sha.hexdigest()

    #This is the timestamp
    ts = date.datetime.now()

    #This is the vote
    vote = 'a'

    #Here the File.json attributes are assigned
    block = chain[0]
    if block['VIDh'] == "" and block['ts'] == "" and block['vote'] == "":
        block['VIDh'] = VIDh
        block['ts'] = str(ts)
        block['vote'] = vote
        
        File["chain"] = chain
        kubicleJson.write(File)
    else:
        index = (len(chain)) + 1
        
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
    

startup()
