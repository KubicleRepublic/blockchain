from flask import Flask, render_template, request, jsonify, request
from collections import defaultdict
from werkzeug.utils import secure_filename
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
# return Response('only if you are admin')

#This is where the UPLOADS folder is set
#Will create script for this later to recognize path
UPLOAD_FOLDER = "/home/e/Desktop/SAIT/Capstone/blockchain/source/web_server/UPLOADS"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def hello():
    return "hello world, could u proceed to /home"

@app.route("/vote-submission", methods=['GET','POST'])
def vote_submission():
    if request.method == 'POST':

            url = 'http://localhost:8080/ballot'

           # newcount = defaultdict(int)

            EID = request.form["test1"]
            electee = request.form["options"]
            #tokenfile = request.form["fileToUpload"]
            #print(tokenfile)

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
            return render_template('success.html',name = f.filename)


@app.route("/home")
#use uploadScreen.html
def home():
    return render_template('uploadScreen.html')
    vote_submission()

@app.route('/success', methods =['POST'])
def success():
    if request.method == 'POST':
        #This is reading what candidate was voted for
        url = 'http://localhost:8080/ballot'
        electee = request.form["options"]
        print("vote is " + electee)
        Token = {'candidate' : electee}
        response = requests.post(url, data = Token)

        #This reads the "file" attribute
        f = request.files['file']

        #This works, but it saves in current dir where script is
        #f.save(f.filename)

        #This Saves script in the UPLOAD_FOLDER
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        
        return render_template("success.html", name = f.filename), response.text
    
@app.route("/receive-count", methods=['GET'])
def receive_count():

    url = 'http://localhost:8080/get_votes'
    returned = requests.get(url)
    return returned.text

if __name__ == "__main__":
    app.run(host='0.0.0.0') #ssl_context='adhoc'
    #app.run(ssl_context='adhoc') #host='0.0.0.0'
