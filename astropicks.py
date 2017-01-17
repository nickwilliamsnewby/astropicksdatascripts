# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
from yahoo_finance import Share
import ephem
import datetime as dt 

def nextnewmoon(date):
    m = ephem.Moon.phase(date)
    return m

indexplanets = ['Mars', 'Mercury', 'Saturn', 'Jupiter', 'Neptune', 'Uranus',
    'Venus','Moon','Sun']

sectors = ['XLY','XLF', 'XLK', 'XLE', 'XLV', 'XLI', 'XLP', 'XLU', 'XLB']


def get_history(symbol):
    stock = Share(symbol).get_historical('2015-01-04', '2016-01-01')
    return stock

def getdateints(date):
    ints = []
    ints.append(int(date[:4]))
    ints.append(int(date[5:7]))
    ints.append(int(date[8:10]))
    return ints

    
def change(x,y):
    return (y-x)
    
    

def planet_constell(date):
    positions = {}
    planets = [ephem.Mars(date), ephem.Mercury(date), ephem.Saturn(date), ephem.Jupiter(date),
               ephem.Neptune(date), ephem.Uranus(date), ephem.Venus(date), ephem.Moon(date), ephem.Sun(date)]
    for x in range(0,len(planets)):
        positions[indexplanets[x]]= ephem.constellation(planets[x])
    return positions       



def dateparse(date):
    return date.replace('-','/')


def dailyreturns(stocks):
    master = {}
    for symbol in stocks:
        hist = get_history(symbol)
        results = {}
        for i in range(0, len(hist)):
            date = dateparse(hist[i]["Date"])
            constells = planet_constell(date) 
            returns = change(float(hist[i]['Open']),float(hist[(i)]['Adj_Close']))
            results[hist[i]["Date"]] = {'returns': returns, 'positions': constells}
        master[symbol] = results
        '''with open(symbol+'positive.txt', 'w') as f:
            f.write(str(positive))'''
    return master


def print_frames(inputdict):
    df = pd.DataFrame.from_dict(inputdict, orient='index')
    print df
def get_frames(stockdata):
    d = dailyreturns(stockdata)
    df = pd.DataFrame.from_dict(d, orient = 'index')
    return df
m = dailyreturns(sectors)
def get_list_positive_constells(data):
    constell_list = []
    for k in data:
        if data[k]["returns"] > 0:
            constell_list.append(data[k]["positions"])
    return constell_list
#pos_planet = get_list_positive_constells(m['XLE'])       
#print pos_planet

'''for x in pos_planet:
    count = pos_planet.count(x)
    print x+":"+count'''    
#print_frames(master['XLY'])

