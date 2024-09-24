# Michael Rizig
# CS7247 Machine Learning
# Professor Zongxing Xie
# 8/31/24
# Assignment 2: K Nearest Neighbor

# import plot and math tools
import matplotlib.pyplot as plot
import seaborn as sea
import statistics
import math
# this function assigns a group to each input datapoint
# data format: 
# data = [x1,x2...x613]
# Datapoint x ∈ Data = ([x1,x2,..x29], label)
# input format = [x1,x2...x29]
# output format = int 
def predict(input, k, data):
    # define list to store distances from input to all datapoints
    distances = []
    # for each datapoint in sample input, calculate its distance to all other points
    for datapoint in data:
        sum=0
        for i in range(len(input)-1):
            sum += (input[i]-datapoint[0][i])**2
        distances.append((math.sqrt(sum),datapoint))
    # sort list
    distances.sort(key=lambda x: x[0])
    # get k closest values
    kclosest = distances[:k]
    #debug
    #print("\n\ninput:",input, "closest:",kclosest)
    #tallay votes
    votes = []
    for value in kclosest:
        votes.append(value[1][1])
    # return the label with the highest votes (mode of set)
    return statistics.mode(votes)

def run(inputSet, trainingSet):
    # predetermined k values to run
    kvalues = [1,3,5,7,9,11,13]
    for k in kvalues:
        # tally for confusion matrix later
        correct=0
        error=0
        for datapoint in inputSet:
            # remove last value ()
            datapoint[0].pop()
            prediction = predict(datapoint[0],k,trainingSet)
            if(prediction != datapoint[1]):
                error+=1
            else:
                correct+=1
        print("K value: ", k , " Correct: " , correct, " Error: ", error, " Accuracy: " , (correct/(correct+error))*100 , "%")
    
                 
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
        output.append(([float(x[i]) for i in range(len(x)-2)],x[len(x)-1]))
    return output

# normalize the dataset
def normalizeData(data):
    # for each sample we find its max and min elements and divide each point by the range (max-min)
    for x in data:
        maxValue = max(x[0])
        minValue= min(x[0])
        for i in range (len(x[0])):
            x[0][i] = (x[0][i]-minValue)/(maxValue-minValue)  
    return data

def normalizeInput(input):
    maxValue = max(input)
    minValue = min(input)
    output=[]
    for x in input:
        output.append((x-minValue)/(maxValue-minValue))
    return output

# Main: -------------------------------------------------------------------------------------------------

# parse dataset:
dataset = normalizeData(readData("Data/wdbc.data.mb.csv"))

# define training and testing set ratio:
trainingSetCount = int(len(dataset) * .7)
testingSetCount = len(dataset)-trainingSetCount
# partition training set and testing set from full dataset:
trainingSet = dataset[:trainingSetCount]
testingSet = dataset[-testingSetCount:]
print(len(testingSet))
run(testingSet,trainingSet)