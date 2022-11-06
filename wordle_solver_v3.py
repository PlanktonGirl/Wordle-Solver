#Wordle Solver
#copyright 2022 Rebecca Schwab

import random
import time

a = 2
b = 3
c = 4
d = 5

# This code imports the word lists

with open(r"C:\Users\Rebecca\Desktop\Wordle Solver\answers.txt") as answers_file:
  wordle_answers = answers_file.read().split()

with open(r"C:\Users\Rebecca\Desktop\Wordle Solver\allowed.txt") as allowed_file:
    allowed_guesses = allowed_file.read().split()

# This code combines the two word lists and shuffles them so the answers list is mixed in with the allowed guesss list
full_word_list = allowed_guesses + wordle_answers
full_list_shuffled = random.sample(full_word_list, len(full_word_list))

# The next set of variables are where you will manually enter what you know so far. 

known_letters = ['r', 'e', 'u']

# Enter any letters you've eliminated below. 

eliminated = ['h', 't', 'i', 'n', 'm', 'o', 'a', 'b', 'y', 'l', 'c']

# This code lets you enter the positions of the letters you know.

known_position = [[0, 'r'], [1, 'u'], [3, 'e'], [4, 'r']]

# This code accepts the *incorrect* positions of the letters you know

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

           
#solve_wordle()

#Adding an intro for the user

def intro():
    print("")
    print("")
    print("Welcome to my Wordle Solver!")
    print("")
    time.sleep(a)
    print("Important note: This program assumes you're familiar with how to play Wordle")
    time.sleep(b)
    print("and that you've come here for help when you *just can't think* of a 5-letter word")
    time.sleep(c)
    print("that fits the letters you know and the ones you've eliminated.")
    time.sleep(c)
    print("")
    print("First, I'm going to ask you to enter any letters you've completely eliminated from the word.")
    time.sleep(c)
    print("Then, I'm going to ask you about the letters you know are in the word.")
    time.sleep(c)
    print("I'm going to ask you for the letter itself, and any correct or incorrect positions of the letter in the word.")
    time.sleep(d)
    print("")
    print("Once I have that information, I'll show you a list of all the 5-letter words that fit the criteria you've given me.")
    time.sleep(d)
    print("")
    print("It will be important that you follow my instructions exactly")
    time.sleep(c)
    print("or my program may not give you the correct answer(s).")
    time.sleep(c)
    
    while True:
        print("")
        get_started = input("Are you ready to get started? Y/N: ")
        if get_started.lower() not in ("y", "n"):
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            time.sleep(a)
        else:
            break
    if get_started.lower() == "y":
            print("")
            time.sleep(a)
            print("Ok, great! Here we go!")
            time.sleep(a)
    else:
        print("")
        time.sleep(a)
        print("No worries. Please come back when you're ready.")
        print("")
        time.sleep(a)

intro()