# 04-26-Complexity: Kontrola duplicitních checkpointů

V předchozím cvičení `03-market` jste implementovali načítání dat z prodejen obchodního řetězce a výpočet délky fronty pomocí množin.

V tomto cvičení využijeme **data z jednoho konkrétního obchodu** a změříme, jaký je rozdíl mezi použitím `list` a `set` při kontrole duplicit.

## Datová sada

Použijte stejná data jako v úloze `03-26-market`. V tomto cvičení budeme pracovat vždy s **jedním konkrétním souborem** (např. `cities/output/Plzen/1-Mon/shop_a.txt`).

Data ke stažení :
[[liks]](https://liks.fav.zcu.cz/adt/exam/service/download-data?filename=cities.zip)

## Měřená úloha

Cílem je **najít všechny unikátní páry (checkpoint, zákazník)** v daném souboru.

Každý řádek dat obsahuje informaci o průchodu zákazníka (identifikovaného `id`) určitým checkpointem (`ckpt`). Chceme zjistit, kolik různých kombinací `(ckpt, id)` se v souboru vyskytuje.

**Poznámka**: Pokud bychom sledovali pouze unikátní checkpointy (`ckpt`), bylo by jich jen ~20, což je příliš málo na demonstraci rozdílu složitosti. Proto sledujeme páry `(checkpoint, zákazník)`, kterých jsou v jednom souboru tisíce.

### Varianta A – `list`

Implementujte funkci, která načte data ze specifikovaného souboru a vrátí seznam unikátních párů.

```python
def check_ckpt_list(data_path: str, city: str, shop: str, day: str) -> list[tuple[str, str]]:
    ...
```

1. Sestavte cestu k souboru pomocí `os.path.join(data_path, city, day, f"{shop}.txt")`.
2. Načtěte soubor po řádcích (přeskočte hlavičku).
3. Z každého řádku získejte `ckpt` a `id`.
4. Udržujte **seznam** (`list`) všech dosud nalezených párů `(ckpt, id)`.
5. Pro každý nově přečtený pár ověřte, zda již v seznamu není:
   - pokud není, přidejte jej (`append`)
   - pokud je, nedělejte nic

V těle funkce používejte operaci `if (ckpt, id) in seen_list`.

### Varianta B – `set`

Stejnou logiku realizujte pomocí `set`:

```python
def check_ckpt_set(data_path: str, city: str, shop: str, day: str) -> set[tuple[str, str]]:
    ...
```

1. Postupujte stejně jako ve variantě A.
2. Namísto seznamu používejte `set` pro ukládání párů `(ckpt, id)`.
3. Každý nově přečtený pár vložte do množiny pomocí `add`. (U množiny není třeba kontrolovat přítomnost, `add` si s duplicitami poradí efektivně samo, ale i explicitní kontrola `in` je rychlá).

## Měření času

Implementujte funkci pro měření času pomocí modulu `timeit`:

```python
def measure(func, data_path: str, city: str, shop: str, day: str, n_runs: int = 5) -> float:
    ...
```

Funkce spustí `func(data_path, city, shop, day)` několikrát za sebou a vrátí celkový čas.

Ve funkci `main`:
1. Načtěte argumenty z příkazové řádky (cesta k datům, město, obchod, den).
2. Zavolejte `experiment`, který změří a vypíše časy pro obě varianty.

### Spouštění programu

Program by měl přijímat argumenty pro specifikaci souboru:

```bash
# Základní použití (použije defaultní hodnoty: Plzeň, shop_a, 1-Mon)
python main.py path/to/cities

# Specifikace konkrétního města, obchodu a dne
python main.py path/to/cities Plzeň shop_b 2-Tue
```

## Co porovnávat a diskutovat

- **Rozdíl v čase**: I na jednom souboru byste měli vidět výrazný rozdíl. Operace `in` nad listem je $O(N)$, nad množinou $O(1)$.
- **Složitost**: Celková složitost pro zpracování $N$ řádků:
  - List: $O(N^2)$ (pro každý z $N$ řádků prohledáváme seznam délky až $N$).
  - Set: $O(N)$ (pro každý z $N$ řádků provedeme operaci v konstantním čase).
- **Počet unikátních prvků**: Čím více unikátních párů v souboru je, tím pomalejší bude varianta s listem.

## K zamyšlení
