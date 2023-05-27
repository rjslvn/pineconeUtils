# pineconeUtils

Utilities for using pinecone vector DB with llms (covers tokenizing, upserting, etc)

## 🤖 AI Buddy - Pinecone Query and OpenAI Response Generator 🚀

This Python package:

- Uses the SentenceTransformer model to convert a user's query into an embedding vector.
- Sends a POST request to Pinecone to query the index with the query vector.
- Extracts the ID of the most similar item from the response if the query is successful and results are returned.
- Sends a GET request to Pinecone to fetch the vector of the most similar item.
- Extracts the vector from the response and converts it to a string if the fetch is successful.
- Defines a prompt for GPT-3 using the query, item ID, vector string, and chat URL.
- Generates a response using GPT-3.

## 📜 Abstract

In the field of Natural Language Processing, word embeddings are a type of word representation that allows words with similar meaning to have a similar representation. This package automates the process of:

- Generating these word embeddings for a given user query.
- Querying a Pinecone index with the query vector.
- Fetching the vector of the most similar item.
- Generating a GPT-3 response based on the query and the fetched vector.

## 🚀 Usage

```python
# Run the script
python main_script.py
```

This script will:

- Ask the user for a query.
- Convert the query to an embedding vector.
- Query a Pinecone index with the query vector.
- Fetch the vector of the most similar item.
- Define a prompt for GPT-3 using the query, item ID, vector string, and chat URL.
- Generate a GPT-3 response.

## 📄 License

This project is licensed under the terms of the MIT license.

## 📦 Installation

This package requires Python 3.6 or later. To install the package, run the following command:

```bash
pip install sentence_transformers openai requests
```

You also need to set your Pinecone API key and OpenAI API key in the script.

## 🎉 Enjoy!

We hope you find this package useful! If you have any questions, feel free to open an issue on GitHub. Happy querying and responding! 🤖🚀
