# The Main Entry Point: Initializes the Flask application, defines routes (like '/chat'),
# and acts as the bridge between the web interface and the backend logic.

from flask import Flask, render_template, jsonify,request
from src.helper import download_hugging_face_embedddings
from langchain_pinecone import PineconeVectorStore # Best for modern Pinecone
from langchain_core.prompts import PromptTemplate
import pinecone 
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

embeddings = download_hugging_face_embedddings()

index_name = "mchatbot"

docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)

# Connects to an already populated Pinecone index to enable searching without re-uploading the data.

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context" , "question"])
chain_type_kwargs = {"prompt" : PROMPT}

# Initializes the custom prompt object and packages it into a dictionary to configure the retrieval chain.

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={
                      'max_new_tokens':512,
                         'temperature':0.8,
                         'repetition_penalty': 1.1,  
                           'context_length': 2048
                        }
                )

# Loads the local quantized Llama 2 model and configures generation parameters like token limit and creativity (temperature).
retriever=docsearch.as_retriever(search_kwargs={'k':2})

combine_docs_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=PROMPT
)

qa = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=combine_docs_chain
)

# Constructs the main Question-Answering chain that connects the LLM, the retriever (Pinecone), and the prompt to answer queries.

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg)

    result = qa.invoke({"input": msg})

    print("Response :", result["answer"])
    return str(result["answer"])


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8080, debug = True)