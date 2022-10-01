from algosdk.v2client import algod
from algosdk.future.transaction import AssetTransferTxn, wait_for_confirmation


def asset_optin(public_key,private_key,asset_id):
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = "hX5WEmJCdA8dS7wgsxZ57aBbUSzz8K0O5TPLrgVn"
    headers = {
     "X-API-Key": algod_token,
     }
    algod_client = algod.AlgodClient(algod_token, algod_address,headers)
   
    params = algod_client.suggested_params()
   
    account_info = algod_client.account_info(public_key)
    holding = None
    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]
        idx = idx + 1    
        if (scrutinized_asset['asset-id'] == asset_id):
            holding = True
            break
    if not holding:
        
        txn = AssetTransferTxn(
        sender=public_key,
        sp=params,
        receiver=public_key,
        amt=0,
        index=asset_id)
        #stxn = txn.sign(private_key)
        
        try:
            '''txid = algod_client.send_transaction(stxn)
            
            confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
            confirmed_round = confirmed_txn['confirmed-round']''' 
           
            return txn   
        except Exception as err:
            print(err)
            return

   