#S -> AB
#A -> CD|CF
#B -> c|EB
#C -> a
#D -> b
#E -> c
#F -> AD
#Word: aaabbbcc
#rules = {'S': ['AB'],'A': ['CD','CF'], 'B': ['c','EB'], 'C': ['a'], 'D' : ['b'], 'E' : ['c'], 'F' : ['AD']}

#S -> AB|BC
#A -> BA|a
#B -> CC|b
#C -> AB|a
#Word:baaba
#rules = {'S': ['AB', 'BC'],'A': ['BA','a'], 'B': ['b','CC'], 'C': ['a', 'AB']}

#rules = {'S':['AB', 'CD', 'AT', 'CU', 'SS'], 'T':['SB'], 'U':['SD'], 'A':['('], 'B':[')'], 'C':['['], 'D':[']']}

#S -> BC
#C -> SA
#A -> a
#B -> b
rules = {'S':['BC'], 'C':['SA','BA'], 'A':['a'], 'B':['b']} 
