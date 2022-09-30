from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
from pymongo import MongoClient
import sys,os,logging
sys.path.insert(0,'../scripts/')
from scripts.create_account import create_account
from scripts.create_nft import create_nft
from scripts.asset_transfer import asset_transfer
logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)
client = MongoClient('localhost', 27017)
database = client.web3
trainees = database.trainess
admins = database.admins

@app.route('/')
def index():
    
    return render_template('admin_index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def admin_account():
    if request.method == 'GET':
        admin_acc = create_account()
        admin_info = {
            "private_key":admin_acc[0],
            "address":admin_acc[1],
            "message":admin_acc[3]}
        admins.insert_one(admin_info).inserted_id

        return  render_template('admin_account.html',admin_info), jsonify({
            "status": "success",
            "private_key":admin_acc[0],
            "address":admin_acc[1],
            "message":admin_acc[3]
        })

@app.route('/create_nft', methods=['GET', 'POST'])
def create_nft():
    if request.method == 'POST':
        public_key = request.get_json()['public_key']
        private_key = request.get_json()['private_key']
        unit_name = request.get_json()['unit_name']
        asset_name = request.get_json()['asset_name']
        nft = create_nft(public_key,private_key,unit_name,asset_name)
        return jsonify({
            "status": "success",
            "txid":nft[0],
            "asset_id":nft[1],
            "confirmed_round":nft[2]
            })
@app.route('/asset_transfer', methods=['GET', 'POST'])
def transfer_asset():
    if request.method == 'POST':
        sender_public_key = request.get_json()['sender_public_key']
        sender_private_key = request.get_json()['sender_private_key']
        receiver_public_key = request.get_json()['receiver_public_key']
        asset_id = request.get_json()['asset_id']
        transfer = asset_transfer(sender_public_key,sender_private_key,receiver_public_key,asset_id)
        return jsonify({
            "status": "success",
            "txid":transfer[0],
            "asset_id":transfer[1],
            "confirmed_round":transfer[2]
            })
