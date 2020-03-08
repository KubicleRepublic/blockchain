#This script will create a sample file, encrypt it with the private key from
#the asymmetric_Encryption.py program and verify it using the public key

#[!] THIS SCRIPT DOES NOT CREATE THE PUB/PRIV KEYS [!]

import os
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
    public_key = pub
    #[1] Opens the file
    file = open(UPLOAD_DIR + '/' + "sample.txt")
    
    file_contents = str.encode(file.readline())
    file.close()

    #[2] Encrypts the contents with the public key    
    encrypted = public_key.encrypt(
        file_contents,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        
    #[3] Rewrites the files with the encrypted content 
    file = open(UPLOAD_DIR + '/' + "sample.txt", "w+")
    file.write(str(encrypted))
    file.close()
    return encrypted

def sign_sample(priv):
    private_key = priv
    file = open(UPLOAD_DIR + '/' + "sample.txt", "rb")
    file_contents = file.readline()

    signature = base64.b64encode(
        private_key.sign(
            file_contents,
            padding.PSS(
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length = padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    )
    #[?] Important note -- open file with wb operation so you can write it as bytes [?]
    sig = open(UPLOAD_DIR + '/' + "signature.sig", "wb")
    sig.write(signature)
    return signature


def verification(sign, enc, pub, priv):
    public_key = pub
    private_key = priv
    signature = sign
    encrypted = enc
    
    file = open(UPLOAD_DIR + '/' + "signature.sig")
    sig_test = base64.b64decode(signature)
    file_contents = base64.b64decode(file.read())
    

    file2 = open(UPLOAD_DIR + '/' + 'sample.txt')
    file_contents2 = str.encode(file2.read())

    print("debug: %s\n%s" % (signature, encrypted))

    #--------------------------------------------#
    try:
        public_key.verify(
            file_contents,
            file_contents2,
            padding.PSS(
                mgf = padding.MGF1(hashes.SHA256()),
                salt_length = padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        print("Signature Valid. You shall pass...")
        decrypt_sample(encrypted, private_key)
    except cryptography.exceptions.InvalidSignature as e:
        print("ERROR: Sample file && || Signature files failed verification.\n")

def decrypt_sample(enc, priv):
    encrypted = enc
    private_key = priv
    clear_text = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
    print(clear_text)
         
#[1]
samplef()

#[2]
priv = access_priv()
pub = access_pub()

#[3]
enc = encrypt_sample(pub)

#[4]
sign = sign_sample(priv)

#[5]
verification(sign, enc, pub, priv)

#[6] This is only if the signature is valid
#This may be imlemented into the web server to find out
#the contents of the token (VID)



