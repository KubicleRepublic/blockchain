import json

#file_path = "/home/e/node/"
#file_path = "/home/e/Desktop/SAIT/Capstone/blockchain/"

file_path = "./"
file_name = "m.json" 
 
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
            json.dump(data, file_object, ensure_ascii=False, indent=4)

# myData = kubicleJson.load()                        
# #print(data.chain)
# for block in myData["chain"]:
#     print(block["index"], ": " , block["hashid"])
