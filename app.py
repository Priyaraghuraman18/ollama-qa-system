import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

print(response["message"]["content"])