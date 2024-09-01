# Michael Rizig
# CS7247 Machine Learning
# Professor Xing
# 8/31/24
# Assignment 1: K-means

# import plot and math tools
import matplotlib as plot
import seaborn as sea
import numpy
import random

#function to create initial predefiend number of cluster centers (K) with data passed
#data is a list of lists
def createClusters(numberOfClusters,data):
# create list to store cluster means
    clusterCenters = []
    #pick random values as clusters
    for i in range (numberOfClusters):
        x = random.randint(0,len(data))
        clusterCenters.append(data[x])
    return clusterCenters

#group data into clusters based on distance from each cluster center
def groupData(clusterCenters,data):
    
    # list to assign groupings
    groupings = []
    
    #debug
    print("Randomly chosen cluster centers: ",clusterCenters)
    
    for x in data:
        distances=[]
        for cluster in clusterCenters:
            distance=0
            for i in range(len(cluster)):
                distance += numpy.sqrt((cluster[i]-x[i])**2)
            distances.append(distance)
        #assign the closest cluster center as group
        groupings.append((x,distances.index(min(distances))))

       
    #debug
    print("Grouping for each value set: ",groupings)
    return clusterCenters,groupings

#this function takes in current groupings, finds average of all values in each group
#then recalls group data to new center clusters.
def recenterGroupings(groupings):
    pass

#helper function for parseCSV
#checks if data is float in string format or not float
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
# takes in string path of csv file and returns all numeric values as list of lists
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
        values.append([float(i) for i in out])
    #return list of values list
    return values

#print(parseCSV("G:\KSU\CS7267-Machine Learning\Assignments\Project 1 - Unsupervised Learning\Data\iris.csv"))
data = parseCSV("C:\CS7247\Machine-Learning-Projects-Python\Project 1 - Unsupervised Learning\Data\iris.csv")
clusterCenters = createClusters(3,data)
clusters,groupings = groupData(clusterCenters,data)
print(groupings)