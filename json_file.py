import json
import os

FILE_PATH = "./"
FILE_NAME = "m.json"  

class KubicleJson:

    def __init__(self, file_name=FILE_NAME, file_path=FILE_PATH):
        self.file_name = file_name
        self.file_path = file_path
   
    def load(self):
        file_path_name = self.file_path + self.file_name

        #check if the file is empty
        if os.stat(file_path_name).st_size == 0:
            return {"alert": "this files is empty"}

<<<<<<< HEAD
=======
    def __init__():
        print("instance of a class")
        pass
    
    def update_mock_json_file():
        self.write(mock_json_data)
    
    @staticmethod
    def load():
>>>>>>> bd5d986f0050702da7026039cffb3212d0207d14
        #File I/O Open function for read data from JSON File
        with open(self.file_path + self.file_name) as file_object:
            # store file data in object
<<<<<<< HEAD
            if file_object.read(2) != '[]':
                file_object.seek(0)  # it may be redundant but it does not hurt
                data = json.load(file_object)
                return data
    
    def write(self,data):
        with open(self.file_path + self.file_name, 'w', encoding='utf-8') as file_object:
=======
            data = json.load(file_object)
            return data

    @staticmethod        
    def write(data):
        with open(file_path + file_name, 'w', encoding='utf-8') as file_object:
>>>>>>> bd5d986f0050702da7026039cffb3212d0207d14
            # store file data in object
            json.dump(data, file_object, ensure_ascii=False, indent=4)

# myData = kubicleJson.load()                        
# #print(data.chain)
# for block in myData["chain"]:
#     print(block["index"], ": " , block["hashid"])
