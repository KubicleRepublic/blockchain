#This script will create a sample file, encrypt it with the private key from
#the asymmetric_Encryption.py program and verify it using the public key

#[!] THIS SCRIPT DOES NOT CREATE THE PUB/PRIV KEYS [!]

import os
from os import path
SOURCE_DIRECTORY = os.path.dirname(os.path.dirname(__file__)) #absolut path until source dir


import base64
import cryptography.exceptions
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import dsa, rsa

UPLOAD_DIR = SOURCE_DIRECTORY + '/web_server/UPLOADS'
FILE_NAME_PATTERN = 'token_sample-{}.txt'
SIG_NAME_PATTERN =  'signature-{}.sig'

def samplef(saitId, force_mkdir=True):
    f_path = UPLOAD_DIR + "/" + FILE_NAME_PATTERN.format(str(saitId))
    print("f_path: ", f_path)
    if force_mkdir and not os.path.exists(os.path.dirname(f_path)):
        try:
            os.makedirs(os.path.dirname(f_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(f_path, "w+")
    f.write(str(saitId))
    f.close()


def access_priv():
    with open("../blockchain/private_key.pem", "rb") as pr:
        private_key = load_pem_private_key(pr.read(), password=None, backend=default_backend())
        print(private_key)
        return private_key
        
def access_pub():
    with open("../blockchain/public_key.pem", "rb") as pu:
        public_key = load_pem_public_key(pu.read(), default_backend())
        print(public_key)
        return public_key


def encrypt_sample(pub, saitId):
    public_key = pub
    #[1] Opens the file
    file = open(UPLOAD_DIR + '/' + FILE_NAME_PATTERN.format(saitId))
    
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
    file = open(UPLOAD_DIR + '/' + FILE_NAME_PATTERN.format(saitId), "w+")
    file.write(str(encrypted))
    file.close()
    return encrypted


def sign_sample(priv, saitId):
    private_key = priv
    file = open(UPLOAD_DIR + '/' + FILE_NAME_PATTERN.format(saitId), "rb")
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
    sig = open(UPLOAD_DIR + '/' + SIG_NAME_PATTERN.format(saitId), "wb")
    sig.write(signature)
    return signature

def merge_signed_and_encypted_sample(sign, saitId):
    encrypted_sample = UPLOAD_DIR + '/' + FILE_NAME_PATTERN.format(saitId)

    with open(encrypted_sample, "a") as f:
        f.write("\n")
        f.write(str(sign))


def verification(sign, enc, pub, priv, saitId):
    public_key = pub
    private_key = priv
    signature = sign
    encrypted = enc
    
    file = open(UPLOAD_DIR + '/' + SIG_NAME_PATTERN.format(saitId))
    sig_test = base64.b64decode(signature)
    file_contents = base64.b64decode(file.read())
    

    file2 = open(UPLOAD_DIR + '/' + FILE_NAME_PATTERN.format(saitId))
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


def verification2(sign, enc, pub, priv, saitId):
    public_key = pub
    private_key = priv
    signature = sign
    encrypted = enc
    
    # file = open(UPLOAD_DIR + '/' + SIG_NAME_PATTERN.format(saitId))
    # sig_test = base64.b64decode(signature)
    # file_contents = base64.b64decode(file.read())

    with open(UPLOAD_DIR + '/' + FILE_NAME_PATTERN.format(saitId)) as file:
        file_contents = file.readlines()
        print("file0: ", file_contents[0][:-1], "FIM")
        file_content = base64.b64decode(file_contents[0][:-1])

        file_contents2 = str.encode(file_contents[1])

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

sait_id = 789         
#[1]
samplef(sait_id)

# #[2]
priv = access_priv()
pub = access_pub()

# #[3]
enc = encrypt_sample(pub, sait_id)

# # #[4]
sign = sign_sample(priv, sait_id)
print("sign: ", sign)

#merge_signed_and_encypted_sample(sign, sait_id)

# # #[5]
verification(sign, enc, pub, priv, sait_id)

#[6] This is only if the signature is valid
#This may be imlemented into the web server to find out
#the contents of the token (VID)



