# germanic-english-translator
Translate your English to be as Germanic as possible, eliminating most if not all Latinate and foreign roots!

## Setup
Install prerequisites:
```sh
pip install --user -U nltk
pip install --user -U numpy
pip install ety
```

Install corpora within Python interactive shell:
```python
>>> import nltk
>>> nltk.download()
```

From there, download the "wordnet" corpus.

Also, run this command:
```python
>>> nltk.download("punkt")
```

## Credits
Heavy credits to the Germanic Thesaurus available
[here](https://docs.google.com/spreadsheets/d/1x-GB6AjZu_CYlxTit1n260i6xV9qxZXQk1N9X4oJAPI/edit).
