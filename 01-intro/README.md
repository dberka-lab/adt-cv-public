# Opakování PPA, nastavení prostředí, práce s AI

## 1. REPL: Read-eval-print-loop

Spusťte REPL Pythonu v terminálu operačního systému. Spočtěte délku přepony pravoúhlého trojúhelníku:

1. Připravte proměnné pro délky odvěsen a = 3; b = 4
2. Vypočtěte délku přepony pravoúhlého trojúhelníku a uložte do proměnné c
   (můžete použít sqrt z modulu math, ale jde to i bez něj :-))
3. Vypište hodnotu c

## 2. CMD, Visual Studio Code

### Doporučené balíčky pro VSCode

- ruff (Astral Software)
  - An extremely fast Python linter and code formatter, written in Rust.
  - Pro přizpůsobení nastavení můžeme upravovat .ruff.toml v root adresáři našeho projektu.
  - Nebo pro globální konfiguraci použít na windows `~\AppData\Roaming\ruff\ruff.toml`    (dle dokumentace `${config_dir}/ruff/pyproject.toml`)
    - My jsme pro vás připravili nastavení, které je rozumné pro studium ADT [.ruff.toml](../.ruff.toml)
- python (microsoft)
  - Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
- Code Spell Checker (Street Side Software)
  - (+Czech - Code Spell Checker)
  - "cSpell.language": "en,cs",

Vytvořte skript (textový soubor) se sekvencí příkazů, které vedou ke stejnému výsledku jako v předešlém cvičení s REPL.

### Zásady pro vypracování

1. Proměnné staticky vytvořte v kódu.
2. Importy soustřeďte na začátku textového souboru
3. Diskutujte příponu souboru (.txt .py) Fungují stejně? Proč?
    1. Program spusťte z terminálu operačního systému
    2. Program spusťte v prostředí VSC


## 3. Využívání AI a Debuggeru

1. Přihlaste se na gapps.zcu.cz a z nabídky aplikaci zvolte aplikaci Gemini.
2. V nastavení nástrojů zvolte "Učení s vedením".
3. Do vstupního pole vložte nefunkční kód a pokuste se jej pomocí AI opravit.

```python
data = 1,2,3,4,5,6,7,8,9,10

for i in len(data):
   print(data[i])
```

4. Ve VSCode si otevřete debuggovací panel a něm nastavte debuggovací konfiguraci
5. Odlaďte tento program 

### Další příklady k procvičení

Pokuste se najít chybu v následujících kódech pomocí debuggeru nebo AI. 

**Příklad 1: Výpočet podílu**
Cílem je vypočítat poměry mezi hodnou a jeji změnou.
```python
data = 3,7,6,11,5,5,8,9
prev = 0

for value in data: 
  print(value/(value - prev))
  prev = value
```



**Příklad 2: Odstranění nevyhovujících prvků**
Cílem je odstranit z listu všechna čísla menší než 50. 
```python
scores = [50, 80, 45, 90, 30, 60]
for i in range(len(scores)):
    if scores[i] < 50:
        scores.pop(i)
print(scores)
```

**Příklad 3: Tvorba párů**
Cílem je vytvořit dvojice jmen ze seznamu (např. pro turnaj). 
```python
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
pairs = []

for i in range(len(names)):
    if i + 1 < len(names):
        pairs.append(names[i] + " - " + names[i+1])

print(pairs)
```

**Příklad 4: Klouzavý průměr**
Cílem je spočítat klouzavý průměr teplot s oknem velikosti 3.
```python
temperatures = [20.5, 21.0, 22.5, 20.0, 19.5, 23.0, 24.0]
window_size = 3
moving_averages = []

for i in range(len(temperatures)):
    window = temperatures[i:i+window_size]
    average = sum(window) / window_size
    moving_averages.append(average)

print(moving_averages)
```

