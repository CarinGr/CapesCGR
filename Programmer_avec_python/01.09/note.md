# Structures de données abstraites

> **Cours du 1er septembre** — Louis Leskow  
> Contact : `louis.leskow@ac.versailles.fr`

---

## 1. Qu’est-ce qu’un type abstrait de données ?

Un **type abstrait de données** (TAD) est un modèle théorique qui décrit une structure de données du point de vue de son utilisateur.

Il précise :

- les **opérations** disponibles ;
- leurs **préconditions** (quand elles peuvent être utilisées) ;
- leurs **axiomes**, qui décrivent leur comportement.

L’important est donc de savoir **ce que fait** la structure, sans imposer **comment elle est programmée**.

---

## 2. Tableau `Tab(n, E)`

`Tab(n, E)` représente un tableau de taille `n` dont les éléments appartiennent à l’ensemble `E`.

### Opérations

| Opération | Signature | Rôle |
|---|---|---|
| Construire | `Eⁿ → Tab(n, E)` | Créer un tableau avec `n` valeurs |
| Accéder | `ieme : Tab(n, E) × Indice → E` | Lire l’élément d’indice `i` |
| Modifier | `change_ieme : Tab(n, E) × Indice × E → Tab(n, E)` | Remplacer l’élément d’indice `i` |

### Précondition

Pour un tableau `t`, `ieme(t, i)` et `change_ieme(t, i, v)` ne sont définies que si `0 ≤ i < n`.

### Axiomes

```text
ieme(construire(a₀, …, aₙ₋₁), i) = aᵢ
ieme(change_ieme(t, i, v), i) = v
```

---

## 3. File `File(E)` — FIFO

Une **file** fonctionne comme une file d’attente : le premier élément entré est le premier à sortir.

> **FIFO** : *First In, First Out*.

| Opération | Signature | Rôle |
|---|---|---|
| File vide | `file_vide : → File(E)` | Créer une file vide |
| Tester | `est_vide : File(E) → Booléen` | Indiquer si la file est vide |
| Enfiler | `enfiler : E × File(E) → File(E)` | Ajouter un élément à la fin |
| Défiler | `defiler : File(E) → E × File(E)` | Retirer et renvoyer le premier élément |

**Précondition :** `defiler(f)` n’est définie que si `f` n’est pas vide.

```text
est_vide(file_vide()) = vrai
est_vide(enfiler(x, f)) = faux
```

---

## 4. Pile `Pile(E)` — LIFO

Une **pile** fonctionne comme une pile d’assiettes : le dernier élément posé est le premier retiré.

> **LIFO** : *Last In, First Out*.

| Opération | Signature | Rôle |
|---|---|---|
| Pile vide | `pile_vide : → Pile(E)` | Créer une pile vide |
| Tester | `est_vide : Pile(E) → Booléen` | Indiquer si la pile est vide |
| Empiler | `empiler : E × Pile(E) → Pile(E)` | Ajouter un élément au sommet |
| Dépiler | `depiler : Pile(E) → E × Pile(E)` | Retirer et renvoyer l’élément du sommet |

**Précondition :** `depiler(p)` n’est définie que si `p` n’est pas vide.

```text
est_vide(pile_vide()) = vrai
est_vide(empiler(x, p)) = faux
depiler(empiler(x, p)) = (x, p)
```

---

## 5. Liste récursive `Liste(E)`

Une liste récursive est soit une liste vide, soit un élément suivi d’une autre liste. Il existe plusieurs représentations : listes chaînées de style Lisp, tableaux dynamiques et vecteurs.

| Opération | Signature | Rôle |
|---|---|---|
| Liste vide | `liste_vide : → Liste(E)` | Créer une liste vide |
| Tester | `est_vide : Liste(E) → Booléen` | Indiquer si la liste est vide |
| Ajouter | `ajouter : E × Liste(E) → Liste(E)` | Ajouter un élément en tête |
| Tête | `tete : Liste(E) → E` | Renvoyer le premier élément |
| Reste | `reste : Liste(E) → Liste(E)` | Renvoyer la liste privée de sa tête |

**Préconditions :** `tete(l)` et `reste(l)` ne sont définies que si `l` n’est pas vide.

```text
est_vide(liste_vide()) = vrai
est_vide(ajouter(x, l)) = faux
tete(ajouter(x, l)) = x
reste(ajouter(x, l)) = l
```

---

## 6. Notions à retenir

### Langage fonctionnel

Un langage fonctionnel considère le calcul comme l’évaluation de fonctions. Il favorise les fonctions pures et limite les changements d’état. Exemples : Haskell, OCaml et Lisp. Python permet aussi d’utiliser certains principes fonctionnels.

### Inférence de type

L’**inférence de type** permet au langage de déterminer automatiquement le type d’une expression sans qu’il soit toujours écrit explicitement.

```python
nombre = 3             # entier
message = "Bonjour"   # chaîne de caractères
```

### Mutable et immuable

- Un objet **mutable** peut être modifié après sa création : `list`, `dict`, `set`.
- Un objet **immuable** ne peut pas être modifié après sa création : `int`, `float`, `str`, `tuple`.

```python
notes = [10, 12]
notes.append(15)          # La même liste est modifiée

texte = "bon"
texte = texte + "jour"   # Une nouvelle chaîne est créée
```

---

## Résumé express

| Structure | Principe | Opérations principales |
|---|---|---|
| Tableau | Accès par indice | Lire, modifier |
| File | FIFO | Enfiler, défiler |
| Pile | LIFO | Empiler, dépiler |
| Liste récursive | Tête + reste | Ajouter, lire la tête, obtenir le reste |

> Pour afficher cette page sans les symboles Markdown dans VS Code : **Ctrl + Maj + V**.  
> Pour exécuter les exemples du cours : `python exemples.py`.
