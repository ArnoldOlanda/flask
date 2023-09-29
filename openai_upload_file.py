import openai

openai.api_key = "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"

# Load file
with open("dataset.jsonl", "rb") as file:
    response = openai.File.create(file=file, purpose="fine-tune")

file_id = response["id"]
print(f"File uploaded with ID: {file_id}")
