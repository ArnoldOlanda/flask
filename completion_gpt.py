import openai
import json
from extract_json import extract_json

openai.api_key = "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"

message_history = [
    {
        "role": "user",
        "content": """
                    Estos son los codigos de algunos productos con sus respectivos id: 
                        10044->44
                        20010->59
                        20110->475
                        20011->60
                        20074->257
                        20073->248
                        30011->96
                        30012->97; 
                    Genera un JSON a partir del texto que te enviare en los proximos mensajes , 
                    necesito que entiendas el texto e identifica datos como el ruc o el dni del cliente segun sea el caso (para este caso crea una llave denominada  "ruc_dni") 
                    y el listado de productos, adicionalmente a la cantidad de cada producto, 
                    toda esa info estara en el texto que te proporcionare lo unico que debes cambiar es el codigo por el respectivo id que le corresponde, 
                    limitate a responderme unicamente con el JSON generado""",
    },
    {
        "role": "assistant",
        "content": """
        Entiendo que necesitas generar un JSON a partir de un texto que contiene información sobre el dni o ruc del cliente, 
        y un listado de productos con códigos que deben convertirse en sus respectivos IDs, 
        además de la cantidad y el precio de cada producto. Para ayudarte con esto, necesitaré que proporciones el texto con la información específica,
         y a partir de ese texto, te mostraré cómo generar el JSON.
        Por favor, proporciona el texto con la información necesaria, y estaré encantado de ayudarte a crear el JSON correspondiente.
        """,
    },
]


def completion_gpt(content=""):
    message_history.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
        temperature=0,
        max_tokens=256,
    )

    json_data = extract_json(completion.choices[0].message.content)
    # print(json_data)
    data = json.loads(json_data)
    dni_ruc = data["ruc_dni"]
    ids_productos = [producto["id"] for producto in data["productos"]]
    print(ids_productos)

    return ids_productos, dni_ruc
