import os
import os.path
from os import path
import getpass
import hashlib as hlib
import subprocess


def startup():
    whoami = getpass.getuser()
    print("The current user is: " + whoami + "\n")

    #This will search for the /node directory
    nodeDIR = "/home/" + whoami + "/node"
    if path.exists(nodeDIR):
        print("Directory: Found\n\n")
        print("Would you like to check connectivity to the Network?\n")
        contin = input("Yes or No?\n")
        if contin == "Yes":
            print("Checking connecting to the internet: ")
            network()
            
        elif contin == "No":
            exit(1)
        else:
            print("Please enter Yes or No\n")
            startup()
    else:
        print("Directory: Not Found")
        print("Would you like to create the directory?\n")
        creationDIR = input("Yes or No?\n")
        
        if creationDIR == "Yes":
            os.mkdir("/home/" + whoami + "/node")
            
        elif creationDIR == "No":
            exit(1)
            
        else:
            print("Please type either Yes or No")
            startup()

def main():
    dirpath = os.getcwd()
    print("Current Directory is: " + dirpath)
    foldername = os.path.basename(dirpath)
    print("Directory name is: " + foldername)
    print()
    print("Directory Needs to be in /home/user/node\n")
    print("Would you like to initialize setup?\n")
    start = input("Yes or No\n")
    if start == "Yes":
        startup()
    elif start == "No":
        print("Program either starts here or quits.\n")
    else:
        print("Please type either Yes or No\n")
        main()

def network():
    hostname = "www.google.com"
    string = "ping -c 1 " + hostname
    result=subprocess.getoutput(string)
    print(result)
    
    response = os.system("ping -c 1 " + hostname)
    
    if response == 0:
        print("Connected to internet\n")
    else:
        print("Network down\n")

    print("Would you like to test connectivty to other nodes?\n")
    nodeCON = input("Please enter Yes or No\n")
    
    if nodeCON == "Yes":
        OtherNode = input("What is the IP?: ")
        string = "ping -c 1 " + OtherNode
        result=subprocess.getoutput(string)
        print(result)
        response = os.system("ping -c 1 " + OtherNode)
        if response == 0:
            print("Connected to node\n")
        else:
            print("Not Connected\n")
main()
    

