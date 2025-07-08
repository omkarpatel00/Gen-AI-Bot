FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask openai langchain psycopg2-binary
CMD ["python", "app.py"]
