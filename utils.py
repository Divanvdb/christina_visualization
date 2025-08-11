from typing import Dict

def eskom_tdp_preset():
    print("Eskom TDP")

def necom_expected_preset():
    print("Necom Expected")

def delayed_roll_out_preset():
    print("Delayed Roll Out")

def scenario_A():
    print("Scanario A")

def scenario_B():
    print("Scanario B")

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
        filenames.append(f"{linked_value} {d_code} O{o_code} {year}")

    return filenames



