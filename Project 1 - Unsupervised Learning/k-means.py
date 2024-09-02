# Michael Rizig
# CS7247 Machine Learning
# Professor Zongxing Xie
# 8/31/24
# Assignment 1: K-means

# import plot and math tools
import matplotlib.pyplot as plot
import seaborn as sea
import numpy
import random

#function to create initial predefiend number of cluster centers (K) with data passed
# Takes in number of clusters (K) and data
# returns random cluster centers from within dataset
def createClusters(numberOfClusters,data):
# create list to store cluster means
    clusterCenters = []
    #pick random values as clusters
    for i in range (numberOfClusters):
        x = random.randint(0,len(data))
        clusterCenters.append(data[x])
    return clusterCenters

# return size of each current group
def groupSizes(K,groupings):
     # create list to store size of each current group
    groupSizes = [0 for i in range(K)]
    # find sizes of each group TODO: Fit this into other loop somehow
    for i in groupings:
        groupSizes[i[1]]+=1
    return groupSizes

# group data into clusters based on distance from each cluster center
# takes in center of clusters and groups data into closest cluster center
def groupData(clusterCenters,data):
    
    # list to assign groupings
    groupings = []
    
    #debug
    print("Randomly chosen cluster centers: ",clusterCenters)
    # for eaach data point,
    # calculate the distance between that point and each center
    for x in data:
        #list to hold each distance
        distances=[]
        #parse through each cluster center
        for cluster in clusterCenters:
            #init distanceto 0
            distance=0
            # calculate distance :  sqrt( a^2 + b^2 + c^2...) 
            # and add
            for i in range(len(cluster)):
                distance += numpy.sqrt((cluster[i]-x[i])**2)
            #
            #add it list for final comparison 
            distances.append(distance)
        #assign the closest cluster center as group
        groupings.append((x,distances.index(min(distances))))

       
    #debug
    print("Grouping for each value set: ",groupings)
    return clusterCenters,groupings

#this function takes in current groupings, finds average of all values in each group
#then recalls group data to new center clusters.
def recenterGroupings(K,groupings):
    # create list to store average point of each group
    groupAverage = [[0 for i in range(len(groupings[0][0]))] for u in range(K)]
   
    Sizes = groupSizes(K,groupings)
    print(Sizes)
    # for each datapoint structure: ([x,y,z,...],group#),
    # go through each value in list [x,y,z,...], 
    # divide it by total # of comparable values (divide each x by total appearences of x in group)
    # and add that weighted value to its appropriate spot in group avreages
    # at end of loop, we have average point of each group 
    for datapoint in groupings:
        for i in range(len(datapoint[0])):
            groupAverage[datapoint[1]][i]+= datapoint[0][i] /Sizes[datapoint[1]]

    #debug        
    #print(groupAverage)

    # now regroup data
    newCenters, newGroupings = groupData(groupAverage,[i[0] for i in groupings])

    return newCenters,newGroupings

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

# MAIN: 

#print(parseCSV("G:\KSU\CS7267-Machine Learning\Assignments\Project 1 - Unsupervised Learning\Data\iris.csv"))
#parse Data
data = parseCSV("G:\KSU\CS7267-Machine Learning\Assignments\Project 1 - Unsupervised Learning\Data\iris.csv")

#generate K number of random cluster centers
clusterCenters = createClusters(3,data)

#group data based on random clusters
clusters,groupings = groupData(clusterCenters,data)

#print(groupings)
#find average of each data group, use that as new center, regroup based on average
newCenters,newGroupings = recenterGroupings(3,groupings)
#print new grouping
#print(groupSizes(len(newCenters),newGroupings))

colors = ["red","blue","green"]

plot.axes(projection='3d')
for duple in newGroupings:
    plot.scatter(duple[0][0],duple[0][1],duple[0][2], color=colors[duple[1]])
   

plot.title("Data without normalization:")
plot.show()
