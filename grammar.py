#Example of Rules:
#S -> AB
#S -> BD
#A -> BA
#A -> a
#B -> b
#D -> AB

rules = {
	"AB" : "S",
	"BD" : "S",
	"AB" : "D",
	"b" : "B",
	"a" : "A"
}

