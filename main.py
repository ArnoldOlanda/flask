import openai
from flask import Flask, request, jsonify
from transcribe import transcribe_audio
from completion_gpt import completion_gpt as gpt
from get_products_info import get_products_info
from generate_json import generate_json

app = Flask(__name__)
openai.api_key = "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"


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

    # obtencion de los ids de los productos
    products_ids = gpt(texto)

    # Obtencion de la info de los productos
    products = get_products_info(products_id=products_ids)

    # Generacion del json
    generated_json = generate_json(products=products)

    return jsonify({"transcription": texto, "content": generated_json}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
