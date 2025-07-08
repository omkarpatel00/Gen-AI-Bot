FROM python:3.10
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install flask openai-whisper
CMD ["python", "app.py"]
