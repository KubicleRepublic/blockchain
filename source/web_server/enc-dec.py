#This script will create a sample file, encrypt it with the private key from
#the asymmetric_Encryption.py program and verify it using the public key

#[!] THIS SCRIPT DOES NOT CREATE THE PUB/PRIV KEYS [!]

import base64
import cryptography.exceptions
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import dsa, rsa



UPLOAD_DIR = '/home/e/Desktop/SAIT/Capstone/blockchain/source/web_server/UPLOADS'

def samplef():
    f = open(UPLOAD_DIR + "/" + "sample.txt", "w+")
    f.write("123123123")
    f.close()

def access_priv():
    with open("/home/e/Desktop/SAIT/Capstone/blockchain/private_key.pem", "rb") as pr:
        private_key = load_pem_private_key(pr.read(), password=None, backend=default_backend())
        print(private_key)
        return private_key
        
def access_pub():
    with open("/home/e/Desktop/SAIT/Capstone/blockchain/public_key.pem", "rb") as pu:
        public_key = load_pem_public_key(pu.read(), default_backend())
        print(public_key)
        return public_key

def encrypt_sample(pub):
    #[1] Opens the file
    file = open("sample.txt")
    
    file_contents = str.encode(file.readline())
    file.close()

    #[2] Encrypts the contents with the public key    
    public_key = pub
    encrypted = public_key.encrypt(
        file_contents,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )

    #[3] Sign the file
    private_key = priv
    signature = base64.b64encode(
        private_key.sign(
            payload,
            padding.PSS(
                mgf = padding.MGF1(hashes.SHA256()),
                salt_length = padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
            )
        )

    #[4] You are writing a new file which is the signature
    with open("sample.sig", "wb") as file:
        file.write(signature)
        file.close()
        
    
    #[5] Rewrites the files with the encrypted content 
    file = open("sample.txt", "w+")
    file.write(str(encrypted))
    file.close()
    return encrypted

def verification(priv):
    private_key = priv
    file = open("sample.txt")
    file_contents = str.encode(file.readline())


#[1]
samplef()
#[2]
priv = access_priv()
pub = access_pub()
#[3]
encrypt_sample(pub)
enc = encrypt_sample()

#[4]
verification(pub)

