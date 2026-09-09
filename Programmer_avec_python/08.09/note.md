# TD 1 — Notes du 08/09

[Ouvrir le notebook](note.ipynb) · [Énoncé du TD](TD1.pdf)

## Exercice 2 — Délimiteurs

### 1. Vérifier une chaîne

**Piste personnelle :** utiliser un ensemble.

```python
stack = []
ouvrantes = "({["
match = {"{' = "}" , "[" : "]" ..}
if char in ouvrantes :
if char in fermantes and (len(stack)) == 0 or match[char] != stacl.pop()
```

Autre piste : utiliser `match.keys()` et `match.values()`.

### 2. Retrouver la parenthèse correspondante

**Essai personnel en cours :**

```python
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
    
```
