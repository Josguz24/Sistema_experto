base_conocimiento = {
    "fiebre": "posible infección",
    "tos seca": "posible COVID-19",
    "dolor muscular": "posible gripe"
}

def obtener_conocimiento(sintoma):
    return base_conocimiento.get(sintoma, "No hay información disponible")

print(obtener_conocimiento("fiebre"))
print(obtener_conocimiento("tos seca"))
print(obtener_conocimiento("dolor muscular"))
print(obtener_conocimiento("dolor de cabeza"))
