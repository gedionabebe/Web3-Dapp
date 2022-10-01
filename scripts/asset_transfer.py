from algosdk.v2client import algod
from algosdk.future.transaction import AssetTransferTxn, wait_for_confirmation


def asset_transfer(sender_public_key,receiver_public_key,asset_id):
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = "hX5WEmJCdA8dS7wgsxZ57aBbUSzz8K0O5TPLrgVn"
    headers = {
     "X-API-Key": algod_token,
     }

    algod_client = algod.AlgodClient(algod_token, algod_address,headers)
    params = algod_client.suggested_params()

    txn = AssetTransferTxn(
    sender=sender_public_key,
    sp=params,
    receiver=receiver_public_key,
    amt=1,
    index=asset_id)
    

    try:
        return txn
    except Exception as err:
        print(err)
        return


   