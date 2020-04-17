import os
from os import path

import getpass
import hashlib as hlib
import datetime as date

#from module import class
from jsonEditor import JsonEditor


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

    #home = str(Path.home())

    def __init__(self, nodeName="node"):
        self.kubicleJson = JsonEditor(file_add_folder=nodeName, file_name="m.json")
        self.kubicleJson.create_dir()
        self.File = self.kubicleJson.load()


    def config(self):
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


if __name__ == '__main__':        
    node = Node(nodeName="core/node8080")
    #print("File loaded: ", node.File)

    if "alert" not in node.File:
        print(node.File["chain"][0]["VIDh"])
