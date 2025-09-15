import asyncio
from googletrans import Translator


async def traduce_text():
    # Creează un obiect Translator
    translator = Translator()

    # Textul pe care vrei să-l traduci
    text_de_tradus = "Aceasta este o propoziție de test."

    # Traducerea în limba dorită (de exemplu, engleză)
    traducere = await translator.translate(text_de_tradus, src='ro', dest='en')

    # Afișează traducerea
    print(f"Text original: {text_de_tradus}")
    print(f"Traducere: {traducere.text}")


# Rulează funcția asincronă
asyncio.run(traduce_text())
