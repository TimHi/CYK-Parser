import os
import numpy as np
from grammar import rules

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

def initArray(WORD):
	length = len(WORD)
	height = length
	tArray = np.zeros([height, length], list)
	return tArray


def parse(WORD, array, wHeight, u):
	#print(u)
	print("------------FUNCTION START----------------")
	print(array)
	possibleProductions = []
	length = len(WORD)
	length = (length - u) 
	if(u == 0):
		return array
	else:
		#CHECK LOOP NEST IF CORRECT
		for i in range(length):
			possibleProductions = []
			inDown = u - 1
			for z in range(1, wHeight):
				
				if(u == 0):
					dummy = 9
				elif(inDown < 0):
					dummy = 9
				else:
					#print("I = ", i, "inDown= ", inDown)
					tempC = array[inDown][i]
					print("tempC: ", tempC, "an Stelle Height:", inDown, "Right: ", i)
					#array[inDown][i] = ['H']
					#print(tempC)
					possibleProductions.append(tempC)
					print("Possible Production:", possibleProductions)
					#straight downwards
					inDown = inDown - 1 
			for k in range(1, wHeight):
				indexList = 0
				inRight = u 
				inHeight = i
				tempD = array[inHeight][inRight]
				print("Diagonal tempD: ", tempD )
				if(tempD == 0):
					dummy = 10
				else:
					#checkC = tempC.join(possibleProductions[indexList])
					#checkC = possibleProductions[indexList] + tempC
					checkC = ''.join(item for item in possibleProductions[indexList] + tempD)

					#for o in range()
					#checkC = possibleProductions[indexList][0] + tempC[0]
					print("CheckC: ", checkC)
					foundC = findRules(checkC)
					print("foundC: ", foundC)
				
					array[u][i] = foundC
				#Diagonal upwards
				inRight = inRight - 1
				inHeight = inHeight + 1
				indexList = indexList + 1



	print("------------FUNCTION END----------------")
	return array


def parseFirst(WORD, array):
	possibleProductions = {}
	length = len(WORD)
	height = length

	#parse first row of array
	#do this seperatly because if one terminalsymbol
	#cant be deducted the word cant be build
	for i in range(length):
		findC = WORD[i]
		foundC = findRules(findC)
		array[0][i] = foundC
		if(len(foundC) == 0):
			print("Word cant be build")
			print(array)
			return 1
	#print(array)
	return array





def main():
	WORD = input("Enter the word to test \n")
	array = initArray(WORD)
	array = parseFirst(WORD, array)
	#loop:
	wHeight = len(WORD)
	for u in range(1, wHeight):
		array = parse(WORD, array, wHeight, u)
	print(array)


if __name__ == "__main__":
	main()