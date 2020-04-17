import hashlib
import json
from jsonEditor import JsonEditor

import requests

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'votes': []
}


"""
open_votes[]:

Core feature of blockchain!

All open votes will be taken and added to a new block 
and then added to a blockchain whenever this block is mined

"""
#open_votes = [] #outstandinf transactions
owner = 'Luiz'

candidates = set()

NODES = [
    "8081",
    "8082"
]

class Blockchain:

    def __init__(self, nodeId):
        self.__peer_nodes = NODES
        self.blockchain = [genesis_block]
        self.open_votes = []
        self.nodeId = nodeId
        self.kubicleJson = JsonEditor()
        self.load_data()
        self.resolve_conflicts = False
    
    def load_data(self):
        try:
            f_path = self.kubicleJson.file_path + "/core/nodes/blockchain-{}.json".format(self.nodeId)
            
            with open(f_path , mode='r') as f:
                file_content = f.readlines()
                self.blockchain = json.loads(file_content[0][:-1])
        except (IOError, IndexError):
            pass
        finally:
            pass


    def save_data(self):
        try:
            f_path = self.kubicleJson.file_path + "/core/nodes/blockchain-{}.json".format(self.nodeId)
            
            self.kubicleJson.create_dir(f_path)
            
            with open(f_path , mode='w') as f:
                f.write(json.dumps(self.blockchain))
                f.write('\n')
                f.write(json.dumps(self.open_votes))
        except IOError:
            print('Saving failed!')


    def add_block(self, block):
        """Add a block which was received via broadcasting to the localb
        lockchain."""
        
        #TODO: validate block already exists
        #TODO: validate digitally signed
        #TODO: decrypt data
        
        hashes_match = self.hash_block(self.blockchain[-1]) == block['previous_hash']
        if not hashes_match:
            return False
        
        votes = []
        for vt in block['votes']:
            vote = { 
                'vote_id': vt['vote_id'], 
                'candidate': vt['candidate']
            }
            votes.append(vote)

        # Create a Block object
        broadcasted_block = {
            'previous_hash': block['previous_hash'],
            'index': block['index'],
            'votes': votes
        }

        self.blockchain.append(broadcasted_block)
        
        self.save_data()
        return True


    def hash_block(self, block):
        strBlock = json.dumps(block) #converts the object block into a string that looks like json
        strBlock = strBlock.encode() #encode into utf-8
        byteHashBlock = hashlib.sha256(strBlock) #converts string into byte hash
        hashedBlock = byteHashBlock.hexdigest() #converts hash in string format
        
        return hashedBlock
        #return '-'.join([str(block[key]) for key in block])


    def get_vote_count(self):
        
        counter = dict()
        
        for block in self.blockchain:
            for vote in block['votes']:
                key = vote['candidate'] #dictionary key i.e: 1, 2, 3 or 4 (represents the candidate #)
                counter[key] = counter.get(key, 0) + 1 #votes.get check if the key/candidate has value otherwise sets the initial value to 0 (zero)

        return counter


    def get_last_blockchain_value(self):
        """ Returns the last value of the current blockchain"""
        if len(self.blockchain) < 1:
            return None
        return self.blockchain[-1]


    def add_vote(self, vote_id, candidate):
        """ add vote
        
        Arguments:
            :vote_id: unique id per voter/student
            :candidate: candidate of a list of choices
        """
        
        vote = { 
            'vote_id': vote_id, 
            'candidate': candidate
        }

        if self.verify_vote(vote):
            self.open_votes.append(vote)
            return True
        return False


    #will append the vote to the blockchain
    def mine_block(self):
        last_block = self.blockchain[-1] #retrieve the previous block of the blockchain
        hashed_block = self.hash_block(last_block) #hash the previous block

        print("hashed_block: ", hashed_block)

        copied_votes = self.open_votes[:]
        block = {
            'previous_hash': hashed_block,
            'index': len(self.blockchain),
            'votes': copied_votes
        }
        #TODO: validate if the votes are valid to be added
        #TODO: broadcast the event of addind a block
        self.blockchain.append(block)

        #empty open_transactions
        self.open_votes = []

        self.save_data()
        self.broadcast_block(block)
        return True


    def broadcast_block(self, block):
        for node in self.__peer_nodes:
            url = 'http://localhost:{}/broadcast-block'.format(node)

            converted_block = block.copy()
            #try:
            response = requests.post(url, json={'block': converted_block})
            if response.status_code == 400 or response.status_code == 500:
                print('Block declined, needs resolving')
            if response.status_code == 409:
                self.resolve_conflicts = True
            #except requests.exceptions.ConnectionError:
            #    continue
            
            return block


    """
    creates a vote data:
    Request input ID and candidate from user (Console input)
    """
    def get_vote_data(self):
        """ Returns the input of the user (transaction amount in float format) """
        vote_id = input("Vote ID: ")
        candidate = int(input("Choose a number: \n [1] Donald \n [2] Hillary \n "))
        return (vote_id, candidate) #is gonna return a tuple


    def get_user_choice(self):
        user_input = input("Your choice: ")
        return user_input


    def print_vote_count(self):
        votes = self.get_vote_count()
        print(f"Votes: {votes}")
        for vote in votes:
            print(f"candidate - {vote}: {votes[vote]} votes")


    def get_last_blockchain_value(self):
        """ Returns the last value of the current blockchain"""
        if len(self.blockchain) < 1:
            return None
        return self.blockchain[-1]


    def print_blockchain_elements(self):
        #print(blockchain)
        for (index, block) in enumerate(self.blockchain):
            print(f"output block [{index}]: ")
            print(block)
            print("\n")
        else:
            print("-" * 20)


    def verify_chain(self):
        """ Compare the stored hash in a *given block 
            with the *recalculated hash with the *previous block """


        for (index, block) in enumerate(self.blockchain):
            #skips the genesis block because there's nothing before it.
            #Also not necessary to validate genesis block
            if index == 0:
                continue

            #every block holds the hash of the previous block
            previous_hash = block['previous_hash']
            recalc_previous_hash = self.hash_block(self.blockchain[index-1])
            
            if previous_hash != recalc_previous_hash: #compares the current block with the previous block (hash comparison)
                print(f"XXXXX\n prev_hash: {previous_hash} != {recalc_previous_hash} \nXXXXX")
                return False
        
        return True #if all the calculated hashes match then blockchain is valid 


    #TODO: implement verify votes
    def verify_vote(self, vote):
        return True


waiting_for_input = False

while waiting_for_input:
    objBlockchain = Blockchain("NODE_TX")

    print("\nPlease choose")
    print("1: add a new vote")
    print("2: Mine block")
    print("3: output the blockchain blocks")
    print("4: output vote count")
    print("h: Manipulate blocks!")
    print("q: quit")
    user_choice = objBlockchain.get_user_choice()

    if user_choice == "1":
        tx_data = objBlockchain.get_vote_data()
        vote_id, candidate = tx_data #unpack the tuple 1st and 2nd value rescpetively

        #add vote to the blockchain
        ret = objBlockchain.add_vote(vote_id=vote_id, candidate=candidate)
        print("return: ", ret)
        print("open_votes: ", objBlockchain.open_votes)
    elif user_choice == "2":
        objBlockchain.mine_block()
    elif user_choice == "3":
        objBlockchain.print_blockchain_elements()
    elif user_choice == "4":
        objBlockchain.print_vote_count()
    elif user_choice == "h":
        if len(objBlockchain.blockchain) >= 1:
            objBlockchain.blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'votes': [{'vote_id': '00000', 'candidate': '1'}]
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("invalid input")

    if not objBlockchain.verify_chain():
        objBlockchain.print_blockchain_elements()
        print("Invalid blockchain")
        break

else:
    print("User left!")