import configparser

config = configparser.ConfigParser()                                     
config.read('./config.ini')

print(config['NODE']['folder_name'])
print(config.get('NODE', 'folder_name'))
print(config.get('NODE', 'nodes'))

nodeIPs = config.get('NODE', 'nodes')
nodeIPs = nodeIPs.split(",")

print("----------")

for node in nodeIPs:
    print(node)