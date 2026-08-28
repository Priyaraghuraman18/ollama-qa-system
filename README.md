# Ollama Llama 3.2 Local AI Project

## Overview

This project uses **Whisper** to convert an audio question into text and **Ollama Llama 3.2** to generate an AI answer locally. The question and answer are also stored in `history.json`.

## Technologies Used

* Python
* Ollama
* Llama 3.2
* OpenAI Whisper
* JSON

## Setup

1. Install Ollama.
2. Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

3. Install Python dependencies:

```bash
pip install ollama openai-whisper
```

## Run

Place your audio file at:

```text
audio/question.m4a
```

Then run:

```bash
python app.py
```

The program will:

1. Convert the audio question to text using Whisper.
2. Send the text to Llama 3.2 through Ollama.
3. Display the AI answer.
4. Save the question and answer in `history.json`.
