import hashlib as hashu
import datetime as date
import shutil
from distutils.dir_util import copy_tree
import os
import glob
import re


active_node1 = []
active_node2 = []
active_node3 = []

#Add block
def new_block():
    active_node1.clear()
    print("Starting...")
    database_sample()
    
    active_node1.sort()
    last_element = str(active_node1[-1])
    
    print("Last element:" + last_element)        
    num = int(re.search(r'\d+', last_element).group())
    num2 = num + 1
    num3 = ('block%s.txt' % num2)
    print(num2)
    print(num)
    
    f = open("/home/elysee/Desktop/COM1/block%s.txt" % num)
    previous_hash = f.read()
    print(previous_hash)
    
    data = input("Next Block# Please input data: ")
    sha = hashu.sha256()
    ts = date.datetime.now()

    sha.update((str(data) + str(ts) + str(previous_hash)).encode('utf-8'))
    print((str(data) + str(ts) + str(previous_hash)).encode('utf-8'))
    print(sha.hexdigest())
    
    file = open("/home/elysee/Desktop/COM1/block%s.txt" % num2, "w")
    file.write(sha.hexdigest())
    file.close() 
    file = open("/home/elysee/Desktop/COM2/block%s.txt" % num2, "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM3/block%s.txt" % num2, "w")
    file.write(sha.hexdigest())
    file.close()
    start()

#Delete folder contents
def delete_all_contents():
    files = glob.glob("/home/elysee/Desktop/COM1/*")
    for f in files:
        os.remove(f)
    files = glob.glob("/home/elysee/Desktop/COM2/*")
    for f in files:
        os.remove(f)
    files = glob.glob("/home/elysee/Desktop/COM3/*")
    for f in files:
        os.remove(f)
    start()

#Will store the databases
def database_sample():
   
    path = "/home/elysee/Desktop/COM1"
    files = os.listdir(path)
    files.sort()
    print("\nCOM1")
    for filename in files:
        print(filename)
        filename = active_node1.append(filename)
        
    path = "/home/elysee/Desktop/COM2"
    files = os.listdir(path)
    files.sort
    print("\nCOM2")    
    for filename in files:
        print(filename)
        filename = active_node2.append(filename)
        
    path = "/home/elysee/Desktop/COM3"
    files = os.listdir(path)
    print("\nCOM3")    
    for filename in files:
        print(filename)
        filename = active_node3.append(filename)
        
#Will store the databases
def database_sample():
    counter = True
    if counter == False:
        blank_nodes()
    counter = False

    path = "/home/elysee/Desktop/COM1"
    files = os.listdir(path)
    print("\nCOM1")
    for filename in files:
        print(filename)
        filename = active_node1.append(filename)
        
    path = "/home/elysee/Desktop/COM2"
    files = os.listdir(path)
    print("\nCOM2")    
    for filename in files:
        print(filename)
        filename = active_node2.append(filename)
        
    path = "/home/elysee/Desktop/COM3"
    files = os.listdir(path)
    print("\nCOM3")    
    for filename in files:
        print(filename)
        filename = active_node3.append(filename)
        


#Will compare the databases
def database_compare():

    if len(active_node1) == 0 and len(active_node2) == 0 and len(active_node3) == 0:
        print("\nDirectories are empty.")
        start()
    
    elif active_node1 == active_node2 and active_node3 == active_node2:
        print("\n***All directories are synchronized***\n")
        start()
        
    elif active_node1 != active_node2 and active_node2 == active_node3:
        print("\nNode 1 different: 66.6% Network same")
        print(active_node1)
        rec()
        
        
    elif active_node2 != active_node1 and active_node1 == active_node3:
        print("\nNode 2 different: 66.6% Network same")
        print(active_node2)
        print("F")
        rec()

        
    elif active_node3 != active_node1 and active_node1 == active_node2:
        print("\nNode 3 different: 66.6% Network same")
        print(active_node3)
        rec()
        
    else:
        print("\nNetwork desyncronized")


def rec():
        print("Would you like to do a node recovery?\n[Yes/No]")
        result = input()
        if result == 'Yes' or 'Y' or 'y':

            node_recovery()

            active_node1.clear()
            active_node2.clear()
            active_node3.clear()
            
            database_sample()
            database_compare()
            start()
        else:
            exit(1)


def node_recovery():
    
    if active_node1 != active_node2 and active_node2 == active_node3:
        
        files = glob.glob("/home/elysee/Desktop/COM1/*")
        for f in files:
            os.remove(f)
        fromDir = "/home/elysee/Desktop/COM2"
        toDir = "/home/elysee/Desktop/COM1"
        copy_tree(fromDir, toDir)
      
        
        
    elif active_node2 != active_node1 and active_node1 == active_node3:
        
        files = glob.glob("/home/elysee/Desktop/COM2/*")
        for f in files:
            os.remove(f)
        fromDir = "/home/elysee/Desktop/COM3"
        toDir = "/home/elysee/Desktop/COM2"
        copy_tree(fromDir, toDir)
     
        
        
    elif active_node3 != active_node1 and active_node1 == active_node2:
        
        files = glob.glob("/home/elysee/Desktop/COM3/*")
        for f in files:
            os.remove(f)
        fromDir = "/home/elysee/Desktop/COM2"
        toDir = "/home/elysee/Desktop/COM3"
        copy_tree(fromDir, toDir)
  
    else:
        print("Implement function to check blocks.\n")
      
#Parts Referenced from: https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2

#This is the first word that is turned into hash, with date.
def function_data():
    data = input("1# Please input data: ")
    sha = hashu.sha256()
    ts = date.datetime.now()
    
    sha.update((str(data) + str(ts)).encode('utf-8'))
    print((str(data) + str(ts)).encode('utf-8'))
    print(sha.hexdigest())

    #Here the file will be created. No encryption on contents.
    file = open("/home/elysee/Desktop/COM1/block1.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM2/block1.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM3/block1.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    return sha.hexdigest()

#second word is now hashed with date + hash of last block
def function_next(genesis_block):
    data = input("2# Please input data: ")
    sha = hashu.sha256()
    ts = date.datetime.now()
    
    sha.update((str(data) + str(ts) + str(genesis_block)).encode('utf-8'))            
    print((str(data) + (str(ts)) + str(genesis_block)).encode('utf-8'))
    print(sha.hexdigest())

    #Here the second file will be created. No Encryption on contents.
    file = open("/home/elysee/Desktop/COM1/block2.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM2/block2.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM3/block2.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    return sha.hexdigest()

#Third word is now hashed with date + hash of second block
def function_third(block_2):
    data = input("3# Please input data: ")
    sha = hashu.sha256()
    ts = date.datetime.now()

    sha.update((str(data) + str(ts) + str(block_2)).encode('utf-8'))
    print((str(data) + str(ts) + str(block_2)).encode('utf-8'))
    print(sha.hexdigest())

    #Here the third file will be created. No Encryption on contents.
    file = open("/home/elysee/Desktop/COM1/block3.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM2/block3.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    file = open("/home/elysee/Desktop/COM3/block3.txt", "w")
    file.write(sha.hexdigest())
    file.close()
    return sha.hexdigest()    

def start():
    print("Blockchain Secret Project\t Prototype v 1.2")
    print("Produced by Elysee Franchuk")
    print("\n")
    print("### Please have 'COM1' 'COM2' 'COM3' directories")
    print("### Set the paths in code to those directories on your local machines")
    print("\n")

    print("Select one of the options:\n")
    print("1) Hash 3 messages")
    print("2) Check Network")
    print("3) Delete Folder Contents")
    print("4) Add new block")
    print("5) Exit")

    resultA = input()
    if resultA == '1':
        print("Setting Environment. . .")
        genesis_block = function_data()
        block_2 = function_next(genesis_block)
        block_3 = function_third(block_2)
        start()


    elif resultA == '2':
        active_node1.clear()
        active_node2.clear()
        active_node3.clear()
        database_sample()
        database_compare()
        exit(1)
    elif resultA == '3':
        delete_all_contents()
    elif resultA == '4':
        active_node1.clear()
        active_node2.clear()
        active_node3.clear()
        new_block()
    elif resultA == '5':
        exit(1)
        
start()


#File Distribution v1.0
#Here it will copy the file to the rest of the folders.
#Things to consider:
#Search by file, if not found and => 51% from all dirs, downloads files(copies)
"""block_files = []
path = "/home/elysee/Desktop/COM1"

files = os.listdir(path)
for filename in files:
    print(filename)
    filename = block_files.append(filename)

fromDir = "/home/elysee/Desktop/COM1"
toDir  = "/home/elysee/Desktop/COM2"
toDir2  = "/home/elysee/Desktop/COM3"
copy_tree(fromDir, toDir)
copy_tree(fromDir, toDir2)
start()
"""



