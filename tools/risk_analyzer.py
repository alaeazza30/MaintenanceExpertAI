from tools.rpn_calculator import calculate_rpn

fmeca = [
    {
        "component": "Roulement",
        "G": 9,
        "F": 7,
        "D": 5
    },
    {
        "component": "Ventilateur",
        "G": 8,
        "F": 5,
        "D": 3
    },
    {
        "component": "Enroulement",
        "G": 10,
        "F": 6,
        "D": 4
    }
]

# Calcul des RPN
for item in fmeca:
    item["RPN"] = calculate_rpn(
        item["G"],
        item["F"],
        item["D"]
    )

# Tri décroissant
fmeca.sort(
    key=lambda x: x["RPN"],
    reverse=True
)

print("\n===== CLASSEMENT DES RISQUES =====\n")

for i, item in enumerate(fmeca, start=1):

    if item["RPN"] >= 300:
        criticity = "CRITIQUE"

    elif item["RPN"] >= 200:
        criticity = "ELEVEE"

    elif item["RPN"] >= 100:
        criticity = "MOYENNE"

    else:
        criticity = "FAIBLE"

    print(
        f"{i}. "
        f"{item['component']} "
        f"- RPN={item['RPN']} "
        f"- {criticity}"
    )