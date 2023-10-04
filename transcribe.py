# import whisper
import openai


def transcribe_audio(file_name="audio.mp3"):
    # model = whisper.load_model("base", device="cpu")  # cuda para usar gpu nvidia
    # result = model.transcribe(file_name)
    audio_file = open(file_name, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript.text)
    return transcript.text
