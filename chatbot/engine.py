import nltk
import spacy

# The spaCy model 'en_core_web_sm' should be installed via requirements.txt
nlp = spacy.load("en_core_web_sm")

def respond(text):
    doc = nlp(text)
    return f"You said: {text} (Processed with spaCy)"
