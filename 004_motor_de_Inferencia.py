# Motor de inferencia que usa reglas y hechos

# Definición de la base de conocimiento
base_conocimiento = {
    "fiebre": "Posible infección",
    "tos": "Posible resfriado",
    "dolor de cabeza": "Posible migraña"
}

# Definición de la base de hechos
base_hechos = {
    "sintomas": ["fiebre", "tos", "dolor de cabeza"]
}

def diagnostico(sintomas):
    for sintoma in sintomas:
        if sintoma in base_conocimiento:
            print(f"Síntoma: {sintoma} → Diagnóstico: {base_conocimiento[sintoma]}")
        else:
            print(f"Síntoma: {sintoma} → No hay diagnóstico disponible")

diagnostico(base_hechos["sintomas"])