# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:50:24 2016

@author: nick
"""
import ephem
import pandas as pd
from datetime import datetime

def getmoonphase(date):
    m = ephem.Moon(date)
    return m.phase
    
sectors = ('XLY','XLF', 'XLK', 'XLE', 'XLV', 'XLI', 'XLP', 'XLU', 'XLB', 'SPY')

constellist = ('Aries', 'Taurus','Gemini','Cancer','Leo','Virgo','Libra', 'Scorpio',
               'Ophiuchus', 'Sagittarius', 'Capricornus', 'Aquarius', 'Pisces', 'Sextans')
planets = ('mercury','saturn','jupiter','neptune','uranus','venus','mars','moon','sun')

def get_planets():
    data = pd.read_csv('sixyearsconstelldata.txt')
    return data
    
def get_sunandmoon():
    data = pd.read_csv('sixyearssunmoonedata.txt')
    return data
def planet_constell(date):
    data = ""
    planets = (ephem.Mars(date), ephem.Mercury(date), ephem.Saturn(date), ephem.Jupiter(date),
               ephem.Neptune(date), ephem.Uranus(date), ephem.Venus(date), ephem.Moon(date), ephem.Sun(date))
    for x in range(0,len(planets)):      
        data += (ephem.constellation(planets[x])[1]+",")
    return data
def get_distplanets():
    data = pd.read_csv('sixyearsdistancedata.txt')
    return data
def sun_moonFrame():
    data= pd.read_csv('sixyearssunmoondata.txt')
    return data
def getreturnsFrame(symbol):
    data = pd.read_csv(symbol+'returnsandvol.txt') 
    return data

def get5Frame(symbol):
    data = pd.read_csv(symbol+'5dayrolling.txt') 
    return data

def get13Frame(symbol):
    data = pd.read_csv(symbol+'13dayrolling.txt') 
    return data

def get28Frame(symbol):
    data = pd.read_csv(symbol+'28dayrolling.txt') 
    return data
    
def planet_constell(date):
    data = ""
    planets = [ephem.Mars(date), ephem.Mercury(date), ephem.Saturn(date), ephem.Jupiter(date),
               ephem.Neptune(date), ephem.Uranus(date), ephem.Venus(date), ephem.Moon(date), ephem.Sun(date)]
    for x in range(0,len(planets)):      
        data += (ephem.constellation(planets[x])[1]+",")
    return data
    
def get28up():
    data = pd.read_csv('up13x28.txt') 
    return data
    
def get13up():
    data = pd.read_csv('up5x13.txt') 
    return data
    
def crossoverfull13(symbols):
    d = get13up()
    with open('crossover513.txt', 'w') as f:
        count = 0
        f.write('ID,symbol,date,mars,mercury,saturn,jupiter,neptune,uranus,venus,moon,sun\n')
        for i in d.iterrows():
            date = i[1]['date']
            print date
            sym = i[1]['symbol']
            plan = planet_constell(date)[:-1]
            f.write('%d,%s,%s,%s\n' %(count,sym,date,plan))
            count +=1


def crossoverfull28(symbols):
    d = get28up()
    with open('crossover1328.txt', 'w') as f:
        count = 0
        f.write('ID,symbol,date,mars,mercury,saturn,jupiter,neptune,uranus,venus,moon,sun\n')
        for i in d.iterrows():
            date = i[1]['date']
            print date
            sym = i[1]['symbol']
            plan = planet_constell(date)[:-1]
            f.write('%d,%s,%s,%s\n' %(count,sym,date,plan))
            count +=1
#crossoverfull13(sectors)
#crossoverfull28(sectors)    
            
def getreturnsFrame5(symbol):
    data = pd.read_csv(symbol+'returns5day.txt') 
    return data
    
def getreturnsFrame30(symbol):
    data = pd.read_csv(symbol+'returns30day.txt') 
    return data

def getcloseFrame(symbol):
    data = pd.read_csv(symbol+'close.txt')    
    return data

def plusonereturns(symbol):
    dataf = getreturnsFrame(symbol)    
    for k in dataf.iterrows():
        if k[1]['returns']>1:
            for k2 in planetframe.iterrows():
                if k2[1]['date'] == k[1]['date']:
                    print k2[1]['moon']
def moonconst(date):
    s = ephem.Moon(date)
    return ephem.constellation(s)[1]
def sunconst(date):
    s = ephem.Sun(date)
    return ephem.constellation(s)[1]                    
def cross_5_12(symbols):
    for symbol in symbols:
        frame13 = get13Frame(symbol)
        frame5 =  get5Frame(symbol)
        


                 
def matvind():
    mat = getreturnsFrame('XLB')
    ind = getreturnsFrame('XLI')
    t = 0
    c = 0
    for k in range(0, len(mat)):
        if mat.ix[k]['returns'] < 0.314:
            t += ind.ix[k]['returns']
            c += 1
    print (t/c)
    
    
def ma_13(df):
    for k in df.iterrows():
        closeseries = df[0:k[0]]['close']
        ma13 = pd.rolling_mean(closeseries, 13)
    short = float(ma13.tail(1).values)
    return short

def ma_5(df):
    for k in df.iterrows():
        closeseries = df[0:k[0]]['close']
        ma = pd.rolling_mean(closeseries, 5)
    val = float(ma.tail(1).values)
    print val
    
def ma_28(df):
    for k in df.iterrows():
        closeseries = df[0:k[0]]['close']
        ma = pd.rolling_mean(closeseries, 55)
    val = float(ma.tail(1).values)
    return val
    
def avg100dayvol(df, date):
    for k in range(0, len(df)):
        if df.ix[k]['date'] == date:
            closeseries = df[k:k+100]['volume']
            ma = pd.rolling_mean(closeseries, 100)
            val = float(ma.tail(1).values)
            return val
    

#planetdist = pd.read_csv('sixyearsdistancedata.txt')


def movingavxconstells(dataf):
    movingup = False
    cancercount = 0
    xup = 0
    xdown = 0
    for x in range(2, len(dataf)):
        if ma_55 != 'nan':
            if ma_13(dataf[:x])>ma_55(dataf[:x]):
                if movingup == False:
                    movingup = True
                    xup += 1
                    if planetframe.ix[x]['moon'] == 'cancer':
                        cancercount +=1
            else:
                if movingup == True:
                    movingup = False
                    xdown += 1
    return (float(cancercount)/xup)*100
            
def movingavxdist(dataf):
    movingup = False
    cancercount = 0
    for x in range(14, len(dataf)):
        if ma_55 != 'nan':
            if ma_13(dataf[x-1:x])>ma_55(dataf[:x]):
                if movingup == False:
                    movingup = True
                    print 'crossover date: %s' % (planetdist.ix[x]['date'])
                    print planetdist.ix[x]
            else:
                if movingup == True:
                    movingup = False
                    print 'crossunder: %s' % (planetdist.ix[x]['date'])
                    print planetdist.ix[x]

def avgprint(dataf):
    for x in range(14, len(dataf)):
        ma_5(dataf[x-1:x])
        
        
def moonlibrareturns(symbol):
    techre = getreturnsFrame(symbol)    
    total = 0
    count = 0
    for x in range(0, len(techre)):
        if planetframe.ix[x]['moon'] == 'Leo':
            total += float(techre.ix[x]['returns'])
            count += 1
    print "avg returns for %s: %f" %(symbol,(total/count))
def close5daycross(symbols):
    with open('closex5.txt', 'w') as f:
        count = 1
        f.write('ID,symbol,date,mars,mercury,saturn,jupiter,neptune,uranus,venus,moon,sun\n')
        for symbol in symbols:
            crossx = False
            closeframe = getcloseFrame(symbol)
            avg = get5Frame(symbol)
            avgcount = 1
            for x in range(0,len(closeframe)):
                if closeframe.ix[x]['date'] == avg.ix[avgcount]['date']:
                    date = closeframe.ix[x]['date']
                    if (closeframe.ix[x]['close'] > avg.ix[avgcount]['avg']):
                        if crossx == False:
                            f.write('%d,%s,%s,%s\n' % (count,symbol,date,planet_constell(date)[:-1]))
                            count += 1
                            crossx = True
                    if closeframe.ix[x]['close'] < avg.ix[avgcount]['avg']:
                            crossx = False
                    avgcount+=1
            print "%s written" %(symbol)
def cross5x13(symbols):
    with open('crossover513.txt', 'w') as f:
        count = 1
        f.write('ID,symbol,date,mars,mercury,saturn,jupiter,neptune,uranus,venus,moon,sun\n')
        for symbol in symbols:
            crossx = False
            closeframe = get5Frame(symbol)
            avg = get13Frame(symbol)
            avgcount = 1
            for x in range(0,len(closeframe)):
                if closeframe.ix[x]['date'] == avg.ix[avgcount]['date']:
                    date = closeframe.ix[x]['date']
                    if (closeframe.ix[x]['close'] > avg.ix[avgcount]['avg']):
                        if crossx == False:
                            f.write('%d,%s,%s,%s\n' % (count,symbol,date,planet_constell(date)[:-1]))
                            count += 1
                            crossx = True
                    if closeframe.ix[x]['close'] < avg.ix[avgcount]['avg']:
                            crossx = False
                    avgcount+=1
            print "%s written" %(symbol)
#cross5x13(sectors)
def closecross():
    data = pd.read_csv('closex5.txt')
    with open('countclosecross.txt', 'w') as f:
        ID = 0
        f.write('ID,symbol,planet,constell,count,percent\n')
        for sym in sectors:
            for plan in planets:
                for cons in constellist:
                    total = 0
                    count = 0
                    for i in range(0,len(data)):
                        if data.ix[i]['symbol'] == sym:
                            if data.ix[i][plan] == cons:
                                count+=1
                                total+=1
                            else:
                                total+=1
                    perc = (float(count)/float(total))*100
                    print total
                    f.write('%d,%s,%s,%s,%d,%f\n' % (ID,sym,plan,cons,count,perc))
                    ID+=1
    
closecross()            
def cross513():
    data = pd.read_csv('crossover513.txt')
    with open('countclosecross513.txt', 'w') as f:
        ID = 0
        f.write('ID,symbol,planet,constell,count,percent\n')
        for sym in sectors:
            for plan in planets:
                for cons in constellist:
                    total = 0
                    count = 0
                    for i in range(0,len(data)):
                        if data.ix[i]['symbol'] == sym:
                            if data.ix[i][plan] == cons:
                                count+=1
                                total+=1
                            else:
                                total+=1
                    perc = (float(count)/float(total))*100
                    print total
                    f.write('%d,%s,%s,%s,%d,%f\n' % (ID,sym,plan,cons,count,perc))
                    ID+=1
def cross1328():
    data = pd.read_csv('crossover1328.txt')
    with open('countclosecross1328.txt', 'w') as f:
        ID = 0
        f.write('ID,symbol,planet,constell,count,percent\n')
        for sym in sectors:
            for plan in planets:
                for cons in constellist:
                    total = 0
                    count = 0
                    for i in range(0,len(data)):
                        if data.ix[i]['symbol'] == sym:
                            if data.ix[i][plan] == cons:
                                count+=1
                                total+=1
                            else:
                                total+=1
                    perc = (float(count)/float(total))*100
                    print total
                    f.write('%d,%s,%s,%s,%d,%f\n' % (ID,sym,plan,cons,count,perc))
                    ID+=1
                    
cross1328()
cross513()

# needs to be switched to the same func as close5daycross
def cross13x28(symbols):
    with open('crossover1328.txt', 'w') as f:
        count = 1
        f.write('ID,symbol,date,mars,mercury,saturn,jupiter,neptune,uranus,venus,moon,sun\n')
        for symbol in symbols:
            crossx = False
            closeframe = get13Frame(symbol)
            avg = get28Frame(symbol)
            avgcount = 1
            for x in range(0,len(closeframe)):
                if closeframe.ix[x]['date'] == avg.ix[avgcount]['date']:
                    date = closeframe.ix[x]['date']
                    if (closeframe.ix[x]['close'] > avg.ix[avgcount]['avg']):
                        if crossx == False:
                            f.write('%d,%s,%s,%s\n' % (count,symbol,date,planet_constell(date)[:-1]))
                            count += 1
                            crossx = True
                    if closeframe.ix[x]['close'] < avg.ix[avgcount]['avg']:
                            crossx = False
                    avgcount+=1
            print "%s written" %(symbol)
#cross5x13(sectors)
#cross13x28(sectors)      
 

    
       
def planconsreturns(symbollist, planetlist, constels):
    with open('plancons5day.txt', 'w') as f:
       planetframe = pd.read_csv('sixyearsconstelldata.txt')
       row = 1 
       f.write("ID,symbol,planet,constell,avg\n")       
       for symbol in symbollist:
           returns = getreturnsFrame5(symbol) 
           for plan in planetlist:
               for const in constels:
                   total = 0.0
                   count = 0
                   for x in range(0, len(returns)):
                       if planetframe.ix[x][plan] == const:
                           #if planetframe.ix[x]['neptune'] == 'Taurus':
                           total += float(returns.ix[x]['returns'])
                           count += 1
                   if count > 0: #catch instances where the planet wasn't in that const for the whole six years
                      f.write("%d,%s,%s,%s,%f\n" %(row,symbol, plan, const,(total/count)))
                      row+=1
                   else:
                      f.write("%d,%s,%s,%s,%f\n" %(row,symbol,plan,const,total))
                      row +=1
def moonphasereturns(symbol):
    techre = getreturnsFrame(symbol) 
    for x in range(0, len(techre)):
        total = 0.0
        count = 0
        if techre.ix[x]['returns'] > 1:
            #if planetframe.ix[x]['neptune'] == 'Taurus':
            d = techre.ix[x]['date']
            total += getmoonphase(d)
            count += 1
#planconsreturns(sectors, planets, constellist)
'''def samesunandmoon(symbols):
    with open('sunmoonmatching.txt', 'w') as f:
        f.write("ID, symbol, constell, avgreturns\n")
        for symbol in symbols:'''
            
        
        
def highreturntuple(symbol):
    pf = pd.read_csv('sixyearsconstelldata.txt')
    blood = getreturnsFrame(symbol)
    count = 0
    highp = ''
    highc = ''
    highr = []
    tucount = 0 
    for i in range(0, len(blood)):
        if blood.ix[i]['returns']>1:
            count += 1
            for p in planets:
                for c in constellist:
                    if pf.ix[i][p] == c:
                        highr.append((p,c))
    for p in planets:            
        for c in constellist:
            x = highr.count((p,c)) 
            if x > tucount:
                tucount = x
                highp = p
                highc = c
    perc = (float(tucount)/count)*100
    print " %s has most high return days when %s is in %s" % (symbol, highp,highc)
    print "%f percent of the high return days %s is in %s %s has high returns" % (perc, highp, highc, symbol)
                     

        
'''
def volstudy(symbol):
    volf = getcloseFrame(symbol)
    future = returns5dayforward(symbol)
    for x in range(0, len(volf)):
        total = 0
        count = 0
        d = volf.ix[x]['date']
        if volf.ix[x]['volume'] > avg100dayvol(volf, d):
            total += future.ix[x]['returns']
            count +=1
    if count > 0:
        avg = (total/count)
        print "%s: had an avg of %f 5day return after breaching 100 moving average volume" %(symbol, avg)

for symbol in sectors: 
    highreturntuple(symbol)
'''
        
