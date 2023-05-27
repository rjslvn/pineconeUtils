# Import necessary libraries
import json
import nltk
import scipy.sparse as sparse
import numpy as np
import logging
import os
from gensim.models import KeyedVectors
from tqdm import tqdm
import PyPDF2

# Set the logging level to INFO
logging.basicConfig(level=logging.INFO)

# Define the path to the PDF file
pdf_path = 'MYGPT.pdf'

# Open the PDF file in read-binary mode
with open(pdf_path, 'rb') as pdf_file:
    # Create a PdfReader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Initialize an empty string to store the text extracted from the PDF
    pdf_text = ""
    # Loop over each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Extract the text from the current page and append it to the pdf_text string
        pdf_text += pdf_reader.pages[page_num].extract_text()

# Define the path to the Word2Vec model file
word2vec_model_path = 'googlenews-vectors-negative300.bin'

# Check if the Word2Vec model file exists
if not os.path.exists(word2vec_model_path):
    print('Word2Vec model not found. Downloading...')
    # Add your code to download the model here

# Load the pre-trained Word2Vec model
model = KeyedVectors.load_word2vec_format(word2vec_model_path, binary=True)

# Initialize an empty list to store the word embeddings
combined_embeddings = []

# Loop over each word in the text
with tqdm(total=len(pdf_text.split()), desc="Creating embeddings") as pbar:
    for word in pdf_text.split():
        try:
            # Get the word embedding for the current word
            word_emb = model[word]
            # Convert the word embedding from a numpy array to a list and append it to the combined_embeddings list
            combined_embeddings.append(word_emb.tolist())
        except KeyError:
            pass  # Ignore words not in the vocabulary
        pbar.update(1)

# Open a JSON file in write mode
with open('embeddings.json', 'w') as f:
    # Dump the combined_embeddings list to the JSON file
    json.dump(combined_embeddings, f)

print('Embeddings saved successfully!')
