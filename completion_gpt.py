import openai

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
                    Ahora lo que necesito es que me ayudes a generar un formato JSON a partir del texto que te enviare en los proximos mensajes , 
                    necesito que entiendas el texto y sepas identificar datos como el nombre del cliente su direccion y el listado de productos que va a pedir, 
                    de acuerdo al listado de codigo y sus respectivos ids de los productos necesito que armes el listado de los productos a pedir adicionalmente a la cantidad de cada producto y sus respectivo precio, 
                    toda esa info estara en el texto que te proporcionare lo unico que debes cambiar es el codigo por el respectivo id que le corresponde, retorname solo el JSON generado""",
    },
    {
        "role": "assistant",
        "content": """
        Entiendo que necesitas generar un JSON a partir de un texto que contiene información sobre el nombre del cliente, 
        su dirección y un listado de productos con códigos que deben convertirse en sus respectivos IDs, 
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

    return completion.choices[0].message.content
