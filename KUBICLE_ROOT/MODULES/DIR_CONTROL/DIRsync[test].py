import os
import socket
import getpass
from pathlib import Path

#These will need to be hardcoded depending what IPs we have in the ESXI server
ACTIVE_NODES = ["10.0.0.1","10.0.0.2","10.0.0.3."]

#Finding the current IP of the system.
#You can try socket.gethostbyname(get.fqbn()) however, it gave me the loopback because my
#/etc/hosts has only the loopback, and that socket function only reads from there.

#https://it.toolbox.com/question/find-the-local-ip-using-python-043013
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
CURRENT_IP = s.getsockname()[0]
s.close()
print(CURRENT_IP)

#This function will simply compare the contents of each active IP and calculate the
#percent that is the same.
home = str(Path.home())
whoami = getpass.getuser()
nodeDIR = home + "/" + "/node"

def scanDIR():
        listing = os.listdir(nodeDIR)
        for file in listing:
                print("File is: " + file)
                #Will also read the file for its contents.
                #Each individual file can be stored in a variable to be further compared
                """
                some_sort_of_list[] = contensts of current file (maybe hash value, or actual contents)

                """
scanDIR()

#This psuedo function will pull the results from the other ACTIVE_NODES and compare them
#to the variable which will store the results
#We may be able to use Flask for this.
#@app.route("/scanDIR")
"""
count_sync = 0
count_desync = 0

for i in range(len(ACTIVE_NODES)):
        directory[i] = ACTIVE_NODES[i]

        if directory[i] == nodeDIR:
                count_sync + 1
        elif directory[i] != nodeDIR:
                some_function_that_finds differences()
                count_desync + 1
        else:
                print("Node[i] is offline")

if (count_sync // count_desync) > 51%:
        print("Network Syncronized")
elif (count_sync // count_desync < 51%:
        print("Network is desyncronized.")
else:
        print("Something is terribly broken with the logic if youre reading this.")

"""

"""

def DIRupdate(sync_node, desync_node):
        #This will update the node in question that is not the same as the 51% or more of the network
        goodNode = sync_node.readlines()
        badNode = desync_node.readlines()

        #Two ways to do this
        #1)Delete entry on node and replace it with good copy from goodNode

        #2)Compare the two strings are update the missing / added parts from the goodNode to the
        #bad node.

        for x in len(goodNode[0]):
                if badNode[x] != goodNode[x]:
                        badNode[VIDh[x]] = goodNode[VIDh[x]]
                elif badNode[x] == goodNode[x]:
                        pass
                elif badNode - If area does not exist:
                        create area copied from goodNode[x]
                else:
                        Print("Somethings wrong")

"""

"""
import hashlib
sha = hlib.sha256()

def MerkleTree():
        f = open("/path/to/file/m.json")
        #convert m.json file to obj?
        #May very well already be onj

        for v in len(m.json):
                vote{v} = str(m.json[v])
                #This simple looks for first pair.
                if vote{v} and vote{v + 1} // 2 == %2:
                        sha.update((str(vote{v}).encode('utf-8')) + str(vote{v + 1}).encode('utf-8'))
                        Merklehash{v} = sha.hexdigest()

                        #This creates block if there are 2 merkle hashes
                        if Merklehash{v} and Merklehash{v+1} // 2 == %2:
                                sha.update((str(Merklehash{v}).encode('utf-8')) + str(Merklehash{v + 1}).encode('utf-8'))
                                block{v} = sha.hexdigest()
                                b = open("/path/to/file/%s" % block{V})
                                b.write(block{v})

#The logic is not complete with the function above.

#Down below the Merkle tree will attempt to verify the blocks
blockfiles = []

def MerkleTreeVerify():
        path = "/path/to/blocks/"
        files = os.listdir(path):
        files.sort()
        for file in dir:
                file = blockfiles.append(file) #This will not have the hash, a dictionary will
                                               #Need to be used for that I think
                                               
        #This function checks first 4 vote's hash, and comapres them to block
        if ((m.json[0][1].hash) + (m.json([2][3]).hash)_.hash == blockfile[0].hash:
                #This compares the first 4 votes' combined hash to the calculated block
                #from the last function
                print("Good block\n")
        elif ((m.json[0][1].hash) + (m.json([2][3]).hash)_.hash != blockfile[0].hash:
                print("Bad block")
        else:
                print("Something is terribly wrong"                    

                
"""






