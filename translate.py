# This project has two dependencies: nltk and ety

import nltk
import ety

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def find_word_type(word: str):
    potential_word_types = []
    
    if word.endswith("ed") or word.endswith("ing") or word.endswith("s"):
        potential_word_types.append("verb")
    
    if word.endswith("er") or word.endswith("est"):
        potential_word_types.append("adjective")
    
    return potential_word_types

def find_related_words(word: str):
    words = [word]
    word_types = find_word_type(word)

    if "verb" in word_types:
        words.append(lemmatizer.lemmatize(word, pos="v"))
    if "adjective" in word_types:
        words.append(lemmatizer.lemmatize(word, pos="a"))
    
    return words

# lemmatizer.lemmatize("rocks")

while True:
    word = input("Input word: ")
    words = find_related_words(word)
    
    print(words)