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

#Rules S -> AB
#To SAB 
import os

#	gFile = open("grammar.cfg", "r")
#	for line in gFile.readline():
#		rules = gFile.readline()
#	print ("SOMETHIN?")
def readGrammar():
	with open('grammar.cfg') as gFile:
		for line in gFile:
			print line
			rules = line
		print rules

def parser(WORD):
	print("PARSE")
	lengthW = len(WORD)
	print lengthW


def main():
	WORD = raw_input("Enter the word to test \n")
	print WORD
	readGrammar()
	parser(WORD)


if __name__ == "__main__":
    main()