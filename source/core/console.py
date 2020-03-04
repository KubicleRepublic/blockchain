import os
from os import path

import hashlib as hlib
import datetime as date

from json_file import JsonEditor

import json
from pathlib import Path
import requests

from flask import jsonify

import imp
node = imp.load_source('node', 'node.py') #import files with dot
from node import Node


class Console:

    home = str(Path.home())

    def __init__(self, node):
        self.node = node
        self.nodeDIR = self.home + "/" + nodeName + "/"
        self.kubicleJson = JsonEditor(file_path=self.nodeDIR)
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


    def vote(self):
        print("What is your Voter-ID?\n")
        userIn = str(input())
        u = userIn

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
            self.node.save_data(self.File)

            #broadcast the data to other nodes
            self.node.send_broadcast(block)
        else:
            #index = (len(chain)) + 1
            block = chain[ssize-1]
            block['VIDh'] = VIDh
            block['ts'] = str(ts)
            block['vote'] = vote
            chain.append(block)
    
            self.File["chain"] = chain
            self.kubicleJson.write(self.File)
            self.node.send_broadcast(block)


if __name__ == "__main__":
    node = Node()
    console = Console(node)
    console.startup()


