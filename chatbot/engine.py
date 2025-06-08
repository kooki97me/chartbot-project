import nltk
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def respond(text):
    doc = nlp(text)
    return f"You said: {text} (Processed with spaCy)"
