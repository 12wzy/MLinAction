import trees
import treePlotter
# 3.1

# myData,labels = trees.createDataSet()
# # print(trees.calcShannonEnt(myData))
# # print(trees.splitDataSet(myData,0,0))
# print(trees.chooseBestFeatureTosplit(myData))
# # list test
# test_l = [0,1,2,3,4,5]
# print(test_l[0:])
# print(test_l[:1])
# print(test_l[2:])
#
# print(test_l[2:5])

# 3.3
fr = open('Data/lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesTree = trees.createTree(lenses,lensesLabels)

treePlotter.createPlot(lensesTree)