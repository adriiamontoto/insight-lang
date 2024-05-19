# 🧠🔤 Insight Lang
Insight Lang is a Python 🐍 project aimed at exploring various technologies and develop new skills. The primary goal is to create an API that leverages advanced NLP capabilities such as text translation, emotion detection, and more. To ensure easy deployment, Insight Lang will be containerized using Docker 🐳.

This project is purely educational 📚 and open-source, intended to provide hands-on experience with modern technologies and best practices in software development 🚀.
<br><br>


## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Documentation](#documentation)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [Utilization](#utilization)
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
- [x] Analyze text to detect a range of emotions such as joy, sadness, anger, and more.

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


## Documentation
Currently, there is no documentation for the project. However, once the project is deployed, you can access the API documentation at the following URL: `http://localhost/docs`.
<br><br>


### Environment Variables
Create a copy of the `.env.example` file and rename it to `.env`. Fill in the required values for the environment variables.

Example `.env` file:
```bash
# Application Variables
APP_NAME='🧠🔤 Insight Lang'
APP_VERSION='0.0.1'

# Backend Variables
BACKEND_PORT=8000
AI_MODEL='gpt-3.5-turbo'
OPENAI_API_KEY='sk-baPo...AxLP'

# Security Variables
SECRET_KEY='yoursupermegaultrasecretkey'
ACCESS_TOKEN_EXPIRATION_DELTA=15  # minutes

## Password Hashing Variables
# Specific argon2 hashing algorithm parameters https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
HASHING_TIME_COST=20
HASHING_MEMORY_COST=47104
HASHING_PARALLELISM=1
HASHING_HASH_LENGTH=32

## Password Requirements
PASSWORD_MIN_UPPERCASE_LETTERS=2
PASSWORD_MIN_LOWERCASE_LETTERS=2
PASSWORD_MIN_DIGITS=2
PASSWORD_MIN_SPECIAL_CHARACTERS=2
PASSWORD_VALID_SPECIAL_CHARACTERS='!@#$%^&*()-_+={}[]|:;"<>,.?/ '

# Database Variables
DB_USERNAME='root'
DB_PASSWORD='root'
DB_HOST='localhost'
DB_PORT=3306
DB_NAME='database'
DB_VERSION='latest'
```
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

3. Create a copy of the `.env.example` file, rename it to `.env` and [fill it with the required values](#environment-variables)
```bash
cp .env.example .env
```
<br>

4. Start the Docker containers
```bash
docker-compose up --build -d
```
<br>

5. Start making requests to the API
```bash
curl "http://localhost:8000"
```
<br>

6. Stop the Docker containers
```bash
docker-compose down
```
<br><br>


## Utilization
### General endpoints
General endpoints are available for testing the API and checking the status of the service them can be accessed at the following URL: `http://localhost:8000` without any authentication.

- Welcome message endpoint:
```bash
curl "http://localhost:8000"
```

- Docs endpoint:
```bash
curl "http://localhost:8000/docs"
```

### Auth related endpoints
Authentication related endpoints can be accessed at the following URL: `http://localhost:8000/auth`.

- Login endpoint:
```bash
curl -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{"email": "userexample@gmail.com", "password": "P#ssW0rd@23!"}'

>>> {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJcdWQ4M2VcdWRkZTBcdWQ4M2RcdWRkMjQgSW5zaWdodCBMYW5nIiwic3ViIjoiYjZkYTE2MTMtMjMxMC00OWFiLWExNjYtOGZlOWU0NmM1NWYzIiwiYXVkIjoiYXV0aGVudGljYXRpb24iLCJleHAiOjE3MTYxNDQzNzYsImlhdCI6MTcxNjE0MzQ3Nn0.PWquMnf3n27vKswaeeeXarBmSNhoFq8rN85SPO3NEI4","token_type":"bearer"}
```

### User related endpoints
User related endpoints require authentication and can be accessed at the following URL: `http://localhost:8000/user`.

- Get user account endpoint:
```bash
curl -X GET "http://localhost:8000/user" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJcdWQ4M2VcdWRkZTBcdWQ4M2RcdWRkMjQgSW5zaWdodCBMYW5nIiwic3ViIjoiYjZkYTE2MTMtMjMxMC00OWFiLWExNjYtOGZlOWU0NmM1NWYzIiwiYXVkIjoiYXV0aGVudGljYXRpb24iLCJleHAiOjE3MTYxNDQzNzYsImlhdCI6MTcxNjE0MzQ3Nn0.PWquMnf3n27vKswaeeeXarBmSNhoFq8rN85SPO3NEI4"

>>> {"email":"userexample@gmail.com","creation_date":"2024-05-19T18:14:36","update_date":"2024-05-19T18:14:36"}
```

- Create new API key endpoint:
```bash
curl -X POST "http://localhost:8000/user/api-key" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJcdWQ4M2VcdWRkZTBcdWQ4M2RcdWRkMjQgSW5zaWdodCBMYW5nIiwic3ViIjoiYjZkYTE2MTMtMjMxMC00OWFiLWExNjYtOGZlOWU0NmM1NWYzIiwiYXVkIjoiYXV0aGVudGljYXRpb24iLCJleHAiOjE3MTYxNDQzNzYsImlhdCI6MTcxNjE0MzQ3Nn0.PWquMnf3n27vKswaeeeXarBmSNhoFq8rN85SPO3NEI4" \
-H "Content-Type: application/json" \
-d '{"name": "Development"}'

>>> {"id":"806c877c-d506-4e83-bc49-50d219a0a3d9","name":"Development","secret_key":"3eee4f8febee75400df0e3b260ee968b83e6289e7b7ecd671967aaacbce17dfd","creation_date":"2024-05-19T18:40:02","last_utilization_date":null}
```

### AI related endpoints
AI related endpoints **only** require API key authentication and can be accessed at the following URL: `http://localhost:8000/translate` for the translation service.

- Translate text endpoint:
```bash
curl -X POST "http://localhost:8000/translate" \
-H "X-API-Key: 3eee4f8febee75400df0e3b260ee968b83e6289e7b7ecd671967aaacbce17dfd" \
-H "Content-Type: application/json" \
-d '{"text": "I am learning to translate texts with LLM models.", "language": "es"}'

>>> {"original_text":"I am learning to translate texts with LLM models.","text":"Estoy aprendiendo a traducir textos con modelos LLM.","language":"es"}
```
<br><br>


## License
This project is licensed under the terms of the [MIT license](https://choosealicense.com/licenses/mit/).
