from flask import Flask, render_template, request, jsonify
from collections import defaultdict
#from flask. import principal, permission, RoleNeed
import json
import os
import requests
from OpenSSL import SSL
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
    return "hello, proceed to /home"

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/receive-count", methods=['GET'])
def receive_count():

    url = 'http://10.187.229.245:8080/get_votes'
    returned = requests.get(url)
    return returned.text
    

@app.route("/vote-submission", methods=['GET','POST'])
def vote_submission():
    if request.method == 'POST':

            url = 'http://10.187.229.245:8080/ballot'

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

app.run(host='0.0.0.0') #ssl_context='adhoc'