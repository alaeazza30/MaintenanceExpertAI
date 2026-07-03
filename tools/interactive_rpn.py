def calculate_rpn(g, f, d):
    return g * f * d

print("=== CALCULATEUR AMDEC ===")

gravite = int(input("Gravité (1-10) : "))
frequence = int(input("Fréquence (1-10) : "))
detection = int(input("Détection (1-10) : "))

rpn = calculate_rpn(gravite, frequence, detection)

print("\nRésultat :")
print("RPN =", rpn)

if rpn >= 300:
    print("Criticité : TRÈS ÉLEVÉE")
elif rpn >= 200:
    print("Criticité : ÉLEVÉE")
elif rpn >= 100:
    print("Criticité : MOYENNE")
else:
    print("Criticité : FAIBLE")