# This project has two dependencies: nltk and ety

import string
import json
import nltk
import ety

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

wordlist_file = "./wordlist.json"

lemmatizer = WordNetLemmatizer()

good_languages = [
    "English",
    "Middle English",
    "Old English",
    "Old Norse",
]

def find_word_type(word: str):
    potential_word_types = []
    
    if word.endswith("ed") or word.endswith("ing") or word.endswith("s"):
        potential_word_types.append("verb")
    
    if word.endswith("er") or word.endswith("est"):
        potential_word_types.append("adjective")
    
    return potential_word_types

def find_related_words(word: str):
    # words = [word]
    words = [] # Don't include original word
    word_types = find_word_type(word)

    if "verb" in word_types:
        words.append(lemmatizer.lemmatize(word, pos="v"))
    if "adjective" in word_types:
        words.append(lemmatizer.lemmatize(word, pos="a"))
    else:
        words.append(lemmatizer.lemmatize(word))
    
    return words

# lemmatizer.lemmatize("rocks")

while True:
    sentence = input("Input sentence: ")
    words = []

    tokens = word_tokenize(sentence)
    tokens = [i.lower() for i in tokens]

    for word in tokens:
        if word not in string.punctuation:
            words += find_related_words(word)

    words = list(set(list(words))) # Keep only unique tokens

    translations = {}

    with open(wordlist_file, "r") as f:
        translations_raw = f.read()
        translations = json.loads(translations_raw)
    
    # print(f"translations: {translations}\ntranslations ^^^") # PURE DEBUG

    results = {}
    warnings = []
    
    for word in words:
        # Check for translations
        if word in translations.keys():
            results[word] = translations[word]
            # results.append({word: translations[word]})

        # Check for non-Germanic words
        germanic = False

        origins = ety.origins(word, recursive=True)

        if len(origins) == 0: # Skip if no origin is found
            continue

        ultimate_origin = origins[-1]

        for langs in good_languages:
            if langs in str(origins):
                germanic = True
        
        if not germanic:
            origins_str = ""
            for origin in origins:
                origins_str += f"{origin} -> "

            warnings.append(
f"'{word}' is not Germanic in Origin! It is '{origins_str}'"
            )

    # print(f"results: {results}")
    # print(f"results: {json.dumps(results, sort_keys = True, indent = 4)}")
    print("""==[ RESULTS ]==
[Non-Germanic Word]\t[Replacement]""")
    for k, v in results.items():
        print(f"{k}\t:\t{v}\n")

    for w in warnings:
        print(f"warning: {w}")
    
    # Check if each word is Germanic or not