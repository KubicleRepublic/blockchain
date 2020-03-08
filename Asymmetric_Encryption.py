#This program will need python -m pip install cryptography
import cryptography
import os

#This part simple creates a file which will be the token in the current directory
#you are running the program from.
pwd = os.getcwd()
print("pwd: ", pwd)
f = open("%s/token.txt" % pwd, "w+")
f.close()

#Now we are going to generate a private key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

#This part creates the public key from the private key*
public_key = private_key.public_key()

#Storing the private key from the directory you're running the program form
from cryptography.hazmat.primitives import serialization
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
    )
with open('private_key.pem','wb') as pr:
    pr.write(pem)
    pr.close()

#Now for the private key
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
with open('public_key.pem','wb') as pu:
    pu.write(pem)
    pu.close()

#This is for encrypting files (signing & verification)
def encrypt_token():
    with open('token.txt','w+') as f:
        f.write("123456789") #this right here is the VID
        f.close()

    file = open('token.txt')
    file_contents = str.encode(file.readline())
    file.close()
    #print(file_contents)
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    encrypted = public_key.encrypt(
        file_contents,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
    file = open('token.txt', 'w+')
    file.write(str(encrypted))
    file.close()
    return encrypted

enc = encrypt_token()

def decrypt_token(encrypted):
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    clear_text = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
    print(str(clear_text))
    

encrypt_token()
decrypt_token(enc)







