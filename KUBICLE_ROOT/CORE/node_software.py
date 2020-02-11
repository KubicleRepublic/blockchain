import os

from os import path
from pathlib import Path

import hashlib as hlib
import datetime as date
import json
import requests

from flask import jsonify

#from module import class
from json_file import KubicleJson

#Loads the Blockchain
#This will be turned into a function
#That scans for the json_file.py and m.json

class Node:
    home = str(Path.home())
    
    def __init__(self, NodeName="node"):
        self.nodeDIR = self.home + "/" + nodeName + "/"
        self.kublicleJson = KubicleJson(file_path=self.nodeDIR)
        self.File = self.kubicleJson.load()

    def setup(self):
        print("E-Voting Systems\nV.04\n")
        if path.exists(self.nodeDIR):
            print("All set.\n")
            self.options()
        else:
            print(" Working directories are not found.\n")
            print("Would you like to create node directory?\n")

            answer = self.yesno()
            if answer == "yes":
                os.mkdir(self.nodeDIR)
            elif answer == "no":
                exit(1)
                
    #Simple function to get input from user
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
        print("Select one of the options:\n")
        print("1) Check node status\n2)Print config\n3)Vote\n")

        select = str(input())
        if select == "1":
            pass
        elif select == "2":
            #Function to read the IPs?
            #Maybe it can be to check
            #Function doesn't need to exist if no purpose
        elif select == "3":
            self.vote()
        else:
            print("Unrecognised input\n")

    def save_data(self, data):
        self.kubicleJson.write(data)

    def vote(self):
        #This function will need to get votes from web server.
        #No need to control through this APP
        #For testing purposes it can be implemented.

        """Psuedo Function for checking if the VID already voted"""
        """
        data = "12345a" - data_from_web_server
        #data can encapsulate the VID and vote

        
        #You might be comparing the hash, so spliting the vid and vote then
        #hashing the vid to compare it to exisiting hashes would be the best
        #way to go
        
        for x in range(len(m.json)): - Basically number of votes
            if data[0][1][2][3][4] == m.json["VID"][x]:
                print("Duplicate vote\n")
                #drop request, listen to other requests.
            else:
                #continue with request
        """
        #If above is good, take the VID, Timestamp and vote and upload it
        #To the local m.json file

        VID = "test"
        vote = "a"

        chain = self.File["chain"]
        sha = hlib.sha256()
        sha.update((str(VID).encode('utf-8')))
        #This is the VID hash
        VIDh = sha.hexdigest()

        #This is the timestamp
        ts = date.datetime.now()

        #Here the File.json attributes are assigned.
        #This if statement is checking if it is the first vote
        if chain[0]['VIDh'] == '' and chain[0]['ts'] == '' and chain[0]['vote'] == '':
            block = chain[0]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote

            self.File["chain"] = chain
            self.kubicleJson.write(self.File)

            #broadcast the data to other nodes
            self.send_broadcast(block)

        #This statement is assuming that it is not the first vote
        #so it increments form the 
        else:
            block = chain[ssize-1]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote
            chain.append(block)
    
            self.File["chain"] = chain
            self.kubicleJson.write(self.File)
            self.send_broadcast(block)

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
        
        



        
