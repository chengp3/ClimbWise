def getMissingCounts(li):
    allstyles = set(['Face','Overhang','Crack','Not Categorized'])
    set1 = set(li)
    return list(sorted(allstyles - set1))

def backfillCounts(incompleteDict, missingli):
    for label in missingli:
        incompleteDict[label] = 0
    return incompleteDict

def regularizeCounts(df):
    incompleteDict = df['style'].value_counts().to_dict()
    missingLi = getMissingCounts(incompleteDict.keys())
    backfillCounts(incompleteDict,missingLi)
    return incompleteDict

def labelsAndCounts(di):
    labels = sorted(list(di.keys()))
    counts = [di[ele] for ele in labels]
    return labels, counts

#ten = tickdf[['grade','style']][tickdf.grade.str.match(r'(^5.10.*)')==True]
#ele = tickdf[['grade','style']][tickdf.grade.str.match(r'(^5.11.*)')==True]
#twelve = tickdf[['grade','style']][tickdf.grade.str.match(r'(^5.12.*)')==True]

#tendict = regularizeCounts(ten)
#eledict = regularizeCounts(ele)
#twelvedict = regularizeCounts(twelve)
alldict = regularizeCounts(tickdf[['grade','style']])

#tenlabels, tencounts = labelsAndCounts(tendict)
#elelabels, elecounts = labelsAndCounts(eledict)
#twelvelabels, twelvecounts = labelsAndCounts(twelvedict)
alllabels, allcounts = labelsAndCounts(alldict)