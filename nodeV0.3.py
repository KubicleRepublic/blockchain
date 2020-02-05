import os
from os import path

import getpass
import hashlib as hlib
import datetime as date

#from module import class
from json_file import KubicleJson

#Loads the blockchain
#This will be turned into a function
#That scans for json_file.py and m.json

import pprint
import json
from pathlib import Path
import requests

from flask import jsonify

class Node:

    nodes = [
        "127.0.0.1:8080",
        "127.0.0.1:8081"
    ]

    home = str(Path.home())

    def __init__(self, nodeName="node"):
        self.whoami = getpass.getuser() #it's not being used, try to delete it later
        self.nodeDIR = self.home + "/" + nodeName + "/"
        self.kubicleJson = KubicleJson(file_path=self.nodeDIR)
        self.File = self.kubicleJson.load()        

    def startup(self):
        print("Kubicle Systems\nBlockchain E-Voting\nV0.3\n\nLanguage:")
        print("Python 3\nJSON\n")
        if path.exists(self.nodeDIR):
            self.options()
                
        else:
            print("Directory: Not Found\n")
            print("Would you like to create node directory?\n")
            answer = self.yesno()
            if answer == "yes":
                os.mkdir(self.nodeDIR)
            elif answer == "no":
                exit(1)
                
    def yesno(self):
        answer = input("[Y/n]")
        if answer == "Yes" or "Y" or "y" or "yes":
            answer = "yes"
            return answer
        elif answer == "No" or "N" or "n" or "no":
            answer = "no"
            return answer
        else:
            print("Please answer yes or no.\n")
            self.yesno()

    def options(self):
        print("Directory: Found\n")
        print("Please select on of the options below:\n")
        print("1) Check node status\n")
        print("2) Vote\n")
        print("3) Config file")

        select = str(input())
        if select == "1":
            pass
        elif select == "2":
            self.vote()
        elif select == "3":
            self.config()
        else:
            self.options()

    is_receiveing = False
        
    def save_data(self, data):
        self.kubicleJson.write(data)

    def vote(self):
        print("What is your Voter-ID?\n")
        userIn = str(input())
        u = userIn

        #The VIDDB.txt is a simle file that has list of Voter-IDs that it checks.
        #This is the place holder for a stronger database or E-Identity
        #CURRENTLY BROKEN
        #if you type "111" you can vote, 111 not a valid VID
        
	    #DB = open("/home/" + self.whoami + "/Desktop/" + "VIDDB.txt", "r+").read().splitlines()
        #print(DB)
        """
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
                    
            
            #Example VID. This cannot be clear text.
        """
        chain = self.File["chain"]
        
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
            
        ssize = len(self.File["chain"])
        

        #Here the File.json attributes are assigned
        if chain[0]['VIDh'] == '' and chain[0]['ts'] == "" and chain[0]['vote'] == "":
            block = chain[0]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote
            
            self.File["chain"] = chain
            self.kubicleJson.write(self.File)

            #broadcast the data to other nodes
            self.send_broadcast(block)
        else:
            #index = (len(chain)) + 1
            block = chain[ssize-1]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote
            chain.append(block)
    
            self.File["chain"] = chain
            self.kubicleJson.write(self.File)
            self.send_broadcast(block)

    def config():
        #This can access the conn.conf file
        #may read all accessible IPs
        pass

    def send_broadcast(self, data):
        #sends data to other nodes
        for node in self.nodes:
            print("sending to other nodes")
            print(data)
            url = "http://{}/broadcast".format(node)        
            
            #The line belows check if the node sending is not the same receiveing
            #data['is_receiveing'] = True

            #Content type must be included in the header
            header = {"content-type": "application/json"}

            #Performs a POST on the specified url to get the service ticket
            response = requests.post(url,data=json.dumps(data), headers=header, verify=False)

            print(response.json)
            print("---------")
        return "Broadcasted successfully"
