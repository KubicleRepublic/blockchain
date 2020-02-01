import imp
node = imp.load_source('node', 'nodeV0.3.py') #import files with dot
from node import Node

node1 = Node()
node1.startup()