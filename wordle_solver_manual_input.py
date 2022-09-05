#Wordle Solver
#copyright 2022 Rebecca Schwab

import random

# This code imports the word lists
# I've uploaded the two word lists for you to use
# After you download the word lists, you'll need to adjust the file paths below to reflect where files are stored on your computer.

with open(r"C:\Users\Rebecca\Desktop\Wordle Solver\answers.txt") as answers_file:
  wordle_answers = answers_file.read().split()

with open(r"C:\Users\Rebecca\Desktop\Wordle Solver\allowed.txt") as allowed_file:
    allowed_guesses = allowed_file.read().split()

# This code combines the two word lists and shuffles them so the answers list is mixed in with the allowed guesss list
full_word_list = allowed_guesses + wordle_answers
full_list_shuffled = random.sample(full_word_list, len(full_word_list))

# The next set of variables are where you will manually enter what you know so far. I've left examples in th code so you can follow the correct format.

# If you know a letter is in the word, enter it here in string format, regardless of its position in the word. 
# Make sure the letters are within a list/array, or the program won't run correctly.
# Make sure you delete any of my letters if they aren't in your word.

known_letters = ['r', 'e', 'u']

# Enter any letters you've eliminated below. Again, I've left examples in here. 
# Make sure you delete any of my letters if you haven't elminated them from your word.

eliminated = ['h', 't', 'i', 'n', 'm', 'o', 'a', 'b', 'y', 'l', 'c']

# You're going to use those known letters again. Now, we have two lists/arrays that account for correct and incorrect positions in the word.
# First, if you know the correct position of the word within the letter, you'll enter the position and the letter in the 'known_position' variable below.
# Don't forget that Python is zero-indexed, so you'll start at 0 when you count the position of the letter in the word.
# As always, make sure you delete any of my letters if they don't belong in the current list.

known_position = [[0, 'r'], [1, 'u'], [3, 'e'], [4, 'r']]

# Here's where we can account for a letter where you know it's in the word, but you have it in the wrong position.
# Important: if you have the same letter in the correct position, but also know positions where it is NOT located, 
# you can enter it in both the 'known_position' and 'wrong_position' lists. 
# You can also enter the same letter multiple times in each list if you have that info.
# These are the little details that really help the program narrow down the possibilities.

wrong_position = [[2, 'r'], [3, 'u'], [4, 'e']]
 
# This is the function that does the work

def solve_wordle():
    possible_words = set()
    for word in full_list_shuffled:
        has_eliminated = any([letter in word for letter in eliminated])
        if not has_eliminated:
            has_known = all([known in word for known in known_letters])
            if has_known:
                if known_position:
                    has_known_position = all([(word[pair[0]] == pair[1]) for pair in known_position])
                    if has_known_position:
                        has_wrong_position = any([(word[pair[0]] == pair[1]) for pair in wrong_position])
                        if not has_wrong_position:
                            possible_words.add(word)
                elif wrong_position:
                    has_wrong_position = any([(word[pair[0]] == pair[1]) for pair in wrong_position])
                    if not has_wrong_position:
                        possible_words.add(word)
                else:
                    possible_words.add(word)
    print(possible_words)                       

           
solve_wordle()
