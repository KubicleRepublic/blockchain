import json

#file_path = "/home/user/node/"
file_path = "/home/user/git/kubicleRepublic/blockchain/"
file_name = "kubicle.json"
 
 
mock_json_data = {
    "chain": [
        {
            "index": 0,
            "hashid": "genesis",
            "merkleroot": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
            "timestamp": 1541152127213,
            "candidate": "2"
        },
        {
            "index": 1,
            "hashid": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
            "merkleroot": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
            "timestamp": 1541152127214,
            "candidate": "3"
        },
        {
            "index": 2,
            "hashid": "000000000019d6689c085ae1658abcf5463252cdff131313f31fd3fb3f1b60a8ce26f",
            "merkleroot": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
            "timestamp": 1541152127214,
            "candidate": "3"
        }
    ]
} 
 
class kubicleJson:

    def __init__():
        print("instance of a class")
        pass
    
    def update_mock_json_file():
        self.write(mock_json_data)
     
    def load():
        #File I/O Open function for read data from JSON File
        with open(file_path + file_name) as file_object:
            # store file data in object
            data = json.load(file_object)
            return data
            
    def write(data):
        with open(file_path + file_name, 'w', encoding='utf-8') as file_object:
            # store file data in object
            json.dump(data, f, ensure_ascii=False, indent=4)

# myData = kubicleJson.load()                        
# #print(data.chain)
# for block in myData["chain"]:
#     print(block["index"], ": " , block["hashid"])
