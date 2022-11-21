from translate import Translator
translator= Translator(to_lang="en",from_lang="fr")
motsFrancais= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
engWords = {}
for mot in motsFrancais:
    engWords.update({mot : translator.translate(mot)})
print(engWords)