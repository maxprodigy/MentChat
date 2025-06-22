# MentChatbot: Empathetic Response Generator for Mental Health Support

## Project Overview
MentChatbot is a domain-specific AI chatbot built to provide emotionally supportive and encouraging responses to users experiencing distress. It mimics the tone of a kind, non-judgmental friend or counselor—someone who truly listens and replies with compassion when you're feeling overwhelmed.

---

## Video Presentation
[Link](https://youtu.be/k1PYiQMTbNg)

---

## Why Mental Health?
Mental wellness is essential, but access to support isn’t always easy. Many people silently deal with sadness, anxiety, or loneliness. While professional care is vital, MentChatbot is designed to offer an extra layer of comfort—24/7, anytime someone just needs to feel heard.

---

## Dataset
**Sources:**
- A wellness-focused Korean chatbot dataset (translated to English)
- A mental health intent–response dataset (“Friend Mode”)

**Preparation:**
- Merged and cleaned both datasets
- Removed duplicates, normalized text, performed lemmatization and stopword filtering
- Final dataset: ~3,230 unique prompt–response pairs

**Format:**
- `User_Input`: An emotional expression
- `Chatbot_Response`: An encouraging reply

---

## Model & Fine-Tuning

| Parameter        | Details                         |
|------------------|----------------------------------|
| **Base Model**   | `google/flan-t5-small`          |
| **Tokenizer**    | Max length: 128 for input/output |
| **Frameworks**   | `transformers`, `torch`, `pandas`, `nltk` |
| **Training Strategy** | 20 epochs, LR = 5e-5, batch size = 4 |
| **Evaluation**   | Lowest eval loss selection      |

---

## Training Sessions Summary

| Training | Epochs | Loss   | Samples/sec | Notes                      |
|----------|--------|--------|-------------|-----------------------------|
| 1st Run  | 3      | ~2.89  | ~17/sec     | Baseline testing            |
| 2nd Run  | 6      | ~1.02  | ~23.2/sec   | Better convergence          |
| 3rd Run  | 20     | **0.39** | ~24.7/sec   | Final fine-tuned version    |

---

## Evaluation Metrics

- **BLEU Score**: Average ~0.0401 across 50 test samples
- **Interpretation**:  
  While BLEU scores are traditionally used for translation, they're less effective in evaluating emotional tone or supportiveness. In practice, the chatbot often provides kind, comforting, and appropriate replies—even when phrasing differs from reference responses.

---

## Sample Dialogue

**User:** I feel like I'm not good enough  
**Chatbot:** I think it's a good idea to ask for help if you have a hard time.

**User:** I can no longer control my feelings  
**Chatbot:** You might want to talk to someone who can help you.

**User:** What should I do if I feel anxious?  
**Chatbot:** Try taking a deep breath and talk to someone you trust.

---

## Homepage Preview

![Homepage Screenshot](https://github.com/maxprodigy/MentChat/blob/main/homepage.png)

---

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
