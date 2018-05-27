#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:41:23 2018

@author: chavdar
"""
from webscrape import *
import time
import sys
import numpy as np
url = "https://ethereumprice.org/live/"
if len(sys.argv)!=1:
    fetchInterval = float(sys.argv[1])
else:
    fetchInterval = 3.0
if __name__ == "__main__":
    while True:
        w.getHtml(url)
        res = w.getElementsOfType("span","ep-price")
        res = res[1].split(">")[1].split("<")[0]
        
        data = np.array([res])
        np.save("./data/eth_avg",data)
        
def getEthAverage():
    w = Webscraper()
    url = "https://ethereumprice.org/live/"
    w.getHtml(url)
    res = w.getElementsOfType("span","ep-price")
    res = res[1].split(">")[1].split("<")[0]
    
    data = np.array([res])
    np.save("./data/eth_avg",data)
    return res