import time

# 1. Adquisición del Conocimiento
base_conocimiento = {}

def agregar_regla(sintoma, enfermedad):
    base_conocimiento[sintoma] = enfermedad
    print(f"Regla agregada: Si hay '{sintoma}', entonces es '{enfermedad}'.")
    time.sleep(3)

# Agregamos reglas iniciales
agregar_regla("fiebre", "posible infección")
agregar_regla("tos seca", "posible COVID-19")
agregar_regla("dolor muscular", "posible gripe")

# 2. Base de Hechos (Datos específicos del paciente)
base_hechos = {
    "paciente": "Juan Pérez",
    "edad": 30,
    "sintomas": ["fiebre", "tos seca"]
}

# 3. Motor de Inferencia
def diagnostico(sintomas):
    resultados = []
    for sintoma in sintomas:
        if sintoma in base_conocimiento:
            resultado = f"Síntoma: {sintoma} → Diagnóstico: {base_conocimiento[sintoma]}"
            print(resultado)
            time.sleep(3)
            resultados.append(resultado)
        else:
            resultado = f"Síntoma: {sintoma} → No hay diagnóstico disponible"
            print(resultado)
            time.sleep(3)
            resultados.append(resultado)
    return resultados

# 4. Módulo de Explicaciones
def explicar(sintoma):
    if sintoma in base_conocimiento:
        return f"El síntoma '{sintoma}' está asociado con '{base_conocimiento[sintoma]}'"
    else:
        return "No se encontró una explicación."

# 5. Interfaz de Usuario (Interacción con el usuario)
def interactuar_usuario():
    print("\nBienvenido al Sistema Experto Médico")
    time.sleep(3)
    sintoma_usuario = input("Ingrese su síntoma: ")
    resultado_diagnostico = diagnostico([sintoma_usuario])
    print("\nResultados del diagnóstico:")
    for res in resultado_diagnostico:
        print(res)
        time.sleep(3)
    print("\nExplicación:")
    print(explicar(sintoma_usuario))
    time.sleep(3)

# 6. Ejecución de Órdenes
def ejecutar_accion(diagnostico):
    acciones = {
        "posible infección": "Tomar antibióticos y descansar.",
        "posible COVID-19": "Hacerse una prueba y aislarse.",
        "posible gripe": "Tomar líquidos y reposar.",
        "faringitis": "Tomar analgésicos y hacer gárgaras con agua tibia."
    }
    return acciones.get(diagnostico, "No se recomienda ninguna acción.")

# 7. Sistema de Aprendizaje (Aprender nuevas reglas)
def aprender_nueva_regla(sintoma, enfermedad):
    base_conocimiento[sintoma] = enfermedad
    print(f"Aprendida nueva regla: Si hay '{sintoma}', entonces es '{enfermedad}'.")
    time.sleep(3)

# Flujo del Sistema Experto
if __name__ == "__main__":
    interactuar_usuario()
    
    print("\nAcciones recomendadas basadas en síntomas registrados:")
    time.sleep(3)
    for sintoma in base_hechos["sintomas"]:
        diagnostico_paciente = base_conocimiento.get(sintoma, "Desconocido")
        print(f"Síntoma: {sintoma} → {ejecutar_accion(diagnostico_paciente)}")
        time.sleep(3)
    
    # Aprender nueva regla (Ejemplo de aprendizaje automático)
    aprender_nueva_regla("dolor de garganta", "faringitis")
    
    print("\nBase de conocimiento actualizada:")
    time.sleep(3)
    for key, value in base_conocimiento.items():
        print(f"{key}: {value}")
        time.sleep(3)
