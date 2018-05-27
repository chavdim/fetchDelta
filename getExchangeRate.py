#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:16:46 2018

@author: chavdar

program for gettin usd jpy exchange rate from goodle search

"""


from webscrape import *
import time
import sys
import numpy as np

#w = Webscraper()
#search = "usd+jpy"
#w.getHtml("https://www.google.co.jp/search?q={}&oq={}&aqs=chrome..69i57.31606j0j1&sourceid=chrome&ie=UTF-8".format(search,search))
#exchange_rate = w.getElementsOfType(element_type = "div",contains = "dDoNo vk_bk")
#exchange_rate = exchange_rate[0].split(">")[1].split(" ")[0]
w = Webscraper()
search = "usd+jpy"
if len(sys.argv)!=1:
    fetchInterval = float(sys.argv[1])
else:
    fetchInterval = 60.0
if __name__ == "__main__":
    while True:
        w.getHtml("https://www.google.co.jp/search?q={}&oq={}&aqs=chrome..69i57.31606j0j1&sourceid=chrome&ie=UTF-8".format(search,search))
        exchange_rate = w.getElementsOfType(element_type = "div",contains = "dDoNo vk_bk")
        exchange_rate = exchange_rate[0].split(">")[1].split(" ")[0]
        print(exchange_rate)
        np.save("./data/usd_jpy",np.array([exchange_rate]))
        time.sleep(fetchInterval)
        
    
def getExchangeRate():
    w = Webscraper()
    search = "usd+jpy"
    w.getHtml("https://www.google.co.jp/search?q={}&oq={}&aqs=chrome..69i57.31606j0j1&sourceid=chrome&ie=UTF-8".format(search,search))
    exchange_rate = w.getElementsOfType(element_type = "div",contains = "dDoNo vk_bk")
    exchange_rate = exchange_rate[0].split(">")[1].split(" ")[0]
    np.save("./data/usd_jpy",np.array([exchange_rate]))
    return exchange_rate
    
    
    
    