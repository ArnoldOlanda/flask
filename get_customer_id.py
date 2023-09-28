import json

with open("clientes.json", "r") as archivo:
    # Carga el contenido del archivo JSON en una variable
    clientes = json.loads(archivo)


def get_customer_id(ruc_dni=""):
    cliente_id = None
    for cliente in clientes:
        if cliente["number"] == ruc_dni:
            cliente_id = cliente["number"]

    print(cliente_id)
    return cliente_id
