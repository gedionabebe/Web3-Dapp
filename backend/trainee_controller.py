from flask import Flask, request, jsonify
import sys,os,logging
sys.path.insert(0,'../scripts/')
from scripts.create_account import create_account
from scripts.asset_optin import asset_optin
logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    
    return jsonify({
                "status": "success",
                "message": "Index Page"
             })

@app.route('/create_account', methods=['GET', 'POST'])
def user_account():
    if request.method == 'GET':
        user_acc = create_account()
        return jsonify({
            "status": "success",
            "private_key":user_acc[0],
            "address":user_acc[1],
            "message":user_acc[3]
        })

@app.route('/asset_optin', methods=['GET', 'POST'])
def asset_optin():
    if request.method == 'POST':
        public_key = request.get_json()['public_key']
        private_key = request.get_json()['private_key']
        asset_id = request.get_json()['asset_id']
        optin = asset_optin(public_key,private_key,asset_id)
        return jsonify({
            "status": "success",
            "txid":optin[0],
            "asset_id":optin[1],
            "confirmed_round":optin[2]
            })