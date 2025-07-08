# GenAI Voice Chatbot (Local Ubuntu Setup)

This is a full local implementation of a multilingual voice chatbot using Whisper and OpenAI GPT-4 (or GPT-3.5), with PostgreSQL + pgvector.

## 🔧 Requirements

- Ubuntu 24.04 LTS
- Docker
- Python 3.10+
- PostgreSQL (with pgvector extension)
- OpenAI API Key

## 🛠 Setup Steps

1. Install dependencies:
   sudo apt install ffmpeg docker.io docker-compose postgresql postgresql-contrib libpq-dev python3-venv

2. Start PostgreSQL and enable pgvector:
   sudo -u postgres psql -c "CREATE EXTENSION vector;"

3. Run Docker services:
   cd backend
   docker-compose up --build

4. Open frontend/index.html in your browser.

## 📦 Structure

- frontend/ - Audio recording UI
- backend/ - Whisper and RAG API (Dockerized)
- ingestion/ - Python script to embed docs
- rds/ - PostgreSQL table setup

