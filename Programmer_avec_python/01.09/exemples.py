"""Exemples exécutables du cours sur les types abstraits de données."""

from collections import deque


def exemple_tableau() -> None:
    tableau = [10, 20, 30]
    print("Tableau initial :", tableau)
    print("Élément d’indice 1 :", tableau[1])
    tableau[1] = 99
    print("Après modification :", tableau)


def exemple_file() -> None:
    file = deque()
    file.append("Alice")
    file.append("Bob")
    premier = file.popleft()
    print("Premier sorti de la file :", premier)


def exemple_pile() -> None:
    pile = []
    pile.append("assiette 1")
    pile.append("assiette 2")
    sommet = pile.pop()
    print("Première retirée de la pile :", sommet)


def exemple_mutabilite() -> None:
    notes = [10, 12]
    notes.append(15)
    print("Liste mutable :", notes)

    texte = "bon"
    nouveau_texte = texte + "jour"
    print("Chaîne originale :", texte)
    print("Nouvelle chaîne immuable :", nouveau_texte)


if __name__ == "__main__":
    exemple_tableau()
    exemple_file()
    exemple_pile()
    exemple_mutabilite()
