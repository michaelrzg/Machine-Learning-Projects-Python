import matplotlib as plot
import seaborn as sns;
import numpy
import random

#function to create predefiend number of clusters (K) with data passed
#data is a list of lists
def createClusters(numberOfClusers,data):
    # create list to store cluster means
    clusterCenters = []
    #pick random values as clusters
    for i in range (numberOfClusers):
        x = random.randint(0,len(data))
        clusterCenters.append(data[x])
    # list to assign groupings
    groupings = []
    
    #debug
    print("Randomly chosen cluster centers: ",clusterCenters)
    
    for x in data:
        prevLowest=0
        lowest=0
        for center in clusterCenters:
            difference  = [i - j for i,j in zip(center,x)]
            if numpy.linalg.norm(numpy.array(center)-numpy.array(x)) < lowest:
                lowest = center

        if lowest!=prevLowest:
            groupings.append((x,center))
            prevLowest=lowest
    #debug
    print("Grouping for each value set: ",groupings)
    return clusterCenters,groupings

#helper function for parseCSV
def isFloat(x):
    #try to see if passed value is float
    try:
        float(x)
        #return true if this doesnt fail
        return True
    #if we get an exception , it means that value can not be converted to float, so it not one
    except: 
        #return false
        return False

#function to parse data from csv and return each set of values as list within list
def parseCSV(path):
    #open file
    file = open(path,'r',encoding='utf-8-sig')
    #place to store lines
    lines=[]
    #insert each line into lines list
    for x in file:
        lines.append(x)
    #place to store value lists
    values = []
    #split each line, then filter out non-numeric values
    for i in lines:
        x= i.split(",")
        out = [a for a in x if isFloat(a)]
        #insert into list
        values.append(out)
    #return list of values list
    return values

#print(parseCSV("G:\KSU\CS7267-Machine Learning\Assignments\Project 1 - Unsupervised Learning\Data\iris.csv"))

groupings,clusters = createClusters(3,parseCSV("G:\KSU\CS7267-Machine Learning\Assignments\Project 1 - Unsupervised Learning\Data\iris.csv"))
print(groupings)