from flask import Flask, request, jsonify, render_template, url_for, redirect
from pymongo import MongoClient
import sys,os,logging,json
sys.path.insert(0,'../scripts/')
from create_account import create_account
from create_nft import create_NFT
from asset_transfer import asset_transfer
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

        return  render_template('admin_account.html',admin_info=admin_info)

@app.route('/create_nft', methods=['GET', 'POST'])
def create_nft():
    if request.method == 'POST':
        public_key = request.form.get('public_key')
        trainee_name = request.form.get('trainee_name')
        unit_name = request.form.get('unit_name')
        asset_name = request.form.get('asset_name')
        nft = create_NFT(public_key,unit_name,asset_name)
        res_bytes = dict(nft.dictify())
        return render_template('algosigner.html', nft = nft,public_key=public_key,trainee_name=trainee_name,unit_name=unit_name,asset_name=asset_name,res_bytes=res_bytes)
    if request.method == 'GET':
        return render_template('create_nft.html')
        
@app.route('/asset_transfer', methods=['GET', 'POST'])
def transfer_asset():
    if request.method == 'POST':
        sender_public_key = request.form()['public_key']
        receiver_public_key = request.form()['receiver_public_key']
        asset_id = request.form()['asset_id']
        if request.form.get('action1') == 'approved':
            transfer = asset_transfer(sender_public_key,receiver_public_key,asset_id)
            return render_template('transfer_asset.html',transfer=transfer)
        elif request.form.get('action2') == 'declined':
            trainees.update_one({'asset_id':asset_id},{ "$set": { 'status': "Declined" } })
            return redirect(url_for('trainee_rquests'))
        

@app.route('/store_asset',methods=['POST'])
def store_asset():
    if request.method =='POST':
        output = request.get_json()
        result = json.loads(output)
        trainees.insert_one(result).inserted_id
        return redirect(url_for('trainee_rquests'))

@app.route('/trainee_rquests',methods=['GET','POST'])
def trainee_requests():
    data = trainees.find()
    return render_template('trainee_requests.html',data=data)
@app.route('/update_asset',methods=['GET','POST'])
def update_asset():
    if request.method =='POST':
        output = request.get_json()
        result = json.loads(output)
        id = result['asset_id']
        status = result['status']
        trainees.update_one({'asset_id':id},{ "$set": { 'status': status } })
        return redirect(url_for('trainee_rquests'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', debug=True, port=port)