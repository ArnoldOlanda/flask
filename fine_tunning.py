import openai

openai.api_key = "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"

file_id = "file-RS8iwRGPqTRZd6bTlgXjbBso"
model_name = "gpt-3.5-turbo"

response = openai.FineTuningJob.create(training_file=file_id, model=model_name)

job_id = response["id"]

print(f"Fine tunning job created with id: {job_id}")
