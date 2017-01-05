#S -> AB
#A -> CD|CF
#B -> c|EB
#C -> a
#D -> b
#E -> c
#F -> AD
#Word: aaabbbcc
rules = {'S': ['AB'],'A': ['CD','CF'], 'B': ['c','EB'], 'C': ['a'], 'D' : ['b'], 'E' : ['c'], 'F' : ['AD']}

#S -> AB|BC
#A -> BA|a
#B -> CC|b
#C -> AB|a
#Word:baaba
#rules = {'S': ['AB', 'BC'],'A': ['BA','a'], 'B': ['b','CC'], 'C': ['a', 'AB']}
