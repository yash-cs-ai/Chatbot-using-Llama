from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(data):
    loader =  DirectoryLoader(data,
                    glob = "*.pdf",
                    loader_cls= PyPDFLoader)
    
    documents = loader.load()

    return documents

# Defines a function to scan the specified directory and extract text from all PDF files found.


#Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)
    
    return text_chunks

# Splits the extracted text into smaller, overlapping chunks (500 chars) to prepare them for embedding.


#download embedding model

def download_hugging_face_embedddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MinilM-L6-v2")
    return embeddings

# Initializes and downloads the specific Hugging Face model used to convert text chunks into vector embeddings.