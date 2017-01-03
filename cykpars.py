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
	tArray = np.empty([height, length], list)
	return tArray


def parse(WORD, array, wHeight, u):
	print(u)
	print(array)
	length = len(WORD)
	length = (length - u) 
	if(u == 0):
		return array
	else:
		for i in range(length):
			for z in range(wHeight):
				for k in range(wHeight):
					#Diagonal/Senkrecht checken, 


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
		parse(WORD, array, wHeight, u)


if __name__ == "__main__":
	main()