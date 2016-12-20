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

#Read the grammar rules from cfg File
#Rules are saved in a dictionary in the form SXY or Sa
#def readGrammar():
	#rules = {}
	#x = 0
	#with open('grammar.cfg') as gFile:
	#	for line in gFile:
	#		stringT = line
	#		stringT = stringT.replace(" -> ", "")
	#		stringT = stringT.replace("\n", "")
	#		rules[x] = stringT
	#		x += 1
	#	print rules

def parser(WORD):
	print("PARSE")
	lengthW = len(WORD)
	#print lengthW
	#Height of array, + 1 because the word isnt part of the algorithm

	lengthH = lengthW + 1
	Matrix = [[0 for x in range(lengthW)] for y in range(lengthH)]

	#Fill first row with the word to parse 
	for x in range(lengthW):
		Matrix[0][x] = WORD[x]
	i = 0 
	j = 0

	for i in range(lengthW):
		tempC = Matrix[0][i]
		if tempC in rules:
			Matrix[1][i] = "FOUND"
			tempT = rules.get(tempC)
			Matrix[1][i] = tempT

	
	print Matrix[1][0]
	print Matrix[1][1]
	print Matrix[1][2]
	print Matrix[1][3]



def main():
	WORD = raw_input("Enter the word to test \n")
#	readGrammar()
	#print rules
	parser(WORD)



if __name__ == "__main__":
    main()