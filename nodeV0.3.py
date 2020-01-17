import os
import os.path
from os import path

import getpass
import hashlib as hlib
import datetime as date
import re

whoami = getpass.getuser()
nodeDIR = "/home/" + whoami + "/node"

def startup():
    print("Kubicle Systems\nBlockchain E-Voting\nV0.3\n")
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
        vote()
    elif select == "3":
        config()
    else:
        options()

def network():
    pass
def vote():
    pass
def config():
    pass
    

startup()
