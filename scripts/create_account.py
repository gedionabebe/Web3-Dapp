from algosdk import account, mnemonic
from algosdk.v2client import algod



def create_account():
    private_key, address = account.generate_account()
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = "hX5WEmJCdA8dS7wgsxZ57aBbUSzz8K0O5TPLrgVn"
    headers = {
   "X-API-Key": algod_token,
    }
    algod_client = algod.AlgodClient(algod_token, algod_address,headers)
    account_info = algod_client.account_info(address)
    message = mnemonic.from_private_key(private_key)

    return private_key, address, account_info, message