import ollama
import whisper
import json

with open("history.json", "r") as file:
    history = json.load(file)

# Load Whisper model
whisper_model = whisper.load_model("base")

# Convert audio to text
result = whisper_model.transcribe("audio/question.m4a")
question = result["text"]

print("Transcribed question:", question)

# Send the transcribed text to Ollama
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("Answer:", response["message"]["content"])

history.append({
    "question": question,
    "answer": response["message"]["content"]
})

with open("history.json", "w") as file:
    json.dump(history, file, indent=4)