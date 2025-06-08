import spacy
import openai

# The spaCy model 'en_core_web_sm' should be installed via requirements.txt
nlp = spacy.load("en_core_web_sm")

def respond_spacy(text):
    doc = nlp(text)
    # Example: simple response using spaCy's processed doc.
    return f"Processed with spaCy. You said: \"{doc.text}\". It has {len(doc)} tokens."

def respond_openai(text, api_key):
    if not api_key:
        return "OpenAI API key not provided. Please enter it in the sidebar."
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or a newer/cheaper model like "gpt-3.5-turbo-instruct"
            prompt=f"The user said: \"{text}\". Respond conversationally.",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"OpenAI API Error: {str(e)}"
