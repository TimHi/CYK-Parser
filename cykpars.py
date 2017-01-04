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
			#return 1
	#print(array)
	return array

def parse(WORD, array, i):
	length = len(WORD)
	height = length
	print(i)
	return array

def main():
	WORD = input("Enter the word to test \n")
	array = initArray(WORD)
	array = parseFirst(WORD, array)
	for i in range(1, len(WORD)):
		array = parse(WORD, array, i)
		print(array)

if __name__ == "__main__":
	main()