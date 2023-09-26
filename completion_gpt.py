import openai

openai.api_key = "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"


def initial_task():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": """Estos son los codigos de algunos productos con sus respectivos id: 
        10044->44
        20010->59
        20110->475
        20011->60
        20074->257
        20073->248
        30011->96
        30012->97; 
        Ahora lo que necesito es que me ayudes a generar json a partir del texto que te enviare en los proximos mensajes , 
        necesito que entiendas el texto y sepas identificar datos como el nombre del cliente su direccion y el listado de productos que va a pedir, 
        de acuerdo al listado de codigo y sus respectivos ids de los productos necesito que armes el listado de los productos a pedir adicionalmente a la cantidad de cada producto y sus respectivo precio, 
        toda esa info estara en el texto que te proporcionare lo unico que debes cambiar es el codigo por el respectivo id que le corresponde""",
            }
        ],
    )

    print(completion.choices[0].message.content)


# initial_task()


def completion_gpt(content=""):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "assistant",
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
                "role": "user",
                "content": content,
            }
        ],
        temperature=0,
        max_tokens=256,
    )

    return completion.choices[0].message.content
