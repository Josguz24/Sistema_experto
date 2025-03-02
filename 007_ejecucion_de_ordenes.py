# Definición de la base de conocimiento
base_conocimiento = {
    "fiebre": "posible infección",
    "tos": "posible resfriado",
    "dolor de cabeza": "posible migraña"
}

def ejecutar_accion(diagnostico):
    acciones = {
        "posible infección": "Tomar antibióticos y descansar.",
        "posible COVID-19": "Hacerse una prueba y aislarse.",
        "posible gripe": "Tomar líquidos y reposar."
    }
    return acciones.get(diagnostico, "No se recomienda ninguna acción.")

sintoma = "fiebre"
diagnostico_paciente = base_conocimiento.get(sintoma, "Desconocido")
print(f"Acción recomendada: {ejecutar_accion(diagnostico_paciente)}")