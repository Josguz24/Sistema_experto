# Simulación de adquisición de conocimiento desde un experto
conocimiento = {}

def agregar_regla(sintoma, enfermedad):
    conocimiento[sintoma] = enfermedad

# Adquisición de conocimiento
agregar_regla("fiebre", "gripe")
agregar_regla("tos", "resfriado")
agregar_regla("dolor de cabeza", "migraña")

print(conocimiento)
