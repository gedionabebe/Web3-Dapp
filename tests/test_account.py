import sys
sys.path.insert(0,'../scripts/')
from scripts.create_account import create_account
from scripts.create_nft import create_NFT
from scripts.asset_optin import asset_optin
from scripts.asset_transfer import asset_transfer


def test_account_create():
    account = create_account()
    assert account[3] != None

def test_create_NFT():
    NFT = create_NFT
    assert NFT !=None
def test_asset_optin():
    optin = asset_optin
    assert optin != None
def test_asset_transfer():
    transfer = asset_transfer
    assert transfer !=None