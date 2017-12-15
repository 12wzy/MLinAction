import kNN

from numpy import *
import operator

# 2.2
import matplotlib
import matplotlib.pyplot as plt

# 2.3
from os import listdir

group,labels = kNN.createDataSet()
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
testVector = kNN.img2vector('machinelearninginaction/Ch02/digits/testDigits/0_0.txt')

# print(group)
# print(labels)
# print(datingDataMat)
# print("=====I'm split line.==========")
# print(datingLabels[0:20])
# print(normMat)
# print(ranges)
# print("=====I'm split line.==========")
# print(minVals)
# print("=====I'm split line.==========")
print(testVector)

# 2.1
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        # print(sortedDistIndicies[i])
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

# 2.2
def matplot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.show()
def datingClassTest():
    hoRatio = 0.70
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" %(classifierResult,datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate us: %f" %(errorCount/float(numTestVecs)))


def main():
    # 2.1
    # print(classify0([1.2,1.2],group,labels,4))

    # 2.2
    # matplot()
    # datingClassTest()

    #2.3
    # print(listdir('machinelearninginaction\Ch02\digits\\trainingDigits'))
    kNN.handwritingClassTest()

if __name__ == '__main__':
    main()