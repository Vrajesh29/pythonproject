# I am going to make a very very simple game called hangman.
import time
# To make a time gap of few seconds(here).

import random
#To select a random number from a given list.

player_name = input("Enter your name ")
# Let's start by asking player's.

time.sleep(2)
# Wait for 2 seconds after entering the game.

print("Hello! " + player_name + ", Let's play Hangman!!!" )
# Give a welcome message.

time.sleep(2)
# wait for 2 second after giving welcome message.

words_list = ['vrajesh', 'computing', 'python', 'time', 'random', 'hangman', 'hackerrank', 'codechef', 'codeforces',
              'writing', 'iit_gandhinagar', 'mobile', 'covid', 'canvas', 'assignments', 'project', 'tutor', 'instructor',
              'grades', 'counter_strike', 'pycharm', 'google', 'internet', 'software', 'hardware', 'component', 'motherboard',
              'rockpaper', 'rockscissor', 'paperscissor', 'lalminar', 'metis', 'television', 'reserved', 'cricket',
              'ms_dhoni', 'kl_rahul', 'batsman', 'bowler', 'physics','mathematics', 'precision', 'learning', 'procrastination',
              'ab_d_villiers', 'scarlletjohansson', 'robert_downey', 'tony_stark', 'natasha', 'black_widow', 'foundation_program',
              'pv_sindhu', 'irodov', 'resnick_halliday', 'arihant', 'hc_verma', 'sl_loney', 'vikas_gupta', 'calculus', 'wave_optics',
              'ray_optics', 'cordinate_geometry', 'fluid_mechanics', 'thermodynamics', 'stephen_hawking', 'stephen_fleming', 'albert_einstein',
              ]



word = random.choice(words_list)
# Let's take a random word from the list of given words.

print("Guess a character or characters")

total_guesses = " "

chances = 15
# number of wrong entered terms that can be allowed.

while chances > 0:
    number_of_times_failed = 0
    # we need to calculate the number of times the player fails so let it's initial value be 0.
    guess = input("Guess a character or characters:")
    # if player has input a wrong input then it will ask the player to enter a new number.

    total_guesses = total_guesses + guess
    # total guesses will be stored here.


# let's take first case. Here if the character or characters are correct then it will print the characters at places where they come else it will leave the place blank.
    for character in word:
    # checking wheter the selected character is in our word or not.

        if character in total_guesses:
            print(character)
        # if our character is in word then it will input a word else give the message in else part.

        else:
            print("_")
            number_of_times_failed = number_of_times_failed+1
             # if our character is not in the word then it will increase the nunber of failures till we reach a total of 15.

    # if all the characters are correct then below wil be case.
    if number_of_times_failed == 0:
        print("Congratulations! " + player_name + ", You have won the game!!")
        # if the number of failures are zero then player will win.

        print("The word is: ", word)
        # this will print the entered word if it is randomly selected by computer and you guessed it correctly.

        break
        #if a player has won then we need to break out from the while loop.



    # let's take the last and final case.
    if guess not in word:
        # check wheter the input character or characters is in the word or not.

        chances = chances - 1

        print("Incorrect character or characters")
        # if the input character or characters is not in the randomly selected word then it will give the above output.

        print("You have", + chances, ' more guesses')
        # it will print the number of terms left for a player.

        if chances == 0:
            print("You Lost")
            print("The correct answer is: " + word)
            # when the player has used all his 15 chances then it prints the above message and along with it it gives the correct word.