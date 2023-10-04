from database import get_database

dbname = get_database()
products_collection = dbname["productos"]


def get_products_id(productos=[]):
    productos_data = []
    for codigo in productos:
        producto = products_collection.find_one({"codigo": codigo["codigo"]})
        productos_data.append(
            {
                "id": producto["id"],
                "cantidad": codigo["cantidad"],
                "tipo_precio": codigo["tipo_precio"],
            }
        )

    print(productos_data)
    return productos_data
