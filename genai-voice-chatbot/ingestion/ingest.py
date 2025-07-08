import openai, os, psycopg2
from langchain.embeddings import OpenAIEmbeddings

openai.api_key = os.getenv("OPENAI_API_KEY")
conn = psycopg2.connect("dbname=genai user=postgres password=postgres host=localhost")
cur = conn.cursor()

emb = OpenAIEmbeddings()

for fname in os.listdir("docs"):
    with open(f"docs/{fname}", "r") as f:
        text = f.read()
        vec = emb.embed_documents([text])[0]
        cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (text, vec))

conn.commit()
