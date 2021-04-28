import sqlite3 as sl
import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

con = sl.connect('my-test2.db')

# need to put these functions in a module somewhere

def getStatus(string):
    if string == '': return ''
    poss = {'Solo', 'TR', 'Follow', 'Lead', 'Lead / Onsight', 'Lead / Flash', 'Lead / Redpoint', 'Lead / Pinkpoint', 'Lead / Fell/Hung'}
    
    meta = re.split(r'\.', string)[0]
    if (meta not in poss): return ''
    return meta

def getLastPage(url):
    page = requests.get(url)
    tickSoup = BeautifulSoup(page.content, 'html.parser')
    li = tickSoup.find_all('a', class_ = 'no-click') # find the pagination elements
    noclick = [route.text for route in li]
    p = re.compile(r'\d+')
    for el in noclick:
        if p.findall(el):
            lastPage = p.findall(el)[1] # find the last page number
            break
    return int(lastPage)

def getPageURL(i, url):
    ext = '' if i == 1 else ('?page=%d' %i)
    url = url + ext
    return url

def getTickInfo(tick):
    url = tick['href']
    
    info = re.split(r'[·]',tick.find('i').text)
    date = info[0].strip()
    
    if len(info) > 1:
        status = getStatus(info[1].strip())
    else: 
        status = ''
        
    return (url, date, status)

def getPageTicks(url):
    pageTicks = []
    page = requests.get(url)
    tickSoup = BeautifulSoup(page.content, 'html.parser')
    userRoutes = tickSoup.find_all('a', class_ = 'route-row')
    
    for route in userRoutes:
        info = getTickInfo(route)
        pageTicks.append(info)
        
    return pageTicks

def getUserTicks(url):
    userTicks = []
    
    for i in range(1, getLastPage(url)+1):
        pageurl = getPageURL(i, url)
        pageTicks = getPageTicks(pageurl)
        userTicks+=pageTicks
        
    return userTicks

#get ticks from url x
#put them in db? or skip the db? skip the db. make a pandas dataframe with the necessary routes x
#might have to restructure the database x
#join the databases together x

# access my-test2.db with url index and get pertinent details of route in a tuple
def getRouteInfo(url):
    with con:
        data = con.execute('select rowid, name, grade, type, area, style from routes where url = "' + url + '"')
        for row in data:
            return row
        
# update the pandas df with the tuple
def insertInfo(url, row):
    tickdf.loc[tickdf['url'] == url, ['rowid','name','grade','type','area','style']] = row

# update every route in the ticklist
def updateTickList():
    i = 1
    for url in tickdf['url'].tolist():
        row = getRouteInfo(url)
        insertInfo(url, row)

tickdf = pd.DataFrame(getUserTicks('https://www.mountainproject.com/user/200200801/ryan-westby/ticks'))
tickdf = tickdf.rename(columns={0:'url',1:'date',2:'status'})
tickdf.set_index('url')
updateTickList()

# for incomplete grades backfill a middling grade
def cleanGrades(tickdf):
    tickdf.loc[tickdf['grade'] == 5.1, 'grade'] = '5.10b/c'
    tickdf.loc[tickdf['grade'] == 5.11, 'grade'] = '5.11b/c'
    tickdf.loc[tickdf['grade'] == 5.12, 'grade'] = '5.12b/c'
    return tickdf

# only care about sends... filters out boulders as byproduct because they don't start with "Lead"
def filterSends(tickdf):
    sendConditions = ['Lead / Onsight', 'Lead / Flash', 'Lead / Redpoint', 'Lead / Pinkpoint', 'Lead', 'Solo']
    tickdf = tickdf.loc[tickdf['status'].isin(sendConditions)] 
    return tickdf

tickdf = cleanGrades(tickdf)
tickdf = filterSends(tickdf)

tickdf = tickdf.replace(to_replace='None',value='Not Categorized')

# tickdf contains all the information necessary for analytics. just need to split off the data as necessary and plot