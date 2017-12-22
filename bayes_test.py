import bayes
from numpy import *
import re

listOPosts,listClasses = bayes.loadDataSet()

# 4.5
# myVocabList = bayes.createVocabList(listOPosts)
# # print(myVocabList)
# word2vec = bayes.setOfWords2Vec(myVocabList,listOPosts[0])

# trainMat = []
# for postinDoc in listOPosts:
#     trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
# p0V,p1V,pAb = bayes.trainNB0(trainMat,listClasses)
# print(pAb)
# print(p0V)
# print(p1V)

# bayes.testingNB()

# 4.6
# mySent = ''
# mySent.split()
# regEx = re.compile('\\W*')
# listOfTokens = regEx.split(mySent)
error_rate = 0
for i in range(100):
    error_rate += bayes.spamTest()
print("average error rate is:",float(error_rate/100))