import sys
sys.path.insert(0,'../scripts/')
from create_account import create_account


def test_account_create():
    account = create_account()
    assert account[3] != None