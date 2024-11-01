from deep_translator import GoogleTranslator


# Define function
def translate_text(text_from_lang) -> str:
    translator = GoogleTranslator()
    text_to_lang = translator.translate(text_from_lang, target="english", source="auto")
    return text_to_lang


# Read from console
text_from_lang = input("Please enter a text to translate ('stop' to quit): ")

while text_from_lang != "stop":
    print(translate_text(text_from_lang))
    text_from_lang = input("Please enter a text to translate ('stop' to quit): ")

print("Bye ...")
