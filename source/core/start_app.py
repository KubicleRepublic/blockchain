import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests #this module allows to send data through the nodes
import blockchain
from node import Node
from argparse import ArgumentParser

app = Flask(__name__)
CORS(app) #CORS allows other nodes to communicate between each other

#default host and port

# import pdb
# pdb.set_trace()

@app.route("/ballot", methods=["POST"])
def ballot():
    data = request.get_data()
    response = "This is the node response: {}".format(data)
    print(f"node test {data}")
    #convert the data.candidate into a num
    #data.EID
    #data.candidate
    # blockchain.add_vote(data.EID, data.candidate)
    open_votes_qt = blockchain.add_vote(1111, 1)
    print(f"this is open_votes: {open_votes_qt}")
    if open_votes_qt == 2:
        blockchain.mine_block()
    
    return response


@app.route("/get_votes", methods=["GET"])
def get_votes():
    result = blockchain.get_vote_count()
    return result


@app.route("/", methods=["GET"])
def get_home():
    return 'This is home!'


@app.route("/ui", methods=["GET"])
def get_ui():
    return send_from_directory('ui', 'node.html')


@app.route("/broadcast", methods = ['POST'])
def broadcast():
    #gets the data that was sent
    data = request.get_json(force=True)
    print(data)
    print("test")

    if not data:
        response = {"msg": "No data"}
        return jsonify(response), 400
    
    #TODO: 
    # check if the save_data was successful
    # return error msg
    #  
    global node
    node = Node("node" + app.args.port)
    node.save_data(data)

    #if success:
    response = {
        'message': 'Successfully saved.'
    }
    return jsonify(response), 201
    # else:
    #     response = {
    #         'message': 'failed to save.'
    #     }
    #     return jsonify(response), 500


if __name__ == '__main__':
    app.debug = True
    
    default_host = '0.0.0.0'
    default_port = '8080'
    
    #settings arguments from commandline for Dev purposes
    parser = ArgumentParser()
    parser.add_argument("-H", "--host", help="Hostname of the Flask app " + "[default %s]" % default_host, default=default_host)
    parser.add_argument("-P", "--port", help="Port for the Flask app " + "[default %s]" % default_port, default=default_port)
    
    app.args = parser.parse_args()

    #host = os.environ.get('IP', '0.0.0.0')
    #port = int(os.environ.get('PORT', 8080))
    app.run(host=app.args.host, port=app.args.port)