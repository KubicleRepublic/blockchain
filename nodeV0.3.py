import os
import os.path
from os import path

import getpass
import hashlib as hlib
import datetime as date
import re

#from module import class
from json_file import kubicleJson
<<<<<<< HEAD

#Loads the blockchain
#This will be turned into a function
#That scans for json_file.py and m.json
=======
import pprint
import json
>>>>>>> 0ab3523bde715115d7454adc4e868a872ff86c2a
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
<<<<<<< HEAD
=======
    print("voting..")
    
    chain = File["chain"]
    
>>>>>>> 0ab3523bde715115d7454adc4e868a872ff86c2a
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
<<<<<<< HEAD
    File['VIDh'] = VIDh
    File['ts'] = ts
    File['vote'] = vote
    
=======
   
    # imp1 
    block = chain[0]
    block['VIDh'] = VIDh
    block['ts'] = str(ts)
    block['vote'] = vote
        
    # 1 item
    VID = "6666"
    sha = hlib.sha256()
    sha.update((str(VID).encode('utf-8')))
    VIDh = sha.hexdigest()
    
    print(type(chain[0]))
    #2
    newBlock = {
        "VIDh": VIDh,
        "ts": str(date.datetime.now()),
        "vote": 'b'
    }
    
    #list
    chain.append(newBlock)
        
    File["chain"] = chain
    
    kubicleJson.write(File)
>>>>>>> 0ab3523bde715115d7454adc4e868a872ff86c2a
    
 
def config():
    #This can access the conn.conf file
    #may read all accessible IPs
    pass
    

startup()