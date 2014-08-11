import os
from buttercoin.client import ButtercoinClient

__author__ = 'kadams'

_client = None
public_key = None
secret_key = None


def _initialize_client_from_environment():
    global _client, public_key, secret_key, mode

    if _client is None:
        # check environment for project ID and keys
        public_key = public_key or os.environ.get("BUTTERCOIN_PUBLIC_KEY")
        secret_key = secret_key or os.environ.get("BUTTERCOIN_SECRET_KEY")
        mode = mode or os.environ.get("BUTTERCOIN_MODE")

        _client = ButtercoinClient(public_key=public_key,
                                   secret_key=secret_key,
                                   mode=mode)

def get_ticker(timestamp=None):
    _initialize_client_from_environment()
    return _client.get_ticker(timestamp=timestamp)

def get_orderbook(timestamp=None):
    _initialize_client_from_environment()
    return _client.get_orderbook(timestamp=timestamp)

def get_key(timestamp=None):
    _initialize_client_from_environment()
    return _client.get_key(timestamp=timestamp)

def get_balances(timestamp=None):
    _initialize_client_from_environment()
    return _client.get_balances(timestamp=timestamp)

def get_deposit_address(timestamp=None):
    _initialize_client_from_environment()
    return _client.get_deposit_address(timestamp=timestamp)

def get_orders(body={}, timestamp=None):
    _initialize_client_from_environment()
    return _client.get_orders(body=body, timestamp=timestamp)

def get_order_by_id(order_id, timestamp=None):
    _initialize_client_from_environment()
    return _client.get_order(order_id, timestamp=timestamp)

def get_order_by_url(url, timestamp=None):
    _initialize_client_from_environment()
    return _client.get_order_by_url(url, timestamp=timestamp)

def get_transactions(body={}, timestamp=None):
    _initialize_client_from_environment()
    return _client.get_transactions(body=body, timestamp=timestamp)

def get_transaction_by_id(transaction_id, timestamp=None):
    _initialize_client_from_environment()
    return _client.get_transaction_by_id(transaction_id, timestamp=timestamp)

def get_transaction_by_url(url, timestamp=None):
    _initialize_client_from_environment()
    return _client.get_transaction_by_url(url, timestamp=timestamp)

def create_order(data={}, timestamp=None):
    _initialize_client_from_environment()
    return _client.create_order(data=data, timestamp=timestamp)

def create_deposit(data={}, timestamp=None):
    _initialize_client_from_environment()
    return _client.create_deposit(data=data, timestamp=timestamp)

def create_withdrawal(data={}, timestamp=None):
    _initialize_client_from_environment()
    return _client.create_withdrawal(data=data, timestamp=timestamp)

def send_bitcoin(data={}, timestamp=None):
    _initialize_client_from_environment()
    return _client.send_bitcoin(data=data, timestamp=timestamp)