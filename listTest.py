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


posList=[['A'], ['C']]
tmpC = ['E', 'B']
print(len(posList))
print(len(tmpC))
for i in range(len(tmpC)):
	print(tmpC[i])

print(tmpC[1])
checkC = ''.join(item for item in posList[indexList] + tmpC)