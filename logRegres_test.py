import logRegres
from numpy import *

dataArr,labelMat = logRegres.loadDataSet()

weights = logRegres.stocGradAscent(array(dataArr),labelMat,)

logRegres.plotBestFit(weights)

