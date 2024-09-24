# Michael Rizig
# CS7247 Machine Learning
# Professor Zongxing Xie
# 9/24/24
# Assignment 2: K Nearest Neighbor - Data Analytics 

# this file generates some simple statistics for the project report

import statistics
# read in data from file to memory          
def readData(path):
    # open file in read only
    file = open(path,'r',encoding='utf-8-sig')     
    # create place to store each full line
    lines = []
    #parse each full line
    for line in file:
        lines.append(line[:-1])
    # create place to store each datapoint array
    output = []
    # for each full line, parse csv by spliting at ',', 
    # store each datapoint in output with last value (label) sperated
    # output[x] = ([x1,x2...x29],label)
    for datapoint in lines:
        x = datapoint.split(",")
        # convert each array into an array of float values, and duple it with the class label
        for i in range(len(x)-1):
            output.append(float(x[i]))
    return output
def analyze(data):
    N = len(data)
    minValue = min(data)
    maxValue= max(data)
    dataRange = maxValue-minValue
    print("Total values: ",N,"\nMaximum value: ",maxValue,"\nMinimum Value: ", minValue, "\nRange: ",dataRange)
# normalize the dataset
def normalizeData(data):
    # for each sample we find its max and min elements and divide each point by the range (max-min)
    Maximum = max(data)
    Minimum = min(data)
    output = []
    for x in data:
        output.append((x-Minimum)/(Maximum-Minimum))
    return output
data = readData("Data/wdbc.data.mb.csv")
analyze(data)
norm =normalizeData(data)
analyze(norm)
