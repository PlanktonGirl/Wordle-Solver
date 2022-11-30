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

known_letters = []

# Enter any letters you've eliminated below. 

eliminated = []

# This code lets you enter the positions of the letters you know.

known_position = []

# This code accepts the *incorrect* positions of the letters you know

wrong_position = []
 
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
    while True:
        print("")
        need_intro = input("Do you want me to play the intro? Y/N: ")
        if need_intro.lower() not in ("y", "n"):
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            time.sleep(a)
        else:
            break
    if need_intro.lower() == "n":
            print("")
            time.sleep(a)
            print("Ok, we'll get right to it then!")
            print("")
            time.sleep(a)
            get_eliminated()
    else:
        print("")
        print("This program assumes you're familiar with how to play Wordle")
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
            time.sleep(a)
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
            print("")
            time.sleep(a)
            get_eliminated()
        else:
            print("")
            time.sleep(a)
            print("No worries. Please come back when you're ready.")
            print("")
            time.sleep(a)

# This function lets you input the eliminated letters
def get_eliminated():
    print("First, let's address any letters you've eliminated.")
    while True:
        print("")
        time.sleep(a)
        any_eliminated = input("Have you eliminated any letters from the word? Y/N: ")
        if any_eliminated.lower() not in ("y", "n"):
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            time.sleep(a)
        else:
            break
    if any_eliminated.lower() == "y":
            print("")
            time.sleep(a)
            print("Ok, let's have you enter those letters now.")
            print("")
            time.sleep(a)
            print("Pleae type in the letters with a space in between each one in this format:")
            print("")
            time.sleep(a)
            print("a b c d e ")
            print("")
            time.sleep(a)
            print("If you enter the letters incorrectly, I won't be able to give you the right answers.")
            print("")
            time.sleep(a)
            while True:
                enter_eliminated = input("Enter the eliminated letters now: ").lower()
                if not enter_eliminated:
                    print("")
                    time.sleep(a)
                    print("I'm sorry, you didn't enter any info.")
                    print("")
                    time.sleep(a)
                else:
                    break
            print(enter_eliminated)
            for letter in enter_eliminated.split():
                eliminated.append(letter)
                print(eliminated)
            print("")
            time.sleep(a)
            get_known()

    else:
        print("")
        time.sleep(a)
        print("Ok, we'll move on then.")
        print("")
        time.sleep(a)
        get_known()

# This function lets you input the known letters
def get_known():
    print("Next, let's talk about the letters you know are in the word.")
    while True:
        print("")
        time.sleep(a)
        any_known = input("Are there any letters you know? Y/N: ")
        if any_known.lower() not in ("y", "n"):
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            time.sleep(a)
        else:
            break
    if any_known.lower() == "y":
            print("")
            time.sleep(a)
            print("Ok, let's have you enter those letters now.")
            print("")
            time.sleep(a)
            print("Pleae type in the letters with a space in between each one in this format:")
            print("")
            time.sleep(a)
            print("a b c d e ")
            print("")
            time.sleep(a)
            print("If you enter the letters incorrectly, I won't be able to give you the right answers.")
            print("")
            time.sleep(a)
            while True:
                enter_known = input("Enter the known letters now: ").lower()
                if not enter_known:
                    print("")
                    time.sleep(a)
                    print("I'm sorry, you didn't enter any info.")
                    print("")
                    time.sleep(a)
                else:
                    break
            print(enter_known)
            for letter in enter_known.split():
                known_letters.append(letter)
                print(known_letters)
            print("")
            time.sleep(a)
            get_positions()
       
    else:
        print("")
        time.sleep(a)
        print("Ok, we'll just check the eliminated word against the Wordle word lists.")
        print("")
        time.sleep(a)
        print("Hang tight")
        print("")
        time.sleep(a)
        print("")
        time.sleep(a)
        solve_wordle()


def get_positions():
    print("Finally, I'm going to have you enter the positions of the letters you know.")
    print("")
    time.sleep(a)
    print("When I say, 'position,' I mean where letter is located in the word.")
    print("")
    time.sleep(a)
    print("Like this:")
    print("")
    time.sleep(a)
    print("t h e i r")
    print("1 2 3 4 5")
    print("")
    time.sleep(a)
    for letter in known_letters:
        while True:
                know_correct_position = input(f"Do you know any correct positions of {letter}? Y/N: ")
                if know_correct_position.lower() not in ("y", "n"):
                    print("")
                    time.sleep(a)
                    print("I'm sorry, I didn't understand that.")
                    print("")
                    time.sleep(a)
                    print("Please answer 'Y' or 'N'")
                    time.sleep(a)
                else:
                    break
        if know_correct_position.lower() == "y":
            print("")
            time.sleep(a)
            print(f"Ok, let's have you enter the correct position(s) of {letter}.")
            print("")
            time.sleep(a)
            print(f"Please enter the position of {letter} as a number between 1 & 5.")
            print("")
            time.sleep(a)
            print("Remember, like this:")
            print("")
            time.sleep(a)
            print("t h e i r")
            print("1 2 3 4 5")
            print("")
            time.sleep(a)
            print(f"If you know more than one correct position of {letter} in the word,")
            time.sleep(c)
            print("please enter the number of each position separated by a single space")
            time.sleep(c)
            print("just like you did when you entered the letters.")
            print("")
            time.sleep(a)
            while True:
                correct_position = (input("Enter one or more numbers between 1 & 5 now: "))
                correct_position_integers = [int(number) for number in correct_position.split()]
                print(correct_position_integers)
                in_range = all(n in range(1, 6) for n in correct_position_integers)                
                print(in_range)                
                if not in_range:
                    print("")
                    time.sleep(a)
                    print("I'm sorry, you entered something that isn't a number between 1 & 5.")
                    print("")
                    time.sleep(a)
                    print("Please try again.")
                    print("")
                    time.sleep(a)
                else:
                    break
            for number in correct_position.split():
                known_position.append([int(number) - 1, letter])
                print(known_position)
                
        print("")
        time.sleep(a)
        while True:
            know_incorrect_position = input(f"Do you know any incorrect positions of {letter}? Y/N: ")
            if know_incorrect_position.lower() not in ("y", "n"):
                print("")
                time.sleep(a)
                print("I'm sorry, I didn't understand that.")
                print("")
                time.sleep(a)
                print("Please answer 'Y' or 'N'")
                time.sleep(a)
            else:
                break
        if know_incorrect_position.lower() == "y":
            print("")
            time.sleep(a)
            print(f"Ok, let's have you enter any wrong position(s) of {letter}.")
            print("")
            time.sleep(a)
            print(f"Please enter the wrong position(s) of {letter} as a number between 1 & 5.")
            print("")
            time.sleep(a)
            print("Remember, like this:")
            print("")
            time.sleep(a)
            print("t h e i r")
            print("1 2 3 4 5")
            print("")
            time.sleep(a)
            print(f"If you know more than one wrong position of {letter} in the word,")
            time.sleep(c)
            print("please enter each the number of each position separated by a single space")
            time.sleep(c)
            print("just like you did when you entered the letters.")
            print("")
            time.sleep(a)
            while True:
                incorrect_position = (input("Enter one or more numbers between 1 & 5 now: "))
                incorrect_position_integers = [int(number) for number in incorrect_position.split()]
                print(incorrect_position_integers)
                in_range_incorrect = all(n in range(1, 6) for n in incorrect_position_integers)                
                print(in_range_incorrect)                
                if not in_range_incorrect:
                    print("")
                    time.sleep(a)
                    print("I'm sorry, you entered something that isn't a number between 1 & 5.")
                    print("")
                    time.sleep(a)
                    print("Please try again.")
                    print("")
                    time.sleep(a)
                else:
                    break
            for number in incorrect_position.split():
                wrong_position.append([int(number) - 1, letter])
                print(wrong_position)
                print("")
                time.sleep(a)
        else:
            print("")
            time.sleep(a)
                       

    solve_wordle()




#get_eliminated()
intro()
#get_known()
#get_positions()