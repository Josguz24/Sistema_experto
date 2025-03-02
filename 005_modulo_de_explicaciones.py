# Explicación de la inferencia

# Definición de la base de conocimiento
base_conocimiento = {
    "fiebre": "Posible infección",
    "tos": "Posible resfriado",
    "dolor de cabeza": "Posible migraña"
}

def explicar(sintoma):
    if sintoma in base_conocimiento:
        return f"El síntoma '{sintoma}' está asociado con '{base_conocimiento[sintoma]}'"
    else:
        return "No se encontró una explicación."

print(explicar("fiebre"))
print(explicar("tos seca"))