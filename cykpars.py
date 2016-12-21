#let the input be a string I consisting of n characters: a1 ... an.
#let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
#let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
#for each s = 1 to n
#  for each unit production Rv -> as
#    set P[1,s,v] = true
#for each l = 2 to n -- Length of span
#  for each s = 1 to n-l+1 -- Start of span
#    for each p = 1 to l-1 -- Partition of span
#      for each production Ra -> Rb Rc
#        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
#if P[n,1,1] is true then
#  I is member of language
#else
#  I is not member of language
#Source: 
#https://en.wikipedia.org/wiki/CYK_algorithm#As_pseudocode


import os
from grammar import rules

def printMatrix(Matrix, lengthW):
	
	lengthHeight = lengthW + 1

	for c in range(lengthHeight):
		#print (c)
		#print('\n')
		for v in range(lengthW):
			#print(v)
			print(Matrix[c][v])

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


def parser(WORD):
	lengthW = len(WORD)
	#Height of array, + 1 because the word isnt part of the algorithm
	lengthH = lengthW + 1
	#Initialize Matrix 
	Matrix = [[0 for x in range(lengthW)] for y in range(lengthH)]

	#Fill first row with the word to parse 
	for x in range(lengthW):
		Matrix[0][x] = WORD[x]
	#Parse Terminalsymbols
	#seperate loop because if there is a symbol that cant be
	#deducted through a rule the word cant be build
	for i in range(lengthW):
		findC = Matrix[0][i]
		foundC = findRules(findC)
		if(len(foundC) == 0):
			print("Word cant be build")
			return 1
		Matrix[1][i] = foundC
	#Print Matrix after first row 
	printMatrix(Matrix, lengthW)
	
	#---------------------------
	#What happens now:
	#-3 for loops
	#Outer = Field thats currently to be filled
	#Middle = Field under outer, goes down straight
	#Inner = Diagonal "up" right, goes down diagonal
	#Then check every step if Middle + Inner = in rules
	#Write every possibility in there
	#If not leave it 
	#----------------------------
	#When the loops are over go to 
	#Matrix[0][lengthH]
	#And test if there is a S


def main():
	WORD = input("Enter the word to test \n")
	parser(WORD)

if __name__ == "__main__":
    main()