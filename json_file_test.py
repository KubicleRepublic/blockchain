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


kubicleJson.write(myData)

mockOn = 0 #1 or 0
if mockOn:
    kubicleJson.write( 
    {
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
    })