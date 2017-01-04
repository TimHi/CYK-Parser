import numpy as np 
import os
from grammar import rules







array = np.zeros([4, 4], int)
array[1][0] = 2
print(array)










#	for downCounter in range(heightDownIndexLoop):
#			print("ZWEITER LOOP")
#			#Straight down
#			#Length of loop is the same
#
#			tempSign = array[currentLength][heightDownIndex]
#			print("tempSign: ", tempSign)
#			print("Von Stelle: ", currentLength, heightDownIndex)
#			possibleProductions.append(tempSign)
#			print(currentHeight, ". Reihe")
#			print(possibleProductions)
#			heightDownIndex = heightDownIndex - 1
#		for diagLength in range(heightDiagLoop):
#			print("DRITTER LOOP")
#			#Diag up
#			dum = 0
#	print("---------------------END---------------------------------")










































#def findFinalRules(charItem):
#	rulesFound = []
#	#charItem: ['CB, CF']
#	#rule: AB
#	print(len(charItem))
#	print("--comblist-")
#	print(charItem)
#	print(len(charItem))
#	for f in range(len(charItem)):
#		tempS = charItem[f]
#		print(tempS)
#		
#		for h,k in rules.items():
#			for rule in k:
#				if rule == tempS:
#					rulesFound.append(h)
#
#	return rulesFound


#combList = ['CD']
#print("combList: ", combList)
#foundC = findFinalRules(combList)
#print("----------")
#print(foundC)
#posList=[]
#tmpC = ['E', 'R']


#max = 1
#indexList = 0

#possible: [['A'], ['C']]
#tempD: ['E', 'B']
#Er checkt jetzt AEB
#Muss aber AE und dann AB checken

#Erweitert: 
#possible: [['A' 'C'] , ['B']]
#tempD:[['E', 'B'], ['C', 'A'], ['B']]

#mylist = [1,2,3,4]
#print len(mylist)
#4
#cbcb
#B,E | D | B,E | D



#for u in range(len(posList)):
#	indexG = len(posList[u])
#	indexD = len(tmpC) 
#	for i in range(len(tmpC)):
#		for o in range(indexG):
#			tempJ = posList[u][o]
#			tempK = tmpC[i] 
#			#print("j", tempJ, "k", tempK)
#			checkC = ''.join(item for item in posList[u][o] + tmpC[i])
#			#checkC = ''.join(item for item in posList[u][1] + tmpC[i])
#			combList.append(checkC)
#			print(combList)
#			foundC = findFinalRules(combList)
#			print(foundC)
#			
#
#print(tmpC[1])
#checkC = ''.join(item for item in posList[indexList] + tmpC)
#print(combList)