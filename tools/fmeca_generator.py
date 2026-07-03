from tools.rpn_calculator import calculate_rpn

fmeca = [
    {
        "component": "Roulement",
        "failure": "Usure",
        "cause": "Mauvaise lubrification",
        "effect": "Arrêt moteur",
        "G": 9,
        "F": 7,
        "D": 5
    },
    {
        "component": "Ventilateur",
        "failure": "Blocage",
        "cause": "Accumulation poussière",
        "effect": "Surchauffe",
        "G": 8,
        "F": 5,
        "D": 3
    },
    {
        "component": "Enroulement",
        "failure": "Court-circuit",
        "cause": "Vieillissement isolation",
        "effect": "Perte totale",
        "G": 10,
        "F": 6,
        "D": 4
    }
]

print("\n===== AMDEC =====\n")

for item in fmeca:

    rpn = calculate_rpn(
        item["G"],
        item["F"],
        item["D"]
    )

    print("--------------------------------")
    print("Composant :", item["component"])
    print("Défaillance :", item["failure"])
    print("Cause :", item["cause"])
    print("Effet :", item["effect"])
    print("RPN :", rpn)