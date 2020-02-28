from flask import Flask, render_template, request, jsonify
from collections import defaultdict
#from flask. import principal, permission, RoleNeed
import json
import os
import requests
#from OpenSSL import SSL
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


#principals = Principal(app)
#admin_permission = Permission(RoleNeed('Admin'))

# @app.route('/admin')
# @admin_permission.require()
# def do_admin_index():
#     return Response('only if you are admin')

@app.route("/")
def hello():
    return "hello world, could u proceed to /home"

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/receive-count", methods=['GET'])
def receive_count():

    url = 'http://localhost:8080/get_votes'
    returned = requests.get(url)
    return returned.text

@app.route("/file-reader", methods=['GET'])
def filereader():
    # mylines = []
    # with open ('m.json', 'rt') as myfile:
    #     for myline in myfile:
    #         mylines.append(myline)
    return "hewwo"
            #return mylines.text


@app.route("/vote-submission", methods=['GET','POST'])
def vote_submission():
    if request.method == 'POST':

            url = 'http://localhost:8080/ballot'

           # newcount = defaultdict(int)

            EID = request.form["test1"]
            electee = request.form["options"]

            # if electee == 'A':
            #     newcount['Donald'] += 1
            print(EID + " and vote is " + electee)
            Token = {'EID': EID,'candidate' : electee}
            response = requests.post(url, data = Token)
                # print(newcount)
            print("----------")
            
            # print(EID + " and vote is " + electee)
            # Token = {'EID': EID,'candidate' : electee}
            # response = requests.post(url, data = Token)
            # #response = "this is the answer from the node: " + x.text
            # #print(response)
            # print("----------")
    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0') #ssl_context='adhoc'
    #app.run(ssl_context='adhoc') #host='0.0.0.0'