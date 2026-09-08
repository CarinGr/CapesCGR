Exercice 2 du td : 

1.

utiliser un ensemble
stack = []
ouvrantes = "({["
match = {"{' = "}" , "[" : "]" ..}
if char in ouvrantes :
if char in fermantes and (len(stack)) == 0 or match[char] != stacl.pop()

sinon on peut utilisé match.keys() et match.values()


2.

def bien_delimité(c, i) :
    stack = []
    ouvrantes = "({["
    fermante = "]})"
    compteur = 0
    for in c :
        if c[i] in ouvrantes :
            compteur
            stack.append(c)
    
    if c[i] in ouvrante :
        for j in range (i, len(c)):
            if c[j] in fermante :
                return j
    
    if c[i] in fermante :
        for j in range (i, 0, -1):
            if c[j] in ouvrante :
                return j
    