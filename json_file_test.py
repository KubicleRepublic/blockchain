###importing python files:
# option 1:
# from folder.file import Klasa

# option 2:
# from folder import file
# k = file.Klasa()

# option 3:
# import folder.file as myModule
# k = myModule.Klasa()

from json_file import kubicleJson

myData = kubicleJson.load()                        
originalData = myData

index = 0

#print(data.chain)
for block in myData["chain"]:
    print(block["index"], ": " , block["hashid"], " candidate: ",block["candidate"])
    block["index"] = "Robbert" + str(index + 1)
    block["hashid"] = "Robbert" + str(index + 1)
    block["candidate"] = "Robbert" + str(index + 1)
    block["timestamp"] = "Robbert" + str(index + 1)
    block["merkleroot"] = "Robbert" + str(index + 1)

print(myData)




