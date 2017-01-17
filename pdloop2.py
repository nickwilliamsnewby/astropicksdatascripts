# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:27:45 2016

@author: nick
"""

import pandas as pd
from yahoo_finance import Share
import ephem
import datetime 
import pandas_datareader.data as web


def change(x,y):
    return ((y-x)/y)*100

sectors = ['SPY','''XLY','XLF', 'XLK', 'XLE', 'XLV', 'XLI', 'XLP', 'XLU', 'XLB''']

indexplanets = ['Mars', 'Mercury', 'Saturn', 'Jupiter', 'Neptune', 'Uranus',
    'Venus','Moon','Sun'] 


def datecorrect(date):
    result = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%d-%m')
    return result
def dateparse(date):
    return date.replace('-','/')

def get_history(symbol):
    stock = Share(symbol).get_historical('2010-01-04', '2016-01-01')
    return stock
    
def moonphase(date):
    s = ephem.Moon(date)
    return ephem.constellation(s)
    
def saturnconst(date):
    s = ephem.Saturn(date)
    return ephem.constellation(s)
def planet_constell(date):
    data = ""
    planets = (ephem.Mars(date), ephem.Mercury(date), ephem.Saturn(date), ephem.Jupiter(date),
               ephem.Neptune(date), ephem.Uranus(date), ephem.Venus(date), ephem.Moon(date), ephem.Sun(date))
    for x in range(0,len(planets)):      
        data += (ephem.constellation(planets[x])[1]+",")
    return data
def sun_moon_constell(date):
    data = ""
    planets = (ephem.Moon(date), ephem.Sun(date))
    for x in range(2):      
        data += (ephem.constellation(planets[x])[1]+",")
    return data    
def planet_dist(date):
    data = ""
    planets = (ephem.Mars(date), ephem.Mercury(date), ephem.Saturn(date), ephem.Jupiter(date),
               ephem.Neptune(date), ephem.Uranus(date), ephem.Venus(date), ephem.Moon(date), ephem.Sun(date))
    for x in range(0,len(planets)):
        p = planets[x]
        data += (str(p.earth_distance)+",")
    return data
def saturnTilt(date):
    s = ephem.Saturn(date)
    return s.earth_tilt
                
def writeplanetfiles():
    hist = get_history('XLF')
    with open('sixdistancedata.txt', 'w') as f:
        f.write("date,mars,mercury,saturn,jupiter,neptune,uranus,venus,moon,sun\n")
        for i in range(0, len(hist)):
            d = dateparse(hist[i]["Date"])
            f.write("%s,%s\n" %(d, planet_dist(d)[:-1]))
            
writeplanetfiles()
print planet_constell(2016/11/29)