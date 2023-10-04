import openai
import json
from extract_json import extract_json

openai.api_key = "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"

message_history = [
    {
        "role": "system",
        "content": "Me ayudaras a generar formatos JSON a partir de un texto de entrada que contiene datos de un pedido. Genera un JSON a partir del texto que te enviare para ello sigue las siguientes instrucciones: 1.Entiende el texto e identifica datos como el ruc/dni del cliente (crea una llave denominada  'ruc_dni')2.Identifica el listado de productos(crea una llava 'productos') donde debe estar el codigo, la cantidad y el tipo de precio ('bodega','mercado','mayorista'), para este caso crea una llave denominada 'precio' . Si los numeros de dni o ruc o los codigos del producto estan separados por puntos quita los puntos y consideralos como un numero entero",
    }
]


def completion_gpt(content=""):
    message_history.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::84Jd7qlU",
        # model="gpt-3.5-turbo",
        messages=message_history,
        temperature=0,
        max_tokens=256,
    )

    json_data = completion.choices[0].message.content
    print(json_data)
    data = json.loads(json_data)
    if "ruc_dni" in data:
        dni_ruc = data["ruc_dni"]
    elif "ruc" in data:
        dni_ruc = data["ruc"]
    elif "dni" in data:
        dni_ruc = data["dni"]
    productos = [
        {
            "codigo": producto["codigo"],
            "cantidad": producto["cantidad"],
            "tipo_precio": producto["precio"],
        }
        for producto in data["productos"]
    ]
    # print(codigo_productos)

    return productos, dni_ruc
