import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests #this module allows to send data through the nodes

import imp
node = imp.load_source('node', 'nodeV0.3.py')
from node import Node

app = Flask(__name__)
CORS(app) #CORS allows other nodes to communicate between each other

nodes = [
    "10.0.0.240:8080"
]

@app.route("/", methods=["GET"])
def get_ui():
    return send_from_directory('ui', 'node.html')

@app.route("/broadcast", methods = ['POST', 'GET'])
def broadcast():
    #gets the data that was sent
    data = request.get_json()

    if not data:
        response = {"msg": "No data"}
        return jsonify(response), 400
    
    #TODO: 
    # check if the save_data was successful
    # return error msg
    #  
    global node
    node = Node()
    node.save_data(data)

    if success:
        response = {
            'message': 'Successfully saved.'
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'failed to save.'
        }
        return jsonify(response), 500


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)