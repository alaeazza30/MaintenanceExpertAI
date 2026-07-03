from tools.rpn_calculator import calculate_rpn

# Base AMDEC
fmeca = [
    {
        "component": "Roulement",
        "G": 9,
        "F": 7,
        "D": 5
    },
    {
        "component": "Enroulement",
        "G": 10,
        "F": 6,
        "D": 4
    },
    {
        "component": "Ventilateur",
        "G": 8,
        "F": 5,
        "D": 3
    }
]

print("\n===== OPTIMISATION DES PIECES DE RECHANGE =====\n")

for item in fmeca:

    rpn = calculate_rpn(
        item["G"],
        item["F"],
        item["D"]
    )

    # Classification
    if rpn >= 300:
        priority = "A"
        stock = 4
        inspection = "Hebdomadaire"

    elif rpn >= 200:
        priority = "A"
        stock = 2
        inspection = "Mensuelle"

    elif rpn >= 100:
        priority = "B"
        stock = 1
        inspection = "Trimestrielle"

    else:
        priority = "C"
        stock = 0
        inspection = "Annuelle"

    print("--------------------------------")
    print("Pièce :", item["component"])
    print("RPN :", rpn)
    print("Priorité :", priority)
    print("Stock recommandé :", stock)
    print("Contrôle :", inspection)