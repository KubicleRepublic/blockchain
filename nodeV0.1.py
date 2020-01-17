import os
import os.path
from os import path
import getpass
import hashlib as hlib
import subprocess
import datetime as date
import re 
​
#For the ftp section
from ftplib import FTP
​
def startup():
    whoami = getpass.getuser()
    print("The current user is: " + whoami + "\n")
​
    #This will search for the /node directory
    nodeDIR = "/home/" + whoami + "/node"
    if path.exists(nodeDIR):
        print("Directory: Found\n\n")
        print("Would you like to check connectivity to the Network?\n")
        contin = input("Yes or No?\n")
        if contin == "Yes":
            print("Checking connecting to the internet: ")
            network()
            repository()
        elif contin == "No":
            repository()
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
​
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
        skip()
    else:
        print("Please type either Yes or No\n")
        main()
​
def network():
    hostname = "www.google.com"
    string = "ping -c 1 " + hostname
    #result=subprocess.getoutput(string)
    #print(result)
    response = os.system("ping -c 1 " + hostname)
    os.system("ping -c 1 " + hostname)
    
    if response == 0:
        print("Connected to internet\n")
    else:
        print("Network down\n")
    
    print("Would you like to test connectivty to other nodes?\n")
    nodeCON = input("Please enter Yes or No\n")
    
    if nodeCON == "Yes":
        OtherNode = input("What is the IP?: ")
        string = "ping -c 1 " + OtherNode
        # result=subprocess.getoutput(string)
        #print(result)
        os.system("ping -c 1 " + OtherNode)
        response = os.system("ping -c 1 " + OtherNode)
        if response == 0:
            print("Connected to node\n")
        else:
            print("Not Connected\n")
            
    elif nodeCON == "No":
        repository()
    else:
        print("Please print either yes or no\n")
​
def repository():
    print("Would you like to synchronize the Blockchain?\n")
    Sync = input("Please enter Yes or No\n")
    
    if Sync == "Yes":
        print("1)Checks number of nodes on the network")
        print("2)Calls for network to verify 51% (seperate script?)")
        print("3)Downloads directories/files")
        print("4)Will need to turn on auto-sync to download/upload votes.")
        print("This step will require a Merkle tree to encrypt blocks based")
        print("on an casted votes (from this node) and incoming votes that")
        print("are from other nodes.\n\n")
        
        all_nodes()
        
    elif Sync == "No":
        print("NOTE: If the blockchain is not synchronized, the node will")
        print("not be able to upload votes / blocks\n")
        print("Passive mode may be implemented to download votes but not")
        print("post any.\n\n")
        exit(1)
​
def all_nodes():
    N1 = "127.0.0.1"
    N2 = "10.0.0.98"
    N3 = "10.0.0.237"
    cn = 0
    
    #Node IPs can be read from a node_config.txt as long as its in this
    #Directory or the path is specified
   
    os.system("ping -c 1 " + N1)
    response = os.system("ping -c 1 " + N1)
    if response == 0:
        cn = cn + 1
        print("Responce from " + N1)
    else:
        print("No responce from " + N1)
        
    os.system("ping -c 1 " + N2)
    response = os.system("ping -c 1 " + N2)
    if response == 0:
        cn = cn + 1
        print("Responce from " + N2)
    else:
        print("No responce from " + N2)
​
    os.system("ping -c 1 " + N3)
    response = os.system("ping -c 1 " + N3)
    if response == 0:
        cn = cn + 1
        print("Responce from " + N3)
    else:
        print("No responce from " + N3)
​
    print("There is " + str(cn) + " node(s) on the network")
    skip()
​
def FTP():
    ftp = FTP('10.0.0.237')
    ftp.login()
​
def skip():
    print("\n\nAll Votes will be posted to /node\n")
    print("The Voter ID will be hashed and the timestamp &")
    print("\n vote will be in plain text")
    print("*Note if there is no /node directory on this device")
    print("\nthe program will not post anything")
    print("\nWould you like to vote?")
    print("\nYes/No")
    entryq = str(input())
​
    if entryq == "Yes":
        cast()
        
    elif entryq != "No":
        exit(1)
​
    else:
        print("Please enter Yes or No\n")
        skip()
        
#Casting vote / Error Check
def cast():
    global buffer
    global VID
    print("What is your Voter ID?\n")
    print("Example: XXXX\n")
    VIDe = str(input())
    con = "1234567890"
​
    if VIDe == "5555":
        print("PASS")
        VID = VIDe
        print("Who are you voting for?\n")
        print("a.)Darth Vader\nb.)Bugs Bunny\nc.)Steve\nd.)Lady Liberty")
        choice = str(input())
        buffer = choice
        vote()
        
    elif len(VIDe) > len(con):
        print("We cannot currently process your request.\n")
        print("Please try again, but this time not trying to overflow\n")
        print("the booth. Thanks.")
        exit(1)
        
    elif VIDe != "5555":
        print("VID not Recognized. Please Try again.")
        exit(1)
​
def vote():
    sha = hlib.sha256()
    ts = date.datetime.now()
    sha.update((str(VID).encode('utf-8')))
    votefile = sha.hexdigest() + str(ts) + buffer
    #print(votefile)
    #Here the file will be created in the node dir. While this may change
    #to have the program not store results in files, for the time being this
    #is the easiet way for me to build a POC.
    #If you don't like it, program it yourself.
    
    whoami = getpass.getuser()
    nodeDIR = "/home/" + whoami + "/node/"
    if path.exists(nodeDIR):
​
        current_node = []
        files = os.listdir(nodeDIR)
        files.sort()
        for filename in files:
            print(filename)
            filename = current_node.append(filename)
​
        if current_node != []:
            last_file = str(current_node[-1])
            print("\nThe last file was: " + last_file)
            num = int(re.search(r'\d+', last_file).group())
            num2 = num+1
            num3 = ('vote%s.vt' % num2)
            file = open(nodeDIR + "vote%s.vt" % num2,"w")
            file.write(votefile)
            file.close()
              
            if whoami == "n1":
                os.system("scp /home/n1/node/vote%s.vt n2@10.0.2.5:/home/n2/node/" % num2)
                os.system("scp /home/n1/node/vote%s.vt n3@10.0.2.15:/home/n3/node/" % num2)
​
            elif whoami == "n2":
                os.system("scp /home/n2/node/vote%s.vt n1@10.0.2.6:/home/n1/node/" % num2)
                os.system("scp /home/n2/node/vote%s.vt n3@10.0.2.15:/home/n3/node/" % num2)
            elif whoami == "n3":
                os.system("scp /home/n3/node/vote%s.vt n2@10.0.2.5:/home/n2/node/" % num2)
                os.system("scp /home/n3/node/vote%s.vt n1@10.0.2.6:/home/n1/node/" % num2)
            else:
                print("\nYou are currently not on an authorized node")
                print("\nContact the system administrator")
                exit(1)
            
        else:
            print("DIR is empty")
            file = open(nodeDIR + "vote1.vt","w")
            file.write(votefile)
            file.close()
            
            if whoami == "n1":
                os.system("scp /home/n1/node/vote1.vt n2@10.0.2.5:/home/n2/node/")
                os.system("scp /home/n1/node/vote1.vt n3@10.0.2.15:/home/n3/node/")
​
            elif whoami == "n2":
                os.system("scp /home/n2/node/vote1.vt n1@10.0.2.6:/home/n1/node/")
                os.system("scp /home/n2/node/vote1.vt n3@10.0.2.15:/home/n3/node/")
            elif whoami == "n3":
                os.system("scp /home/n3/node/vote1.vt n2@10.0.2.15:/home/n2/node/")
                os.system("scp /home/n3/node/vote1.vt n1@10.0.2.6:/home/n1/node/")
            else:
                print("\nYou are currently not on an authorized node")
                print("\nContact the system administrator")
                exit(1)
        
        #For now all the IPs will need to be hard coded
        #N1 Is always this computer
        N1 = "10.0.2.6"
        N2 = "10.0.2.5"
        N3 = "10.0.2.15"
  
    else:
        print("\nDirectory: Not Found\n")
        print("Please run the setup wizard")
        exit(1)
​
main()
