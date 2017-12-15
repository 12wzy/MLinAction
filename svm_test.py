import svmMLiA

dataArr,labelArr = svmMLiA.loadDataSet('machinelearninginaction/Ch06/testSet.txt')

def main():
    print(labelArr)

if __name__ == '__main__':
    main()