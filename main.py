from flask import Flask, request, jsonify
from transcribe import transcribe_audio

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"texto": "Hola flask"})


@app.route("/user/<id>")
def get_user(id):
    user_data = {"user_id": id, "name": "Arnold", "email": "olanda188@gmai.com"}

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


# @app.route("/user",methods=["POST"])
# def create_user():
#     data = request.get_json()

#     return jsonify(data),201


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

    return jsonify({"transcripcion": texto}), 200


if __name__ == "__main__":
    app.run(debug=True)

