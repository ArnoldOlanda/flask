import re


def extract_json(texto=""):
    patron = r"```json(.*?)```"
    resultado = re.search(patron, texto, re.DOTALL)

    if resultado:
        json_extraido = resultado.group()
        json_final = json_extraido.replace("```json", "")
        json_final = json_final.replace("```", "")

        return json_final
    else:
        print("No se encontró un JSON en la cadena.")
        return None
