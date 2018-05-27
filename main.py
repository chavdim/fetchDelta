#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:55:52 2018

@author: chavdar
"""

from main import *
from main2 import *
from main3 import *
import numpy as np
import time,sys

if len(sys.argv)!=1:
    sleepTime = float(sys.argv[1])
else:
    sleepTime = 3.0
    
try:
    datas = np.load("./data/deltas.npy")
except FileNotFoundError:
    datas=np.array([])
    np.save("./data/deltas",datas)
except:
    sys.exit()
if __name__ == "__main__":
    while True:
        try:
            ethAverage = float(getEthAverage())
            exchRate = float(getExchangeRate())
            zaifPrice = float(getZaifPrice())
            delta = round((exchRate*ethAverage)-zaifPrice,1)
            datas = np.append(datas,delta)
            np.save("./data/deltas",datas)
            print("delta: ",delta,"exch*ethAvg: ",
                  round(exchRate*ethAverage,1),"zaif: ",zaifPrice)
        except: 
            print("failed fetch")
            continue
        time.sleep(sleepTime)
        
        
