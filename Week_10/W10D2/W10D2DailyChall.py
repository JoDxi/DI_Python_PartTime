from translate import Translator

translator = Translator(from_lang="fr", to_lang="en")

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translated = {}

for word in french_words:
    translated[word] = translator.translate(word)

print(translated)



