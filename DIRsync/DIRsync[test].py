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




