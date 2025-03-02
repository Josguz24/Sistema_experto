# Definición de la base de conocimiento
base_conocimiento = {
    "fiebre": "posible infección",
    "tos": "posible resfriado",
    "dolor de cabeza": "posible migraña"
}

def aprender_nueva_regla(sintoma, enfermedad):
    base_conocimiento[sintoma] = enfermedad
    print(f"Aprendida nueva regla: Si hay '{sintoma}', entonces es '{enfermedad}'.")

aprender_nueva_regla("dolor de garganta", "faringitis")
print(base_conocimiento)