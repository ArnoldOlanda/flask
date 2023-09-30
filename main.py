import os
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from database import get_database
from transcribe import transcribe_audio
from completion_gpt import completion_gpt as gpt
from get_products_info import get_products_info
from generate_json import generate_json
from get_customer_id import get_customer_id
from get_products_id import get_products_id

load_dotenv()
os.environ.get("OPENAI_API_KEY")

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"msg": "Api online"})


@app.route("/subir_audio", methods=["POST"])
def subir_audio():
    # Verifica si se ha enviado un archivo en la solicitud
    if "audio" not in request.files:
        return "No se ha enviado ningún archivo de audio", 400

    archivo_audio = request.files["audio"]

    # Verifica si el archivo tiene un nombre
    if archivo_audio.filename == "":
        return "El archivo no tiene nombre", 400

    # Guardar el archivo en el sistema de archivos
    archivo_audio.save("audio.mp3")

    # transcripcion del audio a texto
    texto = transcribe_audio("audio.mp3")

    # creacion del json inicial
    productos, dni_ruc = gpt(texto)

    # Obtencion del id del cliente
    cliente_id = get_customer_id(dni_ruc)

    # Obtencion de los  ids de los productos
    products_data = get_products_id(productos=productos)

    # Obtencion de la info de los productos
    products = get_products_info(products_data=products_data)

    # Generacion del json
    generated_json = generate_json(products=products, cliente_id=cliente_id)

    return jsonify({"transcription": texto, "content": generated_json}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

    dbname = get_database()
    # clientes = dbname.clientes
