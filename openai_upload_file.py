import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Load file
with open("dataset.jsonl", "rb") as file:
    response = openai.File.create(file=file, purpose="fine-tune")

file_id = response["id"]
print(f"File uploaded with ID: {file_id}")
