import json
from database import get_database

db = get_database()
clientes_collection = db["clientes"]

with open("clientes.json", "r") as archivo:
    # Carga el contenido del archivo JSON en una variable
    clientes = json.load(archivo)


def get_customer_id(ruc_dni=""):
    cliente_id = None
    # for cliente in clientes:
    #     if cliente["number"] == ruc_dni:
    #         cliente_id = cliente["id"]
    cliente = clientes_collection.find_one({"number": ruc_dni})

    if not (cliente):
        print("El cliente no existe en la base de datos")
    else:
        cliente_id = cliente["id"]
        print(cliente_id)
        return cliente_id
