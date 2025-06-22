import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import torch
import re

# Create a Flask application instance
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Define the path to the fine-tuned model
# The model is expected to be in the 'models' directory at the root of the project
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models')

# Load the text2text-generation pipeline from the fine-tuned model
# This is done once when the app starts to be efficient
try:
    # Check if a CUDA-enabled GPU is available, otherwise use CPU
    device = 0 if torch.cuda.is_available() else -1
    chatbot_pipeline = pipeline("text2text-generation", model=MODEL_PATH, tokenizer=MODEL_PATH, device=device)
except Exception as e:
    # If the model can't be loaded, create a dummy pipeline that returns an error
    # This prevents the app from crashing if the model is missing
    print(f"Error loading model: {e}")
    chatbot_pipeline = None

# A simple list of keywords to detect profanity for the guardrail
PROFANITY_KEYWORDS = ["motherfucker", "bitch", "shit", "fuck"]

@app.route('/chat', methods=['POST'])
def chat():
    """
    The main chat endpoint. It receives a user's message,
    generates a response using the model, and returns it.
    """
    if chatbot_pipeline is None:
        return jsonify({'error': 'Model is not loaded.'}), 500

    # Get the user's message from the request's JSON body
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided.'}), 400

    # Basic safety guardrail for profanity
    if any(re.search(r'\b' + word + r'\b', user_message, re.IGNORECASE) for word in PROFANITY_KEYWORDS):
        return jsonify({'response': "I am not equipped to handle such language. Let's maintain a supportive conversation."})

    try:
        # Improved prompt to guide the model's response
        prompt = f"Give a supportive and encouraging response to a person who says: '{user_message}'"
        
        # Use the pipeline to generate a response with better parameters
        response = chatbot_pipeline(
            prompt, 
            max_new_tokens=60, 
            do_sample=True,
            temperature=0.7,
            top_k=50,
            repetition_penalty=1.2 
        )
        
        chatbot_response = response[0]['generated_text']
        return jsonify({'response': chatbot_response})
    except Exception as e:
        print(f"Error during inference: {e}")
        return jsonify({'error': 'Failed to generate a response.'}), 500

# This block runs the app in debug mode when the script is executed directly
if __name__ == '__main__':
    # The app will run on http://127.0.0.1:5000
    app.run(debug=True) 