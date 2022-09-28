from flask import Flask, request, jsonify
import sys,os,logging
sys.path.insert(0,'../scripts/')
from create_account import create_account
from create_nft import create_nft
from asset_transfer import asset_transfer
logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    
    return jsonify({
                "status": "success",
                "message": "Index Page"
             })

@app.route('/create_account', methods=['GET', 'POST'])
def admin_account():
    if request.method == 'GET':
        admin_acc = create_account()
        return jsonify({
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
