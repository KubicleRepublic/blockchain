import hashlib
import datetime as date

###This is a Merkle Tree blockchain

def gen(data, counter):
    sha = hashlib.sha256()
    ts = date.datetime.now()

    sha.update((str(data) + str(ts)).encode('utf-8'))
    print("The hash is number is: " + str(counter))
    print("The hash is: " + sha.hexdigest())
    return sha.hexdigest()

counter = 0
transactions = []
for i in range(0,4):
    data = input("First message")
    transactions.append(gen(data, counter))
    counter = counter + 1

def stage01(hash1, hash2):
    sha = hashlib.sha256()
    
    sha.update((str(hash1) + str(hash2)).encode('utf-8'))
    print("\n")
    print("Stage 2 initiated\n")
    print("The hash is: " + sha.hexdigest())
    return sha.hexdigest()

def stage02(hash1, hash2):
    sha = hashlib.sha256()
    
    sha.update((str(hash1) + str(hash2)).encode('utf-8'))
    print("\n")
    print("Stage 2 initiated\n")
    print("The hash is: " + sha.hexdigest())
    return sha.hexdigest()

transactions2 = []
transactions2.append(stage01(str(transactions[0]), str(transactions[1])))
transactions2.append(stage02(str(transactions[2]), str(transactions[3])))

def stage03(hash1, hash2):
    sha = hashlib.sha256()
    
    sha.update((str(hash1) + str(hash2)).encode('utf-8'))
    print("\n")
    print("Stage 3 initiated\n")
    print("This is Block: 1")
    print("The hash is: " + sha.hexdigest())
    return sha.hexdigest()

transactions3 = []
transactions3.append(stage03(str(transactions2[0]),str(transactions2[1])))




    
