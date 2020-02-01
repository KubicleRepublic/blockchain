import os
import os.path
from os import path

import getpass
import hashlib as hlib
import datetime as date
import re

#from module import class
from json_file import KubicleJson

#Loads the blockchain
#This will be turned into a function
#That scans for json_file.py and m.json

import pprint
import json

class Node:

    nodes = [
        "10.0.0.11:8080"
    ]
    #nodes = ["10.0.1.{}".format(x) for x in range(11,30)

    def __init__(self):
        kubicleJson = KubicleJson()
        self.File = kubicleJson.load()
        self.whoami = getpass.getuser()
        self.nodeDIR = "/home/" + self.whoami + "/node"
        

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
                os.mkdir("/home/" + self.whoami + "/node")
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
        kubicleJson.write(data)

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
                
        
        chain = self.File["chain"]
        #Example VID. This cannot be clear text.
	"""
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
        if chain[0]['VIDh'] == "" and chain[0]['ts'] == "" and chain[0]['vote'] == "":
            block = chain[0]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote
            
            File["chain"] = chain
            kubicleJson.write(File)

            #broadcast the data to other nodes
            send_broadcast(block)
        else:
            #index = (len(chain)) + 1
            block = chain[ssize-1]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote
            chain.append(block)
    
            self.File["chain"] = chain
            kubicleJson.write(self.File)
            

    def config():
        #This can access the conn.conf file
        #may read all accessible IPs
        pass

    def send_broadcast(data):
        #sends data to other nodes
        for node in nodes:
            print("sending to other nodes")
            url = "http://{}/broadcast".format(node)        
            
            #The line belows check if the node sending is not the same receiveing
            #data['is_receiveing'] = True

            requests.post(url, json=data)
        return "Broadcasted successfully"
