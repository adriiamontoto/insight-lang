# 🧠🔤 Insight Lang
Insight Lang is a Python 🐍 project aimed at exploring various technologies and develop new skills. The primary goal is to create an API that leverages advanced NLP capabilities such as text translation, emotion detection, and more. To ensure easy deployment, Insight Lang will be containerized using Docker 🐳.

This project is purely educational 📚 and open-source, intended to provide hands-on experience with modern technologies and best practices in software development 🚀.
<br><br>


## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [License](#license)
<br><br>


## Features
### Text Translation 🌐
- [x] Translate text between multiple languages.
- [x] Detect the language of the input text.

### Paraphrasing 🌀
- [] Rewrite text to have the same meaning but with different wording (e.g., more formal, technical, or casual).
- [] Rewrite text to match a specific style or tone.
- [] Provide multiple paraphrasing options for a single input.

### Grammar and Spelling Check ✅❌
- [] Detect and correct grammar errors in the text.
- [] Provide suggestions for spelling corrections.

### Emotion Detection 😊😢😡
- [] Analyze text to detect a range of emotions such as joy, sadness, anger, and more.

### Named Entity Recognition (NER) 🏷️
- [] Identify and categorize entities (e.g., names, organizations, locations) within the text.

### Text Summarization 📄
- [] Generate concise summaries from longer texts.
- [] Customizable summary length and detail level.
- [] Most important sentences extraction.

### Document Processing 📑
- [] Extract and process text from various document formats.
- [] Optical Character Recognition (OCR) for processing scanned documents and images.

### Speech-to-Text and Text-to-Speech 🎤🔊
- [] Convert spoken language into written text.
- [] Convert written text into natural-sounding speech.

### Integration with multiple Large Language Models (LLMs) 🤖
- [x] OpenAI GPT-3.5
- [] Other OpenAI models such as GPT-4, etc.
- [] Google Gemini
- [] Local models such as LLaMA, etc.
<br><br>


## Technologies
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [MariaDB](https://mariadb.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
<br><br>


## Deployment
1. Clone the repository
```bash
git clone git@github.com:adriiamontoto/insight-lang.git
```
<br>

2. Change directory to the project folder
```bash
cd insight-lang
```
<br>

3. Start the Docker containers
```bash
docker-compose up --build -d
```
<br>

4. Start making requests to the API
```bash
curl "http://localhost"
```
<br>


## License
This project is licensed under the terms of the [MIT license](https://choosealicense.com/licenses/mit/).
