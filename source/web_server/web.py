from flask import Flask, render_template, request, jsonify, request
from collections import defaultdict
from werkzeug.utils import secure_filename
import json
import os
import requests
from functools import reduce
from candidates import CandidateEnum

#from OpenSSL import SSL
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


host_url = None

#principals = Principal(app)
#admin_permission = Permission(RoleNeed('Admin'))

#sec test for admin permissions

# @app.route('/admin')
# @admin_permission.require()
# def do_admin_index():
# return Response('only accessible if you are an admin')

#This is where the UPLOADS folder is set
#Will create script for this later to recognize path

SOURCE_DIRECTORY = os.path.dirname(os.path.dirname(__file__)) #absolut path until source dir
UPLOAD_FOLDER = SOURCE_DIRECTORY + "/web_server/UPLOADS"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/") #home voting
@app.route("/home")
#use uploadScreen.html
def home():
    return render_template('home.html')


@app.route("/upload")
def upload():
    return render_template('uploadScreen.html')


@app.route("/vote-submission", methods=['GET','POST'])
def vote_submission():
    if request.method == 'POST':

            url = host_url + '/ballot'

            EID = request.form["eid"]
            electee = request.form["options"]
           
            print(EID + " and vote is " + electee)
            Token = {'EID': EID,'candidate' : electee}
            response = requests.post(url, json= Token)
                      
            return results(msg="Thanks for voting!")


@app.route("/results")
def results(msg=None):
    
    response = get_votes()
    if not msg == None:
        response["msg"] = msg

    results = []
    if response:
        total_ballot = reduce(lambda votes_sum, value: votes_sum + value if type(value) is int else votes_sum + 0, response.values(), 0)
        
        for x in range(1,5):
            candidate = CandidateEnum(x).name
            total_votes = response.get(str(x), 0)
            vote_percent = round((total_votes / total_ballot) * 100, 2)
        
            result = { 'y': vote_percent, 'label': (str(vote_percent) + "%"), 'indexLabel': candidate }
            results.append(result)
    
    return render_template('results.html', results=results, msg=msg)


@app.route('/success', methods =['GET', 'POST'])
def success():
    
    url = host_url + '/ballot'

    electee = request.form["options"]
    print(electee)
    
    # Token = {'EID': EID,'candidate' : electee}
    # response = requests.post(url, json= Token)

    #This reads the "file" attribute
    f = request.files['file']

    #This works, but it saves in current dir where script is
    #f.save(f.filename)

    #This Saves script in the UPLOAD_FOLDER
    print("path: ", app.config['UPLOAD_FOLDER'])
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    
    return render_template("success.html", name=f.filename)


def get_votes():
    url = host_url + '/get_votes'
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    host_url = "http://localhost:8080"
    app.run(host='0.0.0.0') #ssl_context='adhoc'
    #app.run(ssl_context='adhoc') #host='0.0.0.0'
