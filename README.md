# CYK Parser
Cocke Younger Kasami algorithm written in Python.  

#Usage  

Enter the grammar in the file grammar.py like this:  
>S -> AB  
>A -> CD|CF  
>B -> c|EB  
>C -> a  
>D -> b  
>E -> c  
>F -> AD  
>rules = {'S': ['AB'],'A': ['CD','CF'], 'B': ['c','EB'], 'C': ['a'], 'D' : ['b'], 'E' : ['c'], 'F' : ['AD']}  

To start the script enter:  
>python cykparse.py wordToParse  


Note: the script is written in Python 3 so you need to make sure to start it with the correct version.   

