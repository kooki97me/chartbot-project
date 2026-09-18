import spacy
from openai import OpenAI


# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")


def respond_spacy(text):
    """
    Generate a simple response using spaCy.
    """
    doc = nlp(text)

    return (
        f'Processed with spaCy. You said: "{doc.text}". '
        f"It has {len(doc)} tokens."
    )


def respond_openai(text, api_key):
    """
    Generate a conversational response using OpenAI.
    """

    if not api_key:
        return "OpenAI API key not provided. Please enter it in the sidebar."

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5-mini",
            input=f'The user said: "{text}". Respond conversationally.',
        )

        return response.output_text.strip()

    except Exception as e:
        return f"OpenAI API Error: {str(e)}"
