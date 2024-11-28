from textblob import TextBlob
from googletrans import Translator

def analyze_sentiment(text):
    """Analyze sentiment of the text."""
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return 'positive'
    elif blob.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def translate_message(text, target_language):
    """Translate text into the target language."""
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error: {e}"