# pineconeUtils
Utilities for using pinecone vector DB with llms (covers tokenizing, upserting, etc)

🤖 AI Buddy - Pinecone Query and OpenAI Response Generator 🚀
This Python package uses the SentenceTransformer model to convert a user's query into an embedding vector. It then sends a POST request to Pinecone to query the index with the query vector. If the query is successful and results are returned, it extracts the ID of the most similar item from the response. It then sends a GET request to Pinecone to fetch the vector of the most similar item. If the fetch is successful, it extracts the vector from the response and converts it to a string. Finally, it defines a prompt for GPT-3 using the query, item ID, vector string, and chat URL, and generates a response.

📜 Abstract
In the field of Natural Language Processing, word embeddings are a type of word representation that allows words with similar meaning to have a similar representation. This package automates the process of generating these word embeddings for a given user query, querying a Pinecone index with the query vector, fetching the vector of the most similar item, and generating a GPT-3 response based on the query and the fetched vector.

🚀 Usage
python
Copy code
# Run the script
python main_script.py
This script will ask the user for a query, convert the query to an embedding vector, query a Pinecone index with the query vector, fetch the vector of the most similar item, define a prompt for GPT-3 using the query, item ID, vector string, and chat URL, and generate a GPT-3 response.

📄 License
This project is licensed under the terms of the MIT license.

📦 Installation
This package requires Python 3.6 or later. To install the package, run the following command:

bash
Copy code
pip install sentence_transformers openai requests
You also need to set your Pinecone API key and OpenAI API key in the script.

🎉 Enjoy!
