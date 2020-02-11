#This function will be used to read the results sent from the web server
#And upload the VID and vote to the node

import os
from pathlib import Path

home = str(Path.home())
print(home)

def ballot():
    f = open(home + "/Desktop/ballotbox.txt", "r")
    data = f.readlines()
    print(data)

ballot()

