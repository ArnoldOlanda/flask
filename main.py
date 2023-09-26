from flask import Flask, request, jsonify
from transcribe import transcribe_audio
from completion_gpt import completion_gpt as gpt
import openai

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
    archivo_audio.save("audio.wav")

    texto = transcribe_audio("audio.wav")

    completion = gpt(texto)

    return jsonify({"transcription": texto, "content": completion}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
