from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf, text_split, download_hugging_face_embedddings
from pinecone import Pinecone  # Import the official Pinecone client
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# Initialize the Pinecone client (modern way)
pc = Pinecone(api_key=PINECONE_API_KEY)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embedddings()

index_name = "mchatbot"

# Run only once.

docsearch = PineconeVectorStore.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings, 
    index_name=index_name
)