# Algorithmique et complexité — 02/09

**Contact :** `Irenee.Briquel@cyu.fr`

## 1. Mesurer la complexité en temps

La **complexité en temps** mesure le coût d’un algorithme en nombre d’opérations élémentaires.

### Exemples de comptage notés en cours

| Exemple | Nombre d’opérations noté |
| --- | --- |
| Affectation : `a = 1` | 1 |
| Calcul : `3 + 5` | 1 |
| Calcul : `(3 + 8) * 5` | 2 |
| Consultation, calcul et affectation : `b = a + 3` | 3 |

Le comptage dépend du modèle choisi et du langage machine. Par exemple, il existe plusieurs façons d’effectuer une division entière (`//`).

**Exemple noté :** `10 >> 1` donne le même résultat que la division entière de 10 par 2.

Autres exemples dont le coût est à discuter :

```python
P = [1, 2, 3]
P[2] = 5
```

Si le comptage est trop flou, on choisit une **opération témoin**, par exemple une comparaison, puis on compte ses occurrences.

## 2. Coût des boucles

### Principe général

```text
Pour i de 1 à n :
    opération i
```

Le coût est la somme des coûts des opérations :

$$
\sum_{i=1}^{n} \operatorname{coût}(\text{opération } i)
$$

### Boucle simple

```text
Pour i de 1 à n :
    afficher(i)  → 1 opération
```

**Total :** n opérations.

### Deux boucles imbriquées

```text
Pour i de 1 à n :
    Pour j de 1 à n :
        afficher(i)  → 1 opération
```

**Total :** n² opérations.

### Boucle interne dépendant de i

```text
Pour i de 1 à n :
    Pour j de 1 à i :
        afficher("coucou")
```

- Coût de la boucle interne : i opérations.
- Coût total : 1 + 2 + … + n = n(n + 1) / 2.
- Ordre de grandeur : **O(n²)**.

On parcourt les couples (i, j) tels que 1 ≤ j ≤ i ≤ n. Le schéma du cours représente ces couples sur les axes i et j :

```text
j
|
|
|
|___________________ i
```

## 3. Ordres de grandeur

| Notation | Nom |
| --- | --- |
| O(log n) | Logarithmique |
| O(n) | Linéaire |
| O(n log n) | Quasi linéaire |
| O(n²) | Quadratique |
| O(nᵏ) | Polynomial |
| O(eⁿ) | Exponentiel |

## À revoir

- Les notations de Landau : grand O, Θ (thêta), Ω (oméga), etc.
- Piste de recherche notée en cours : « notation de Landau » sur Wikipédia.
