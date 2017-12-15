import treePlotter
import trees

myData,labels = trees.createDataSet()
inTree = trees.createTree(myData,labels)
print(list(inTree.keys())[0])
treePlotter.createPlot(inTree)
