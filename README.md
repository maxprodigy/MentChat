# MentChatbot: Empathetic Response Generator for Mental Health Support

## Project Overview
MentChatbot is a domain-specific chatbot designed to offer encouraging and emotionally supportive responses to individuals expressing distress. The chatbot simulates the tone of a kind, non-judgmental friend or counselor—someone who listens and responds with compassion when you need it most.

## Why Mental Health?
Many people silently struggle with feelings of sadness, anxiety, overwhelm, and loneliness. While professional help is essential, it isn't always accessible. MentChatbot aims to fill part of that gap by being available 24/7 to offer a few kind words and a sense of understanding.

## Dataset
- **Sources:**
  - A wellness-focused Korean chatbot dataset (translated to English)
  - A mental health intent–response dataset ("Friend Mode")
- **Merging & Cleaning:**
  - Combined, deduplicated, and cleaned both datasets
  - Final dataset: ~3,230 prompt–response pairs
  - Preprocessing: lowercasing, removing non-alphabetic characters, stopword removal, lemmatization
- **Format:**
  - Each entry: a user input describing a difficult emotion or mental state, and a response offering encouragement, empathy, or validation

## Model and Fine-Tuning
- **Base Model:** `google/flan-t5-small` (instruction-tuned transformer)
- **Tokenization:** Max length 128 for both input and output
- **Training:**
  - 20 epochs, batch size 4, learning rate 5e-5
  - Best model selected by evaluation loss
  - Tracked with Weights & Biases (W&B)
- **Final Training Loss:** ~0.39
- **Frameworks:** `transformers`, `torch`, `pandas`, `scikit-learn`, `nltk`

## Performance Metrics
- **BLEU Score:** Average BLEU ≈ 0.0401 (on 50 samples)
- **Qualitative Analysis:**
  - Model provides supportive, encouraging responses
  - Sometimes responses are generic or repetitive
  - Example:
    - **User:** I feel like I'm not good enough
    - **Chatbot:** I think it's a good idea to ask for help if you have a hard time.

## How to Run the Project

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```
The backend server will start on `http://127.0.0.1:5000`.

### 2. Frontend
Open `frontend/ChatBot/chatbot.html` in your web browser. You can now chat with the AI Counselor.

## Example Conversation
**User:** I feel like I'm not good enough.

**Chatbot:** I think it's a good idea to ask for help if you have a hard time.

**User:** I can no longer control my feelings.

**Chatbot:** I think it's a good idea to get help from someone who can help you.

**User:** What should I do if I feel anxious?

**Chatbot:** It's a good idea to take a deep breath and talk to someone you trust.

---

## Training Summary
- **First Training:** 3 epochs, loss ≈ 2.89
- **Second Training:** 6 epochs, loss ≈ 1.02
- **Final Training:** 20 epochs, loss ≈ 0.39
- **Speed:** ~24.7 samples/sec (final run)

## Limitations & Future Work
- Responses can be generic or repetitive
- BLEU score is low, but qualitative results are more promising
- Future: More diverse data, advanced prompt engineering, and improved safety/guardrails 