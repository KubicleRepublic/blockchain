from enum import Enum

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

class CandidateEnum(Enum):
    none = 0
    Trump = 1
    Hillary = 2
    Darth = 3
    Putin = 4

class Blockchain:

    def __init__(self):
        self.blockchain = [genesis_block]
        self.open_votes = []
    

    def hash_block(self, block):
        return '-'.join([str(block[key]) for key in block])


    # 1 - vote
    # vote = { 
    #     'vote_id': 1111, 
    #     'candidate': 2
    # }

    # 2 - list of votes
    # list_of_pending_votes = []
    # list_of_pending_votes.append(vote)

    # 3 - block with 4 votes
    # block = {
    #     'previous_hash': 'hash',
    #     'index': 3,
    #     'votes': list_of_pending_votes
    # }

    # 4 - blockchain
    #blockchain.append(block)

    #vote -> lst_votes -> block(lst_votes) -> lst_blocks(block)

    # lst_blocks #plural
    #     block #singular
    #         lst_votes #plural
    #             vote #singular

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

        print(hashed_block)

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
        return True


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
        print(f"robb: {votes}")
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
    objBlockchain = Blockchain()

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
        objBlockchain.add_vote(vote_id=vote_id, candidate=candidate)
        print(objBlockchain.open_votes)
    elif user_choice == "2":
        if objBlockchain.mine_block():
            objBlockchain.open_votes = [] #empty outstanding votes after creating the block
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