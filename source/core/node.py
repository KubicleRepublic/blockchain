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

    def __init__(self, nodename="node"):
        self.nodeDIR = self.home + "/" + nodeName + "/"
        self.kubicleJson = KubicleJson(file_path=self.nodeDIR)
        self.File = self.kubicleJson.load()        
        

    def save_data(self, data):
        self.kubicleJson.write(data)

    
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
            
            #TODO: The line belows check if the node sending is not the same receiveing
            #data['is_receiveing'] = True

            header = {"content-type": "application/json"} #Content type must be included in the header

            response = requests.post(url,data=json.dumps(data), headers=header, verify=False)

            print(response.json)
            print("---------")
        return "Broadcasted successfully"
