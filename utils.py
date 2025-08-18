from typing import Dict

def eskom_tdp_preset():
    print("Eskom TDP")

    build_out = 0
    demand = {2025: 0, 2026: 0, 2027: 0, 2028: 0, 2029: 0, 2030: 0}
    runtime = {2025: 6, 2026: 6, 2027: 6, 2028: 6, 2029: 6, 2030: 6}

    return build_out, demand, runtime

def necom_expected_preset():
    print("Necom Expected")

    build_out = 1
    demand = {2025: 0, 2026: 0, 2027: 0, 2028: 0, 2029: 0, 2030: 0}
    runtime = {2025: 6, 2026: 6, 2027: 6, 2028: 6, 2029: 6, 2030: 6}

    return build_out, demand, runtime

def delayed_roll_out_preset():
    print("Delayed Roll Out")

    build_out = 2
    demand = {2025: 0, 2026: 0, 2027: 0, 2028: 0, 2029: 0, 2030: 0}
    runtime = {2025: 6, 2026: 6, 2027: 6, 2028: 6, 2029: 6, 2030: 6}

    return build_out, demand, runtime

def scenario_A():
    print("Scenario A")

    build_out = 0
    demand = {2025: 0, 2026: 1, 2027: 2, 2028: 2.5, 2029: 3.5, 2030: 4}
    runtime = {2025: 6, 2026: 6, 2027: 6, 2028: 6, 2029: 6, 2030: 6}

    return build_out, demand, runtime


def scenario_B():
    print("Scenario B")

    build_out = 1
    demand = {2025: 0, 2026: 0, 2027: -0.5, 2028: -0.5, 2029: -1, 2030: -1}
    runtime = {2025: 6, 2026: 6, 2027: 6, 2028: 6, 2029: 6, 2030: 6}

    return build_out, demand, runtime


def documentation():
    print("Documentation")

def all_drop_downs(build_out: str, demand: Dict[int, str], ocgt: Dict[int, str]):
    option_values = {
        "Eskom TDP 2025": "B1",
        "NECOM Expected": "B2",
        "Delayed roll-out": "B3"
    }
    linked_value = option_values[build_out]

    # Generate filenames
    filenames = []
    for year in sorted(demand.keys()):
        d_code = demand[year]
        o_code = ocgt[year]
        filenames.append(f"{linked_value} {d_code} O{o_code} {year}.png")

    return filenames



