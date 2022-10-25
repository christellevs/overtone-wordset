from word_processing import equate_sentences, tuple_processing

# Change this to "True" if you want to activate exercise 2. E.g.:
# (a, b) and (a, c) do imply (b, c)
EXERCISE_TWO = False

if __name__ == "__main__":
  
  if not EXERCISE_TWO:
    # if exercise 2 is not activated equate sentences
    equate_sentences()
  else:
    # if exercise 2 is activated, first run script to create new tuples and then equate sentences
    tuple_processing()
    equate_sentences()
