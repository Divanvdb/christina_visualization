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

def all_drop_downs(build_out: str, demand: Dict, ocgt: Dict):
    option_values = {
        "Eskom TDP 2025": "B1",
        "NECOM Expected": "B2",
        "Delayed roll-out": "B3"
    }
    linked_value = option_values[build_out]

    print(f"Build out trajectory {linked_value}")
    print(f"Demand trajectory {demand}")
    print(f"Ocgt trajectory {ocgt}")