import json
import requests
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

value = 20
acc = ''

# Solidity source code
contract_source_code = requests.get('https://raw.githubusercontent.com/HackatumBestTeamEver/BlockchainStuff/master/contracts/myContract.sol').text

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:myContract']

# web3.py instance
w3 = Web3(HTTPProvider('http://localhost:8545'))

# get the account
def getAcc():
    global acc
    acc = w3.etc.accounts[-1];

# send data
def sendData():
    global acc
    contract_interface.downgrade(value, transact={'from': acc})