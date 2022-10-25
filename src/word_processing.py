import numpy as np
import pandas as pd

from data.sentences import SENTENCES
from data.wordset import WORDSET
  

def equate_sentences():
  # iterate through sentences
  for (key, sentences) in SENTENCES.items():
    # declare variable to identify if sentences are equal
    equal = False

    # Check if sentences has an equal number of words
    if len(sentences[0].split()) != len(sentences[1].split()):
      print(f"Sentence pair {key}: does not have an equal number of words")
    else:
      # check if either word in tuple appears in each sentence.
      for word1, word2 in WORDSET:
        if (word1 in sentences[0] or word1 in sentences[1]) and (word2 in sentences[0] or word2 in sentences[1]):
          # set sentences to equal
          equal = True
          print_info(word1, word2, sentences)


      print(f"Sentence pair {key} is equal!") if equal else  print(f"Sentence pair {key} is unequal!")
      print("----------------------------")


def tuple_processing():
  # Gather first words in tuples
  first_words = [words[0] for words in WORDSET]
  
  # count how man times words appear in list of tuples
  word_count = pd.value_counts(np.array(first_words))
  
  # get only those words that appear 2 times
  duplicate_words = word_count.where(word_count == 2).dropna()
  
  # if first word is duplicate, create new tuples from second words.
  # e.g. (a, b), (a, c) - "a" is duplicate, so (b, c) will be created
  new_words = []
  for word1, word2, in WORDSET:
    if word1 in duplicate_words:
      new_words.append(word2)
  new_tuples = list(zip(*[iter(new_words)]*2))
  
  # Add new tuples to original WORDSET list
  WORDSET.extend(new_tuples)
  

# separate logic for printing
def print_info(word1, word2, sentences):
  print(f'Word pair: ({word1} , {word2}) --- Sentences: "{sentences[0]}" | "{sentences[1]}"')
