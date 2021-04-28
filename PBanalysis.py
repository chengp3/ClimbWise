from datetime import datetime

# small utility function to help sort the dates in grade dictionary
def Sort_Tuple(tup):  
    tup.sort(key = lambda x: x[0])  
    return tup 

# takes the tickdf and returns a dictionary of months with corresponding PB
def monthlyPBs(df):
    monthlyPBs = {} 
    for index, row in df.iterrows(): # for every climb in the df
        month = row.monthyear
        grade = row.gradekey
        
        if month not in monthlyPBs.keys(): # if it's the first climb of the month
            monthlyPBs[month] = grade # set the high of the month to the climb grade
        else: # if it's not the first
            highgrade = monthlyPBs[month] # get the current PB of the month to compare
            if grade > highgrade: # if the current PB is higher
                monthlyPBs[month] = grade # set a new current PB 

        if str(row.grade) in gradeToNum.keys():
            df.at[index, 'gradekey'] = gradeToNum[str(row.grade)]
        else:
            df.at[index,'gradekey'] = 0.0
    return monthlyPBs    

# takes a grade dictionary and returns a list of most recent PBs
def recentHighs(gradeDict):
    tickedMonths = list(gradeDict.keys())
    list.sort(tickedMonths)
    
    lastPB = 0.0
    recentGradeList = []
    
    for month in datefill: # for month in datefill
        if month in tickedMonths: # check if there is a tick logged for the month
            recentGradeList.append(gradeDict[month]) # if it is, get the grade 
            lastPB = gradeDict[month] # and set the most recent PB to the grade
        else:
            recentGradeList.append(lastPB) # if no tick logged for the month, just add the previous month's
    
    return recentGradeList

# takes a grade dictionary and returns a list of personal bests (PBs)
def maxGrades(gradeDict):
    highGradeList = []
    tickedMonths = list(gradeDict.keys())
    list.sort(tickedMonths)
    
    highGrade = 0.0
    for month in datefill: # for every month
        if month in tickedMonths: # check if there is a climbing grade in the ticked maxes
            grade = gradeDict[month]
            if grade > highGrade: # if that month's grade is a PBest
                highGrade = grade
                highGradeList.append(highGrade) # add it to the list
            else:
                highGradeList.append(highGrade) # otherwise add the old PBest
        else:
            highGradeList.append(highGrade) # if no climbs in that month, append old PBest
    return highGradeList

gradeToNum = {
    '5.0' : 0, 'easy' : 0, 'Easy' : 0, '5.1' : 1, '5.2' : 2, '5.3' :  3, '5.4' : 4,
    '5.5' : 5, '5.6' : 6, '5.7-' : 7, '5.7' : 7, '5.7+' : 7, '5.8-' : 8, '5.8' : 8, 
    '5.8+' : 8, '5.9-' : 9, '5.9' : 9, '5.9+' : 9,'5.10a' : 10, '5.10-' : 10, 
    '5.10a/b' : 10, '5.10b' : 11, '5.10b/c' : 12, '5.10' : 12, '5.10c' : 13, 
    '5.10d' : 14, '5.10+' : 14, '5.10c/d' : 14, '5.11a' : 15, '5.11-' : 15, '5.11a/b' : 15,
    '5.11b' : 16,'5.11b/c' : 17, '5.11' : 17, '5.11c' : 18, '5.11d' : 19, '5.11+' : 19, 
    '5.11c/d' : 19, '5.12a' : 20, '5.12-' : 20, '5.12a/b' : 20, '5.12b' : 21, '5.12b/c' : 22, 
    '5.12' : 22, '5.12c' : 23, '5.12d' : 24, '5.12+' : 24, '5.12c/d' : 24, '5.13a' : 25, 
    '5.13-' : 25, '5.13a/b': 25, '5.13b': 26, '5.13b/c': 27, '5.13': 27, '5.13c': 28, 
    '5.13d': 29, '5.13+': 29, '5.13c/d': 29, '5.14a': 30, '5.14-': 30, '5.14a/b': 30, '5.14b': 31,
    '5.14b/c': 32, '5.14': 32, '5.14c': 33, '5.14d': 34, '5.14+': 34, '5.14c/d': 34,
    '5.15a': 35, '5.15-': 35, '5.15a/b': 35, '5.15b': 36, '5.15b/c': 37, '5.15': 37, '5.15c': 38,
    '5.15d': 39, '5.15+': 39, '5.15c/d': 39, '5.16a': 40, '5.16-': 40, '5.16a/b': 40, '5.16b': 41,
    '5.16b/c': 41, '5.16': 41, '5.16c': 42
}

monthyear = []
gradekey = []

# take in a date string from tickdf and append a formatted date to monthyear list
def getMonthYear(datestring):
    string = datetime.strptime(datestring, '%b %d, %Y')
    month = string.strftime('%Y-%m')
    monthyear.append(month) # add monthyear value
    
def translateGrade(gradestring):
    if gradestring in gradeToNum.keys(): # also, for every tick, if the grade is in the translator
        grade = gradeToNum[gradestring] # insert the new gradekey in the column
        gradekey.append(grade)
    else:
        grade = -1 # if it's not in the translator it's probably an iceclimb or something, skip it
        gradekey.append(grade)

for index, row in tickdf.iterrows(): # for every tick in the ticklist
    datestring = row.date
    getMonthYear(datestring)

    gradestring = str(row.grade)
    translateGrade(gradestring)
        
tickdf['monthyear'] = monthyear
tickdf['gradekey'] = gradekey

monthlyPBs = monthlyPBs(tickdf)
highlist = list(monthlyPBs.items())

highlist = Sort_Tuple(highlist)
datefill = pd.date_range(highlist[0][0],highlist[-1][0], freq='MS').strftime("%Y-%m").tolist()
# datefill contains a regularly periodic list of months from earliest tick to last tick