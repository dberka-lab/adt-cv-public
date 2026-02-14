# Cvičení: Kolekce v Pythonu a vlastní objekty

V tomto cvičení si procvičíte práci se základními kolekcemi v Pythonu (`list`, `tuple`, `set`, `dict`) a jejich vzájemné vnořování. Dále si ukážeme, jak správně pracovat s vlastními objekty uvnitř těchto kolekcí, konkrétně v množinách a jako klíče v tabulkách (slovnících).

## Teoretický úvod

### Seznam (`list`)
Uspořádaná, měnitelná kolekce.
```python
fruits = ["jablko", "banán"]
fruits.append("pomeranč")
print(fruits[0]) # jablko
```

### N-tice (`tuple`)
Uspořádaná, **neměnná** kolekce. Často se používá pro záznamy s pevným počtem polí (např. řádek z databáze).
```python
student = ("Jan Novák", "A123")
# student[0] = "Petr" # Nelze!
```

### Množina (`set`)
Neuspořádaná kolekce **jedinečných** prvků. Ideální pro odstranění duplicit a rychlé zjišťování přítomnosti prvku.
```python
ids = {"A101", "A102", "A101"} 
print(ids) # {"A101", "A102"} - duplicita odstraněna
```

### Tabulka (slovník) (`dict`)
Kolekce dvojic klíč-hodnota. Klíče musí být unikátní a neměnné (hashovatelné).
```python
scores = {"A101": 95, "A102": 80}
print(scores["A101"]) # 95
```


### Přepravka (`dataclass`)

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    os_cislo: str
```

## Zadání

Pracujeme s daty z univerzitního informačního systému. Máme k dispozici seznam n-tic (tuple), kde každá n-tice reprezentuje jeden zápis předmětu studentem:
`(Jméno, Osobní číslo, Předmět)`

Vaším úkolem je implementovat funkce v souboru `main.py` pro analýzu těchto dat.

### Úkol 1: Unikátní předměty
Implementujte funkci `get_unique_subjects`, která ze vstupních dat získá seznam všech vyučovaných předmětů. Každý předmět by se měl ve výsledku objevit pouze jednou.
*   **Tip:** Jaká kolekce automaticky odstraňuje duplicity?

### Úkol 2: Studenti dle předmětů
Implementujte funkci `group_students_by_subject`, která vytvoří "rozvrh". Výsledkem bude tabulka (slovník), kde:
*   **Klíč:** Název předmětu (str)
*   **Hodnota:** Seznam (`list`) objektů `Student`, kteří mají předmět zapsaný.

Pro každého studenta v datech vytvořte novou instanci třídy `Student`.

### Úkol 3: Unikátní studenti a identita objektů
Implementujte funkci `get_unique_students`, která vrátí množinu (`set`) všech unikátních studentů (fyzických osob).
*   V datech se jeden student vyskytuje vícekrát (pokud má více předmětů).
*   Vytváříte pro každý záznam novou instanci `Student`.

**Problém:**

```python
students = set()
s = Student("Jan", "A01")
students.add(s)
```

vyvolá výjimku (chybu):
```bash
TypeError: unhashable type: 'Student'
```

Musíte použít `frozen=True`, čímž zajistíte, že přepravka bude neměnná. Jak bylo řečeno na přednášce, v množinách a jako klíče v tabulkách lze používat pouze neměnné datové typy.


```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    name: str
    os_cislo: str
```

