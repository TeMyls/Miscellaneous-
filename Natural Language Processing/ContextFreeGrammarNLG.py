import random

#Natural Language Generation
#Completely Written by ChatGPT

grammar = {
    "Sentence": [["NounPhrase", "VerbPhrase"]],
    "NounPhrase": [["Article", "Noun"]],
    "VerbPhrase": [["Verb", "NounPhrase"]],
    "Article": ["the", "a"],
    "Noun": ["dog", "cat", "man", "woman"],
    "Verb": ["sees", "likes", "pets"]
}

def generate(symbol):
    if symbol not in grammar:
        return symbol
    expansion = random.choice(grammar[symbol])
    if isinstance(expansion, str):
        return expansion
    return ' '.join(generate(sym) for sym in expansion)

print(generate("Sentence"))