import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests #this module allows to send data through the nodes
from blockchain import Blockchain
from node import Node
from argparse import ArgumentParser

app = Flask(__name__)
CORS(app) #CORS allows other nodes to communicate between each other

blockchainz = None
node = None

#default host and port

# import pdb
# pdb.set_trace()

@app.route("/ballot", methods=["POST"])
def ballot():
    data = request.get_json()
    response = "This is the node response: {}".format(data)

    eid = data.get("EID")
    candidate = data.get("candidate")

    open_votes_qt = blockchainz.add_vote(eid, candidate)
    print(f"this is open_votes: {open_votes_qt}")
    if 1 == 1 or open_votes_qt == 1:
        blockchainz.mine_block()
            
    return response


@app.route("/get_votes", methods=["GET"])
def get_votes():
    result = blockchainz.get_vote_count()
    print(blockchainz.blockchain)
    return result


@app.route("/", methods=["GET"])
def get_home():
    return 'This is home!'


@app.route("/ui", methods=["GET"])
def get_ui():
    return send_from_directory('ui', 'node.html')


@app.route("/broadcast-block", methods = ['POST'])
def broadcast_block():
    #gets the data that was sent
    data = request.get_json(force=True)
    print(data)
    print("broadcasting....")

    if not data:
        response = {"msg": "No data"}
        return jsonify(response), 400
    
    if 'block' not in data:
        response = {'message': 'Some data is missing.'}
        return jsonify(response), 400
    block = data['block']

    print("block: ", block)
    if block['index'] == blockchainz.blockchain[-1]['index'] + 1:
        if blockchainz.add_block(block):
            response = {'message': 'Block added'}
            return jsonify(response), 201
        else:
            response = {'message': 'Block seems invalid.'}
            return jsonify(response), 409
    elif block['index'] > blockchainz.blockchain[-1]['index']:
        response = {
            'message': 'Blockchain seems to differ from local blockchain.'}
        blockchainz.resolve_conflicts = True
        return jsonify(response), 200
    else:
        response = {
            'message': 'Blockchain seems to be shorter, block not added'}
        return jsonify(response), 409


if __name__ == '__main__':
    app.debug = True
    
    default_host = '0.0.0.0'
    default_port = '8080'
    
    #settings arguments from commandline for Dev purposes
    parser = ArgumentParser()
    parser.add_argument("-H", "--host", help="Hostname of the Flask app " + "[default %s]" % default_host, default=default_host)
    parser.add_argument("-P", "--port", help="Port for the Flask app " + "[default %s]" % default_port, default=default_port)
    
    app.args = parser.parse_args()

    nodeName = app.args.port
    blockchainz = Blockchain(nodeId=nodeName)

    app.run(host=app.args.host, port=app.args.port)