import json
import hashlib
import os
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation



def create_nft(public_key,unit_name,asset_name):
 
  algod_address = "https://testnet-algorand.api.purestake.io/ps2"
  algod_token = "hX5WEmJCdA8dS7wgsxZ57aBbUSzz8K0O5TPLrgVn"
  headers = {
   "X-API-Key": algod_token,
    }
  algod_client = algod.AlgodClient(algod_token, algod_address,headers)

  params = algod_client.suggested_params()
 
  dir_path = os.path.dirname(os.path.realpath(__file__))
  f = open (dir_path + '../assests/metadata.json', "r")
  path = dir_path + '../assests/metadata.json'

  metadataJSON = json.loads(f.read())
  metadataStr = json.dumps(metadataJSON)

  hash = hashlib.new("sha512_256")
  hash.update(b"arc0003/amj")
  hash.update(metadataStr.encode("utf-8"))
  json_metadata_hash = hash.digest()


  txn = AssetConfigTxn(
      sender=public_key,
      sp=params,
      total=1,
      default_frozen=False,
      unit_name=unit_name,
      asset_name=asset_name,
      manager=public_key,
      reserve=None,
      freeze=None,
      clawback=None,
      strict_empty_address_check=False,
      url=path, 
      metadata_hash=json_metadata_hash,
      decimals=0)

  '''stxn = txn.sign(private_key)

  txid = algod_client.send_transaction(stxn)


  confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
  confirmed_round = confirmed_txn['confirmed-round']'''  
  
  try:
      
      '''ptx = algod_client.pending_transaction_info(txid)
      asset_id = ptx["asset-index"]'''

      return txn

      
  except Exception as e:
      print(e)
      return
    