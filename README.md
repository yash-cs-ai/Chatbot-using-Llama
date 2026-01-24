# End to End Chatbot via Llama2

The main purpose of tis repository/project is to create a RAG (Retrieval-Augemented Generation) model.This application allows users to upload documents (PDFs) and chat with them using a local Llama-2 Large Language Model (LLM).

## 🛠️ Technologies Used

### Tech Stack

* **Language:** Python 3.8
* **LLM Framework:** LangChain
* **Model:** Llama-2-7b-chat (GGML)
* **Web Framework:** Flask
* **Vector Database:** Pinecone
* **Frontend:** HTML / CSS / JavaScript

### Development Environment

* **Git Bash:** A Unix-like command-line interface for Windows, used as the primary terminal for version control and script execution.
* **Conda:** Handles environment management, creating isolated spaces to prevent dependency conflicts between projects.
* **Visual Studio Code (VS Code):** The primary IDE, optimized with extensions for Python debugging and Jupyter notebook integration.

## 📂 Project Structure

```text
├── data/                   # Raw data for ingestion
│   └── Medical_book.pdf    # Source PDF document
├── model/                  # Stores the quantized Llama-2 model
│   ├── llama-2-7b-chat.ggmlv3.q4_0.bin
│   └── modelinfo.md
├── src/                    # Source code for core logic
│   ├── __init__.py         # Package marker
│   ├── helper.py           # Functions for loading PDFs and chunking text
│   └── prompt.py           # System prompts and LLM instructions
├── static/                 # Frontend assets
│   ├── script.js           # Client-side behavior
│   └── style.css           # UI Styling
├── templates/              # HTML templates
│   └── chat.html           # Chat interface
├── app.py                  # Main application entry point (Flask)
├── store_index.py          # Script to process data and push to Vector DB
├── setup.py                # Configuration to install 'src' as a package
├── template.py             # Utility for project scaffolding
├── requirements.txt        # List of dependencies
├── LICENSE                 # License information
└── README.md               # Project documentation
```

## Installation & Setup Guide

1. Clone the Repository Start by cloning the project to your local machine.

    ```Bash
    git clone https://github.com/yash-cs-ai/Chatbot-using-Llama.git
    cd your-repo-name
    ```

2. Create a Virtual Environment.
 It is recommended to use Conda or Python's built-in venv to isolate dependencies.

    ```Bash
    conda create -n venv_name python=3.8 -y
    ```

    **To activate or deactivate venv**

    ```bash
    conda activate venv_name
    ```

    ```bash
    conda deactivate
    ```

3. Install Dependencies.

     Install the required Python libraries and register the local src package.

    ```Bash
    pip install -r requirements.txt
    pip install -e .
    ```

4. You must download the model manually.

    Downloaded from :
    Model installed from [Hugging Face - TheBloke/Llama-2-7B-Chat-GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main).
     For more info on the model refer [model info](./model/modelinfo.md)

    *Placement:* Move the downloaded file into the ```model/``` directory in the project root.

5. Configure Environment Variables Create a .env file in the root directory to store your API keys.

    ```Ini, TOML
    PINECONE_API_KEY=your_pinecone_api_key
    ```

6. Ingest Data (Create Vector Store) Run the ingestion script to process your PDFs and store embeddings in the database.

    ```Bash
    python store_index.py
    ```

7. Run the Application Start the Flask server to launch the chatbot interface.

    ```Bash
    python app.py
    ```
