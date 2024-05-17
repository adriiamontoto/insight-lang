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
- [] Support for automatic language detection.
- [] Context-aware and industry-specific translation.

### Emotion Detection 😊😢😡
- [] Analyze text to detect a range of emotions such as joy, sadness, anger, and more.
- [] Provide confidence scores for each detected emotion.

### Sentiment Analysis 📈📉
- [] Determine the sentiment of the text (positive, negative, neutral).
- [] Aspect-based sentiment analysis for more granular insights.

### Named Entity Recognition (NER) 🏷️
- [] Identify and categorize entities (e.g., names, organizations, locations) within the text.
- [] Support for multiple entity types and context-aware recognition.

### Keyword Extraction 🔑
- [] Extract important keywords or phrases from the text.
- [] Customizable extraction rules and relevance scoring.

### Text Summarization 📄
- [] Generate concise summaries from longer texts.
- [] Options for extractive and abstractive summarization.
- [] Customizable summary length and detail level.
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
