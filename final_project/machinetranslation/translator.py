from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Function to Translate English to French'''
    translator = MyMemoryTranslator("english","french")
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Function to Translate French to English'''
    translator = MyMemoryTranslator("french","english")
    english_text = translator.translate(french_text)
    return english_text
