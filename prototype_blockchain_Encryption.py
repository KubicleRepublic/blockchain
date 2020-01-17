import hashlib as hlib
import datetime as date
from cryptography.fernet import Fernet

buffer = ""
VID = ""
entext = ""

#Casting vote / Error Check
def cast():
    global buffer
    global VID
    print("What is your Voter ID?\n")
    print("Example: XXXX\n")
    VIDe = str(input())
    con = "1234567890"

    if VIDe == "5555":
        print("PASS")
        VID = VIDe
        print("Who are you voting for?\n")
        print("a.)Darth Vader\nb.)Bugs Bunny\nc.)Steve\nd.)Lady Liberty")
        choice = str(input())
        buffer = choice
        
    elif len(VIDe) > len(con):
        print("We cannot currently process your request.\n")
        print("Please try again, but this time not trying to overflow\n")
        print("the booth. Thanks.")
        exit(1)
        
    elif VIDe != "5555":
        print("VID not Recognized. Please Try again.")
        exit(1)

def encrypt(choice, key):
    global entext
    keyy = key
    print(choice)
    print(VID)
    sha = hlib.sha256()
    ts = str(date.datetime.now())
    sha.update((str(VID)).encode('utf-8'))
    text = str((sha.hexdigest() + ts + buffer)).encode()
    
    f = Fernet(keyy)
    en = f.encrypt(text)
    entext = en
    print(en)
    
    return en

def decrypt(text, key):
    f = Fernet(key)
    dec = f.decrypt(text)
    print(dec)

    


#Encryption Section
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
        
def load_key():
    """
    loads key from current directory
    """
    return open("key.key", "rb").read()

write_key()
key = load_key()
   
cast()
write_key()
load_key()
encrypt(buffer, key)

decrypt(entext, key)


