import math
import numpy as np

assignedLabel=[]
training_set= []
test_set=[]

    
count=0
nTrn=1000
nTst=100
k=20


def classify(indexArr,x_tr):
    counter1=0
    counter2=0
    for l in range(0,k-1):
        index=indexArr[l]
        if(x_tr[index][14]==-1):
            counter1=counter1+1
        if(x_tr[index][14]==1):
            counter2=counter2+1
    return counter1>counter2

def calcDist(points1,points2):
    return math.sqrt(pow(points1 - points2),2)

def KNN(k,x_tr,x_tst):
    DistArr=[1500]
    indexArr=[1500]
    for i in range(0,nTst):
        for j in range(0,nTrn):
            dist=0
            for l in range(0,13):
                point1=x_tst[i][l]
                point2=x_tr[j][l]
                dist=dist+pow(point1-point2,2)
            DistArr.append(math.sqrt(dist))
            indexArr.append(j)
        zipped_lists=zip(DistArr,indexArr)
        sorted_pairs=sorted(zipped_lists)
        tuples = zip(*sorted_pairs)
        DistArr,indexArr = [ list(tuple) for tuple in  tuples]
        if(classify(indexArr,x_tr)):
            assignedLabel.append(-1)
        else:
            assignedLabel.append(1)
              
            
    
training_set=np.genfromtxt('TestData.csv',delimiter=',')

test_set=np.genfromtxt('TrainData.csv',delimiter=',')

KNN(k,training_set,test_set)
for i in range(0,nTst-1):
    if(assignedLabel[i]==test_set[i][14]):
        count=count+1
print("Accuracy: ",count*100/nTst,"%")   
        




            
                

        
    
    
    
    