from flask import Flask, request, jsonify
import os
import openai
import psycopg2
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

openai.api_key = os.environ["OPENAI_API_KEY"]
app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    question = request.json["text"]
    vectorstore = PGVector(
        connection_string=os.environ["PG_URI"],
        embedding=OpenAIEmbeddings(),
        table_name="documents"
    )
    retriever = vectorstore.as_retriever()
    llm = OpenAI()
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    answer = chain.run(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
