## main program base libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from contextlib import closing
import csv
import io
from colorama import init
from colorama import Fore, Back, Style, Cursor
from datetime import datetime
import os
import threading
import time
import sys
from itertools import cycle
import netaddr
import resource as res


import pprint
import datetime as dt

## eos node libraries
import eospy.cleos
import eospy.keys
from eospy.types import Abi, Action
from eospy.utils import parse_key_file

## utils
import pytz
import json
import subprocess

## eos node ibraries
from eospy.cleos import Cleos
from prettytable import PrettyTable
import random

## encryption eos libraries
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
import publish.config as conf



# Get random node
def randnode():
    lines = open('missions/nodes').read().splitlines()
    myline =random.choice(lines)
    return (myline)


## encrypt data using a ECC public key
def enc(options):
    return encrypt(options[0], options[1])

## decrypt data using a ECC privatekey
def dec(options):
    return decrypt(options[0], options[1])

## generate encryption keys
def genkeys(options):
    secp_k = generate_eth_key()
    print("Private : "+secp_k.to_hex())
    print("Public : "+secp_k.public_key.to_hex())

## send a message to a eos address
def send(options):
    addr2 = options[0]
    msg = options[1]

    # encrypt data with reveicer public address
    #encrypted = encrypt(private_key, public_key, message)

    ce = eospy.cleos.Cleos(url='https://'+randnode())

    arguments = {
        "from": conf.account,  # sender
        "to": addr2,  # receiver
        "quantity": '0.0001 EOS',  # In EOS
        "memo": msg,
    }
    payload = {
        "account": "eosio.token",
        "name": "transfer",
        "delay_sec": 0,
        "authorization": [{
            "actor": conf.account,
            "permission": "owner",
        }],
    }
# Converting payload to binary
    data = ce.abi_json_to_bin(payload['account'], payload['name'], arguments)
# Inserting payload binary form as "data" field in original payload
    payload['data'] = data['binargs']
# final transaction formed
    trx = {"actions": [payload]}
    trx['expiration'] = str(
        (dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    key = eospy.keys.EOSKey(conf.privkey)
    try:
        resp = ce.push_transaction(trx, key, broadcast=True)
        print(resp)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        pass
        print(e)



def claim_reward(options):
    objd = {}
    objd["dem-reward"]="dem-reward"
    objd["txhash"]=conf.account
    objd["issuer"]=options[3]
    objd["reward"]=option[4]
    objd["status"]="confirmed"
    # encrypt data with reveicer public address
    #encrypted = encrypt(private_key, public_key, message)

    ce = eospy.cleos.Cleos(url='http://api.pennstation.eosnewyork.io:7001')

    arguments = {
        "from": options[1],  # sender
        "to": options[2],  # receiver
        "quantity": '0.0001 EOS',  # In EOS
        "memo": json.dumps(objd),
    }
    payload = {
        "account": "eosio.token",
        "name": "transfer",
        "authorization": [{
            "actor": "eosio",
            "permission": "owner",
        }],
    }
# Converting payload to binary
    data = ce.abi_json_to_bin(payload['account'], payload['name'], arguments)
# Inserting payload binary form as "data" field in original payload
    payload['data'] = data['binargs']
# final transaction formed
    trx = {"actions": [payloade]}
    trx['expiration'] = str(
        (dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    key = eospy.keys.EOSKey(conf.privkey)
    resp = ce.push_transaction(trx, key, broadcast=True)
    print(resp)


MAX_THREADS = 1
scanfilter  = ''
ports = '80'
from time import perf_counter
#IPv4Network('0.0.0.0/255.255.255.0').prefixlen
lista = []
plist = {}


## Receive data from a eos address, decrypts if the messages are encrypted
def receive(options):
        addr = options[0]
        x = PrettyTable(["Issuer","Name","Description","Reward","Status"])
 
        ce = Cleos(url='https://api.eosrio.io')

        # Get account
        #get_acc=ce.get_account(addr)
        get_actions = ce.get_actions(addr)
        
        # decrypt data with your private key
        # decrypted = decrypt(private_key, public_key, encrypted);
        
        for x1 in get_actions["actions"]:
            try:
                x.add_row(["","",x1["action_trace"]["act"]["data"]["memo"][0:50],"",""])
            except:
                pass
    
        print(x) 


## publish mission in address location 
def publish_mission(options):
    objd = {}
    objd["deus-ex-machina"]="deus-ex-machina"
    objd["issuer"]=conf.account
    objd["desc"]=options[3]
    objd["reward"]=option[4]
    objd["status"]="pending"
    # encrypt data with reveicer public address
    #encrypted = encrypt(private_key, public_key, message)

    ce = eospy.cleos.Cleos(url='http://api.pennstation.eosnewyork.io:7001')

    arguments = {
        "from": conf.account,  # sender
        "to": options[2],  # receiver
        "quantity": '0.0001 EOS',  # In EOS
        "memo": json.dumps(objd),
    }
    payload = {
        "account": "eosio.token",
        "name": "transfer",
        "authorization": [{
            "actor": "eosio",
            "permission": "owner",
        }],
    }
# Converting payload to binary
    data = ce.abi_json_to_bin(payload['account'], payload['name'], arguments)
# Inserting payload binary form as "data" field in original payload
    payload['data'] = data['binargs']
# final transaction formed
    trx = {"actions": [payloade]}
    trx['expiration'] = str(
        (dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    key = eospy.keys.EOSKey(conf.privkey)
    resp = ce.push_transaction(trx, key, broadcast=True)
    print(resp)

## publish mission in address location 
def publish_data(options):
    objd = {}
    objd["dem-data"]="dem-data"
    objd["issuer"]=conf.account
    objd["desc"]=options[3]
    objd["reward"]=option[4]
    objd["status"]="pending"
    # encrypt data with reveicer public address
    #encrypted = encrypt(private_key, public_key, message)

    ce = eospy.cleos.Cleos(url='http://api.pennstation.eosnewyork.io:7001')

    arguments = {
        "from": options[1],  # sender
        "to": options[2],  # receiver
        "quantity": '0.0001 EOS',  # In EOS
        "memo": json.dumps(objd),
    }
    payload = {
        "account": "eosio.token",
        "name": "transfer",
        "authorization": [{
            "actor": "eosio",
            "permission": "owner",
        }],
    }
# Converting payload to binary
    data = ce.abi_json_to_bin(payload['account'], payload['name'], arguments)
# Inserting payload binary form as "data" field in original payload
    payload['data'] = data['binargs']
# final transaction formed
    trx = {"actions": [payloade]}
    trx['expiration'] = str(
        (dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    key = eospy.keys.EOSKey(conf.privkey)
    resp = ce.push_transaction(trx, key, broadcast=True)
    print(resp)

## Extend command usage instructions 
def ExtendCommands():
    commands = [["genkeys","genkeys"],["enc","enc 'message'"],["dec","dec 'message'"],["send", "example (send senderAddress receiverAddress msg)"], ["receive", "example (receive eosaddress)"],["publish_mission","publish issuer receiver description reward"],["publish_data","publish_data 'data' reward"],["claim_reward","claim_reward hash issuer reward"]]
    return commands

## Set module options
def coreOptions():
	options = [["address", "set your EOS address", "aaaaaaaaaaaa"], ["channels", "set your address channels, separated by , ", "1"],
	 ["filter", "set filter words", "1"]]
	return options

## Define core params
def core(moduleOptions):
	address = moduleOptions[0][2]
	channels = moduleOptions[1][2]
	s_filter  = moduleOptions[2][2]

	print("\033[1;34m"+"[*]"+"\033[0m"+channels)
