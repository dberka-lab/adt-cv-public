# Systém hromadné obsluhy (SHO) & Práce s frontou (deque)

## 1. Úvod: Fronta a Zásobník pomocí `deque`

V Pythonu používáme pro efektivní práci s frontou (Queue) a zásobníkem (Stack) datovou strukturu `deque` z modulu `collections`.

**Úkol 1:**
Vytvořte soubor `intro.py` a vyzkoušejte si základní operace:

1.  **Fronta (FIFO - First In, First Out):**
    *   Vytvořte prázdnou `deque`.
    *   Přidejte na konec prvky "A", "B", "C" (`append`).
    *   Odeberte prvek ze začátku (`popleft`). Měli byste dostat "A".
    *   Vypište zbytek fronty.

2.  **Zásobník (LIFO - Last In, First Out):**
    *   Vytvořte prázdnou `deque`.
    *   Přidejte na konec prvky 1, 2, 3 (`append`).
    *   Odeberte prvek z konce (`pop`). Měli byste dostat 3.
    *   Vypište zbytek zásobníku.

---

## 2. Simulace Systému hromadné obsluhy (SHO)

Systém hromadné obsluhy umožňuje modelovat procesy, kde požadavky čekají ve frontách na zpracování (např. pokladny v obchodě, routery v síti).

V této úloze naprogramujeme jednoduchý simulátor bez použití složitých objektových struktur. Objekty budeme používat pouze jako "přepravky" na data (Data Class), veškerou logiku budou obstarávat funkce.

### Krok 1: Datové struktury

Budeme potřebovat reprezentovat dvě věci: **Frontu** a **Pracovníka** (např. pokladní).

*   **Fronta**: Použijeme přímo `collections.deque`.
*   **Pracovník**: Použijeme jednoduchou třídu `Worker`, která bude držet informace o tom, odkud bere, kam dává a jak dlouho mu to trvá.

```python
from collections import deque
from dataclasses import dataclass
import random

@dataclass
class Worker:
    name: str
    source: deque        # Odkud beru lidi (vstupní fronta)
    dest: deque          # Kam je posílám (výstupní fronta)
    period: int          # Průměrná doba obsluhy
    spread_factor: float = 0.0   # Faktor rozptylu doby obsluhy (volitelné)
    timer: int = 0       # Odpočet času do dokončení aktuální práce
```

### Krok 2: Pomocné funkce

Prozkoumejte funkci `get_delay(period, spread_factor)`, která vrátí náhodný čas.
*   Pokud je `spread_factor` 0, vratí `period` (vhodně pro ladění, žádná náhoda).
*   Jinak použije generátor náhodných čísel `random.gauss(period, period * spread_factor)` a hodnotu převede na `int`.

### Krok 3: Logika obsluhy

Napište funkci `worker_tick(worker: Worker)`, která simuluje jednu sekundu práce.

Logika funkce (zjednodušená):
1.  **Je pracovník zaneprázdněn?** (`worker.timer > 0`)
    *   Pokud ano, jen snižte `timer` o 1 a skončete (`return`).
2.  **Je pracovník volný?**
    *   Zkontrolujte, zda je ve zdrojové frontě (`worker.source`) někdo k obsloužení.
    *   Pokud ano:
        *   Odeberte prvek ze zdroje (`popleft`).
        *   Přidejte ho do destinace (`append`).
        *   Nastavte `worker.timer` na novou hodnotu pomocí `get_delay`. (Tím se pracovník stane zaneprázdněným na daný počet sekund).

### Krok 4: Sledování stavu

Napište funkci `print_snapshot(time: int, queues: list[tuple[str, deque]])`, která vypíše aktuální čas a stav front.
Protože `deque` nemá jméno, musíme si jména předat v seznamu.

```python
def print_snapshot(time: int, queues: list[tuple[str, deque]]):
    # ... iterujte přes (name, q) v queues ...
    # ... vypište f"{name}({len(q)})" ...
```

### Krok 5: Hlavní smyčka (Main)

Ve funkci `main`:
1.  Vytvořte fronty (`deque`). Naplňte vstupní frontu 1000 lidmi (např. čísla 0-999).
2.  Připravte si seznam front pro výpis: `queues_to_observe = [("Street", street_q), ("Gate", gate_q), ...]`
3.  Vytvořte instance `Worker` pro jednotlivá stanoviště s parametry:
    *   **Generator** (příchod lidí): perioda 30s (zdroj: ulice, cíl: brána)
    *   **GateKeeper** (vstup): perioda 5s (zdroj: brána, cíl: zelenina)
    *   **VegeMan** (váha): perioda 45s, spread_factor 0.2 (zdroj: zelenina, cíl: pokladna)
    *   **Cashier** (pokladna): perioda 120s, spread_factor 0.1 (zdroj: pokladna, cíl: hotovo)
4.  Spusťte simulaci v cyklu (např. 2 hodiny = 7200 sekund):
    *   Pro každého `Worker` zavolejte `worker_tick`.
    *   Každých 60 sekund zavolejte `print_snapshot`.

### Bonus:
Zkuste přidat více pokladen nebo různé cesty průchodu obchodem (např. někdo jde rovnou k pokladně, někdo na zeleninu).
