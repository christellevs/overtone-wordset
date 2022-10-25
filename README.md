# Wordsets

## Overview

This project took around 3 hours to complete.

The original idea is explained in the original README (see below).

If I had more time to complete this implementation I would improve the algorithms I used to equate the sentences to make the process run faster, and also include some unit testing.

### Implementation Summary

- Included a list of tuples to keep the word pairs e.g. `[(eat, consume), (easy, simple)]`
- Included a dictionary holding a list of sentences groups to be equated e.g.:

  - (This was to keep the code cleaner for reading, could also have used a list of tuples instead)

    ```
    SENTENCES = {
    1: ["She wants to eat food.", "She wants to consume food."],
    2: ["She wants to drink water.", "She wants to consume food."],
    }
    ```

- Iterate through the sentences and:
  - Check if the sentences are of equal length
  - Iterate through word pairs and check if sentences equate in meaning
- If Exercise 2 was actived:

  - A function would run to create new word pairs and add to the original list of tuples.

    E.g. if list was originally: `[(a, b), (a, c), (d, e)]`.

    The new list would be: `[(a, b), (a, c), (d, e), (b, c)]`

  - The function to equate the sentences would run as normal, as it did for exercise one.

### Testing results:

If you go to `overtone-wordset/src/main.py` you will see a variable called:

`EXERCISE_TWO = False`

Set this to `EXERCISE_TWO = True` if you want to activate the word pair implication.

#### Example:

If Exercise 2 is set to `False`:

- Sentence pair 7 should NOT be equal.

If Exercise 2 is set to `True`:

- Sentence pair 7 should be equal.

## To run this project:

(For Linux/MacOS)

1 - First clone the repo:

`git clone https://github.com/christellevs/overtone-wordset.git`

2 - Then cd into project folder:

`cd overtone-wordset/`

3 - Create a new Python virtual environment:

`python -m venv .env`

4 - Activate your virtual environment:

`source .env/bin/activate`

5 - Install required packages:

`pip install -r requirements.txt`

6 - Go into source folder to run main file:

`cd src/`

7 - Run main Python file:

`python main.py`

---

# Overtone

1.  You are given a set of synonyms, such as (eat, consume) and (easy, simple).

    Using this set, determine if two sentences with the same number of words are equivalent.
    In this example, we define the following two sentences to be equivalent:

    - "She wants to eat food."
    - "She wants to consume food."

    Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c). Consider
    for example the case of (coach, bus) and (coach, teacher).

    Ignore cases in which a
    word has two different meanings but the same spelling, such as (lead, lead).

2.  Given the above, what if we can now assume that (a, b) and (a, c) do in fact imply
    (b, c)?
