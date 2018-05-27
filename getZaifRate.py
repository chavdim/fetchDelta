#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:59:17 2018

@author: chavdar
"""
import requests, sys
import json
import numpy as np

pair = "eth_jpy"
if len(sys.argv)!=1:
    fetchInterval = float(sys.argv[1])
else:
    fetchInterval = 3.0
if __name__ == "__main__":
    while True:
        response = requests.get('https://api.zaif.jp/api/1/last_price/{}'.format(pair))
        if response.status_code != 200:
            raise Exception('return status code is {}'.format(response.status_code))
        zaif_price = json.loads(response.text)
        np.save("./data/zaif_price",np.array([zaif_price]))
        time.sleep(fetchInterval)

def getZaifPrice():
    pair = "eth_jpy"
    response = requests.get('https://api.zaif.jp/api/1/last_price/{}'.format(pair))
    if response.status_code != 200:
        raise Exception('return status code is {}'.format(response.status_code))
    zaif_price = json.loads(response.text)['last_price']
    np.save("./data/zaif_price",np.array([zaif_price]))
    return zaif_price
    