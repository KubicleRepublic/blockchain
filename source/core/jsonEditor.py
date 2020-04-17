import json
import os
from os import path
import errno

SOURCE_DIRECTORY = os.path.dirname(os.path.dirname(__file__)) #absolut path until source dir
FILE_NAME = "m.json"  


class JsonEditor:

    """
        Arguments: 
            FILE_NAME: You can specify different file
    """
    def __init__(self, file_name=FILE_NAME, file_path=SOURCE_DIRECTORY, file_add_folder=""):
        self.file_name = file_name        
        self.file_path = file_path

        if file_add_folder:
            self.file_path = file_path + "/" + file_add_folder
        self.full_file_path_name = self.file_path + "/" + self.file_name


    def create_dir(self, full_file_path=None):
        if full_file_path == None:
            full_file_path = self.full_file_path_name

        if not os.path.exists(os.path.dirname(full_file_path)):
            try:
                os.makedirs(os.path.dirname(full_file_path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(full_file_path, "w") as f:
            f.write("")
            

    def load(self):
        file_path_name = self.file_path + "/" + self.file_name

        if not os.path.isfile(file_path_name):
            print("File does not exist")
            return {"alert": "File does not exist"}

        #check if the file is empty
        if os.stat(file_path_name).st_size == 0:
            print("This file is empty")
            return {"alert": "this files is empty"}

        #File I/O Open function for read data from JSON File
        with open(file_path_name, 'r') as file_object:
            # store file data in object
            if file_object.read(2) != '[]':
                file_object.seek(0)  # it may be redundant but it does not hurt
                data = json.load(file_object)
                return data

    
    def write(self,data, isJson=True):
        with open(self.file_path + self.file_name, 'w', encoding='utf-8') as file_object:
            # store file data in object
            if isJson:
                file_object.write(json.dump(data, file_object, ensure_ascii=False, indent=4))
            else:
                file_object.write(data)

# myData = kubicleJson.load()                        
# #print(data.chain)
# for block in myData["chain"]:
#     print(block["index"], ": " , block["hashid"])
