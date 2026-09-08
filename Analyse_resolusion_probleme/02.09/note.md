# Cours du 02/09

### Information

Irenee.Briquel@cyu.fr

#Algorithmique et complexité

Complexité en temps = temps de calcule d'un algo En nombre d'opérations élémentaire

ex : 
- une affectation a = 1 -> 1 opération
- une calcule algébrique 3 + 5 -> 1 operation ; (3+8)*5 -> 2 opéation
- une consulation : b = a + 3 -> 3 opération

Discutable car en fonction de language machine, chacun a sa maniere par exemple de faire une // (division entier)

10 >> 1 c'est le resultat identique (ou ya d'autre méthode)

un autre exemple 
P = [1,2,3] (combien d'opération)
P[2] = 5 (un peu difficle a voir)

Sinon si c'est trop flou on peut compter le nombre de comparaison qu'il y a dans un algo. En gros on choisi une opération TEMOI 


Pour i de 1 à n :
    opération i
-> complixité :
cout de la boucle : 

La somme de i= 1 à N : cout(opération i)

pour i de 1 à n :
    print(i) -> (1 opération)

en tout il y a N opération


Print i de 1 à n :
    Pour j de 1 à n :
        print(i) -> (1 opération)
en tout il y N^2 opération


Pour i de 1 à N :
    Pour j de 1 à i :
        print("coucou")

cout de la boucle interne : i opération

cout du tout : somme de i à N de i

donc ça fait n(n+1)/2 (toujours O(N2))

J
|
|
|
|
|
|___________________ i

on fait tout les couples j-i


wikipedia notation de laudon

REVOIR GRAND TO, TETA, OMEGA ect 

O(log(n)) = logarithimque
O(n) = linéaire
O(nlog(n)) = quasi linéaire
O(n^2) : quadratique
O(n^k) : polinomial
O(e^n) : exponentiel
    