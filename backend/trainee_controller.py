from flask import Flask, request, jsonify,render_template,redirect,url_for
from pymongo import MongoClient
import sys,os,logging,json
sys.path.insert(0,'../scripts/')
from scripts.create_account import create_account
from scripts.asset_optin import asset_optin
logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)
client = MongoClient('localhost', 27017)
database = client.web3
trainees = database.trainess

@app.route('/')
def index():
    
    return render_template('trainee_index.html')

@app.route('/create_user_account', methods=['GET', 'POST'])
def create_user_account():
    if request.method == 'POST':
        user_acc = create_account()
        receiver_public_key=user_acc[1]
        trainee_name = request.form()['trainee_name']
        trainees.update_one({'trainee_name':trainee_name},{ "$set": { 'receiver_public_key': receiver_public_key } })
        return redirect(url_for('asset_view',key=receiver_public_key))

@app.route('/asset_optin', methods=['GET', 'POST'])
def asset_optin():
    if request.method == 'POST':
        receiver_public_key = request.form()['receiver_public_key']
        #private_key = request.get_json()['private_key']
        asset_id = request.form()['asset_id']
        optin = asset_optin(receiver_public_key,asset_id)
        trainees.update_one({'asset_id':asset_id},{ "$set": { 'status': 'Requested' } })
        return render_template('optin.html',optin=optin) 
@app.route('/asset_view', methods=['GET', 'POST'])
def asset_view(key):
    data = trainees.find_one({"receiver_public_key":key})
    return render_template('asset_view.html',data=data)