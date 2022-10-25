from data.sentences import SENTENCES
from data.wordset import WORDSET


def print_sentences():
  print(SENTENCES)
  
def print_wordset():
  print(WORDSET)
  

def equate_sentences():
  for (key, sentences) in SENTENCES.items():
    equal = False
    if len(sentences[0].split()) != len(sentences[1].split()):
      print(f"Sentece pair: {key} does not have an equal number of words")
    else: 
      for words in WORDSET:
        if (words[0] in sentences[0] or words[0] in sentences[1]) and (words[1] in sentences[0] or words[1] in sentences[1]):
          equal = True
      print(f"Sentence pair {key} is equal!") if equal else  print(f"Sentence pair {key} is unequal!")

def tuple_processing():
  for words in WORDSET:
    print(f"{words}")
