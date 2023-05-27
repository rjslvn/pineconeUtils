import json
from sentence_transformers import SentenceTransformer

# Load the conversations from the JSON file
with open('conversations.json', 'r') as f:
    data = json.load(f)

# Initialize the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Iterate over the conversations
for conversation in data:
    # Extract the messages from the conversation
    messages = [message['message']['content']['parts'][0] for message in conversation['mapping'].values() if message['message'] and 'parts' in message['message']['content']]

    # Generate embeddings for the messages
    embeddings = model.encode(messages)

    # Iterate over the messages in the conversation
    for message, embedding in zip(conversation['mapping'].values(), embeddings):
        # Create a new 'vector' field in the message with the embedding
        message['vector'] = embedding.tolist()

# Save the updated data to a new JSON file
with open('pinecone_upsert.json', 'w') as f:
    json.dump(data, f)

print('Embeddings saved successfully!')
