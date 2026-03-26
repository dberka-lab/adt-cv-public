import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))


def worker_tick(worker: Worker) -> None:
    if worker.timer > 0:
        worker.timer -= 1
        return

    if len(worker.source) > 0:
        person = worker.source.popleft()
        worker.dest.append(person)
        worker.timer = get_delay(worker.period, worker.spread_factor)
        print(f"{worker.name} is currently working.")


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Current time: {time} seconds")

    for name, q in queues:
        print(f"{name}({len(q)})")


def main() -> None:
    people_number = 1000

    # 1. Vytvoření front
    street_q: deque = deque(list(range(people_number)))
    gate_q: deque = deque()
    vege_q: deque = deque()
    cashier_q: deque = deque()
    final_q: deque = deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe: list[tuple(str, deque)] = [
        ("Street", street_q),
        ("Gate", gate_q),
        ("Vege", vege_q),
        ("Cashier", cashier_q),
        ("Final", final_q)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 5  # Gate keeper každého odbavuje 5s
    vege_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    generator = Worker("Generator", street_q, gate_q, day_m)
    gate_keeper = Worker("GateKeeper", gate_q, vege_q, gate_m)
    vege_man = Worker("VegeMan", vege_q, cashier_q, vege_m, 0.2)
    cashier = Worker("Cashier", cashier_q, final_q, final_m, 0.1)

    # 3. Hlavní smyčka simulace
    workers: list[Worker] = [generator, gate_keeper, vege_man, cashier]

    for time in range(7201):
        for worker in workers:
            worker_tick(worker)

        if time % 60 == 0:
            print_snapshot(time, queues_to_observe)


if __name__ == "__main__":
    main()