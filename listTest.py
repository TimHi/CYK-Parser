import numpy as np 
import os

def findRules(charItem):
	#Empty list to collect the rules found for the
	#Specific charItem
	rulesFound = []
	#Iterate trough rules from grammar.py
	for i,j in rules.items():
		for rule in j:
			#if a rule is found add it to the end of the list
			#Double check for multiple rules
			if rule == charItem:
				rulesFound.append(i)
	return rulesFound



max = 1
indexList = 0

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

combList = []
posList=[['A', 'J'], ['C']]
tmpC = ['E', 'R']


for u in range(len(posList)):
	indexG = len(posList[u])
	indexD = len(tmpC) 
	for i in range(len(tmpC)):
		for o in range(indexG):
			tempJ = posList[u][o]
			tempK = tmpC[i] 
			#print("j", tempJ, "k", tempK)
			checkC = ''.join(item for item in posList[u][o] + tmpC[i])
			#checkC = ''.join(item for item in posList[u][1] + tmpC[i])
			combList.append(checkC)
			

#print(tmpC[1])
#checkC = ''.join(item for item in posList[indexList] + tmpC)
print(combList)