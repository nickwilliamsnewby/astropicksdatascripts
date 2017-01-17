# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:30:39 2016

@author: nick
"""
import pandas as pd
from yahoo_finance import Share
import ephem
import datetime 
import pandas_datareader.data as web

start = datetime.datetime(2013, 1, 1)

end = datetime.datetime(2016, 1, 1)

def change(x,y):
    return ((y-x)/y)*100

sectors = ['XLY','XLF', 'XLK', 'XLE', 'XLV', 'XLI', 'XLP', 'XLU', 'XLB', 'SPY']
def datecorrect(date):
    result = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%d-%m')
    return result
def dateparse(date):
    return date.replace('-','/')

def get_history(symbol):
    stock = Share(symbol).get_historical('2010-01-04', '2016-01-01')
    return stock
    
def saturn_elong(date):
    s = ephem.Saturn(date)
    return ephem.constellation(s)

def saturnTilt(date):
    s = ephem.Saturn(date)
    return s.earth_tilt
    
def writefiles5day(stocks):
    for symbol in stocks:
        hist = get_history(symbol)
        with open(symbol+'returns5dayfor.txt', 'w') as f:
            f.write("date,returns,volume\n")
            for i in range(0, (len(hist)-5)):
                d = dateparse(hist[i]["Date"])
                s = saturn_elong(d)
                s2 = saturnTilt(d)
                returns = change(float(hist[i+5]['Close']),float(hist[(i)]['Close']))
                close = float(hist[i]['Close'])
                formattedLine = "%s,%f,%s\n" % (d, returns, hist[i]['Volume']) 
                f.write(formattedLine)
def writefiles1day(stocks):
    for symbol in stocks:
        hist = get_history(symbol)
        with open(symbol+'returnsandvol.txt', 'w') as f:
            f.write("date,returns,volume\n")
            for i in range(0, (len(hist)-5)):
                d = dateparse(hist[i]["Date"])
                s = saturn_elong(d)
                s2 = saturnTilt(d)
                returns = change(float(hist[i]['Open']),float(hist[(i)]['Close']))
                close = float(hist[i]['Close'])
                formattedLine = "%s,%f,%s\n" % (d, returns, hist[i]['Volume'])                 
                f.write(formattedLine)

def writefiles30day(stocks):
    for symbol in stocks:
        hist = get_history(symbol)
        with open(symbol+'returnsandvol30day.txt', 'w') as f:
            f.write("date,returns,volume\n")
            for i in range(0, (len(hist)-30)):
                d = dateparse(hist[i]["Date"])
                s = saturn_elong(d)
                s2 = saturnTilt(d)
                returns = change(float(hist[i+30]['Close']),float(hist[(i)]['Close']))
                close = float(hist[i]['Close'])
                formattedLine = "%s,%f,%s\n" % (d, returns, hist[i]['Volume'])                 
                f.write(formattedLine)



#writefiles5day(sectors)
#writefiles30day(sectors)
                
