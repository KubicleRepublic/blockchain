import json
import os

FILE_PATH = "./"
FILE_NAME = "m.json"  

class KubicleJson:

    """
        Arguments: 
            FILE_NAME: You can specify different file
    """
    def __init__(self, file_name=FILE_NAME, file_path=FILE_PATH):
        self.file_name = file_name
        self.file_path = file_path
   
    def load(self):
        file_path_name = self.file_path + self.file_name

        #check if the file is empty
        if os.stat(file_path_name).st_size == 0:
            return {"alert": "this files is empty"}

        #File I/O Open function for read data from JSON File
        with open(self.file_path + self.file_name) as file_object:
            # store file data in object
            if file_object.read(2) != '[]':
                file_object.seek(0)  # it may be redundant but it does not hurt
                data = json.load(file_object)
                return data
    
    def write(self,data):
        with open(self.file_path + self.file_name, 'w', encoding='utf-8') as file_object:
            # store file data in object
            json.dump(data, file_object, ensure_ascii=False, indent=4)

# myData = kubicleJson.load()                        
# #print(data.chain)
# for block in myData["chain"]:
#     print(block["index"], ": " , block["hashid"])
