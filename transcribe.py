import whisperx

# import gc
import numpy as np

# import whisper
# from scipy.io.wavfile import write
# from IPython.display import clear_output
from pydub import AudioSegment

# import wave


def transcribe_audio(file_name="audio.mp3"):
    device = "cpu"
    audio_file = "audio.wav"
    batch_size = 16  # reduce if low on GPU mem
    compute_type = "int8"  # change to "int8" if low on GPU mem (may reduce accuracy)

    # 1. Transcribe with original whisper (batched)
    model = whisperx.load_model("base", device, compute_type=compute_type)

    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)
    # print(result["segments"])  # before alignment

    # # delete model if low on GPU resources
    # # import gc; gc.collect(); torch.cuda.empty_cache(); del model

    # 2. Align whisper output
    model_a, metadata = whisperx.load_align_model(
        language_code=result["language"], device=device
    )
    result = whisperx.align(
        result["segments"],
        model_a,
        metadata,
        audio,
        device,
        return_char_alignments=False,
    )

    # print(result["segments"])  # after alignment

    # Concatenating the transcribed segments
    transcription_text = "\n".join([segment["text"] for segment in result["segments"]])

    # Writing to a .txt file
    with open("transcription.txt", "w") as file:
        file.write(transcription_text)
    return transcription_text

    # # delete model if low on GPU resources
    # # import gc; gc.collect(); torch.cuda.empty_cache(); del model_a

    # # 3. Assign speaker labels
    # diarize_model = whisperx.DiarizationPipeline(use_auth_token=YOUR_HF_TOKEN, device=device)

    # # add min/max number of speakers if known
    # diarize_segments = diarize_model(audio)
    # # diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

    # result = whisperx.assign_word_speakers(diarize_segments, result)
    # print(diarize_segments)
    # print(result["segments"]) # segments are now assigned speaker IDs


# print(transcribe_audio())
