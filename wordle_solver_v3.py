#Wordle Solver
#copyright 2022 Rebecca Schwab

import random
import time
import string

#Variables for time.sleep()
a = 2
b = 3
c = 4
d = 5

# This code imports the word lists

with open('./answers.txt') as answers_file:
  wordle_answers = answers_file.read().split()

with open('./allowed.txt') as allowed_file:
    allowed_guesses = allowed_file.read().split()

# The next 4 variables will store the inputs: 

known_letters = []

eliminated = []

known_position = []

wrong_position = []

          
# This is the linear search function that checks the word lists againt the inputted letters:
def solve_wordle():
    possible_words = set()
    # This code combines the two word lists and shuffles them so the answers list is mixed in with the allowed guesss list
    full_word_list = allowed_guesses + wordle_answers
    full_list_shuffled = random.sample(full_word_list, len(full_word_list))

    for word in full_list_shuffled:
        #Check if the word has any of the eliminated letters
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
    print(*possible_words, sep="\n")
    print("")                       

# This is a helper function for the yes or no inputs
def helper_yn(question):
    choice = ''
    while choice.lower() not in ('y', 'n'): 
        choice = input(question)
        if choice.lower() in ('y', 'n'):
            return choice
            #break
        else:
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            print("")
            time.sleep(a)

# Helper function for number inputs
def helper_num():
    while True:
        position = (input("Enter one or more numbers between 1 & 5 now: "))
        position_integers = []
        try:
            for i in position.split():
                position_integers.append(int(i))
        except ValueError as e:
            print("")
            time.sleep(a)
            print("I'm sorry, you entered something that isn't a number between 1 & 5.")
            print("")
            time.sleep(a)
            print("Please try again.")
            print("")
            time.sleep(a)
            continue

        in_range = all(n in range(1, 6) for n in position_integers)                
                 
        if not position_integers or not in_range:
            print("")
            time.sleep(a)
            print("I'm sorry, you entered something that isn't a number between 1 & 5.")
            print("")
            time.sleep(a)
            print("Please try again.")
            print("")
            time.sleep(a)
        else:
            return position_integers
            #break

# Helper function for letter inputs
def helper_alpha(question):
    alphabet=list(string.ascii_lowercase)
    letters_list = []
    while True:
        letters = input(question).lower()
        for l in letters.split():
            letters_list.append(l)
        in_alpha = all(l in alphabet for l in letters_list)                              
        if not in_alpha:
            print("")
            time.sleep(a)
            print("I'm sorry, you entered something other than letters and spaces.")
            print("")
            time.sleep(a)
            print("Let's try that again")
            print("")
            time.sleep(a)
        else:
            return letters_list
    

#Intro that explains how the program works:
def intro():
    print("")
    print("")
    print("Welcome to my Wordle Solver!")
    print("")
    time.sleep(a)
    q_intro = "Do you want me to play the intro? Y/N: "
    need_intro = helper_yn(q_intro)
     
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
        print("")
        time.sleep(c)
        
       
        q_start = "Are you ready to get started? Y/N: "
        get_started = helper_yn(q_start)
            
        if get_started.lower() == "y":
            print("")
            time.sleep(a)
            print("Ok, great! Here we go!")
            print("")
            time.sleep(a)
            #runs the get_eliminated function
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
    q_eliminated = "Have you eliminated any letters from the word? Y/N: "
    any_eliminated = helper_yn(q_eliminated)
    
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
            #Loop makes sure the input is letters only
            q_alpha = "Enter the eliminated letters now: "
            enter_eliminated = helper_alpha(q_alpha)
            for letter in enter_eliminated:
                eliminated.append(letter)
            print("")
            time.sleep(a)
            #runs the get_known function
            get_known()

    else:
        print("")
        time.sleep(a)
        print("Ok, we'll move on then.")
        print("")
        time.sleep(a)
        #runs the get_known function
        get_known()

# This function lets you input the known letters
def get_known():
    print("Next, let's talk about the letters you know are in the word.")
    q_known = "Are there any letters you know? Y/N: "
    any_known = helper_yn(q_known)
    
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
            #Loop makes sure the input is letters only
            q_alpha = "Enter the known letters now: "
            enter_known = helper_alpha(q_alpha)
            for letter in enter_known:
                known_letters.append(letter)
            print("")
            time.sleep(a)
            #runs the get_positions function
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
        #run the solve_wordle function based on eliminated letters only
        solve_wordle()

#This function let you input the correct and incorrect position of the known letters
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
        q_correct_p = f"Do you know any correct positions of {letter}? Y/N: "
        know_correct_position = helper_yn(q_correct_p)
        
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
            #Loop make sure the input is numbers between 1 & 5 only
            correct_position = helper_num()
            
            for n in correct_position:
                known_position.append([int(n) - 1, letter])
                                
        print("")
        time.sleep(a)
        q_incorrect_p = f"Do you know any incorrect positions of {letter}? Y/N: "
        know_incorrect_position = helper_yn(q_incorrect_p)
        
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
            #Loop make sure the input is numbers between 1 & 5 only
            incorrect_position = helper_num()
            for n in incorrect_position:
                wrong_position.append([int(n) - 1, letter])
                #print(wrong_position)
                print("")
                time.sleep(a)
        else:
            print("")
            time.sleep(a)
                       
    #runs the solve_wordle function 
    solve_wordle()


intro()
