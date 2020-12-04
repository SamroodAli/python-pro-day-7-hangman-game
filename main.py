#Step 5
import hangman_art
import hangman_words
import random
from os import system, name 
  


# I did not write this code, copied from stack overflow,to clear the shell every new game.Keeping things clean ;)
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

playing = True
while playing:
    clear()

    #Update the word list to use the 'word_list' from hangman_words.py

    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

 
    print(hangman_art.logo +'\n\n\n')

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    print('WELCOME TO HANGMAN.\n\n ')
    print(f"There are {word_length} letters in the word. \n\nYou start with 6 lives. Enjoy the game\n")
    print(' '.join(display)+'\n')
    guessed_letters=[]

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        #If the user has entered a letter they've already guessed, print the letter and let them know.

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word and guess not in guessed_letters:
            #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"you have guessed {guess} which is not in the word and so, you lose a life, sorry.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}")

        if guess in guessed_letters:
            print(f"You already guessed {guess}")
        else:
            guessed_letters += guess

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(hangman_art.stages[lives])
        # code to check if playing again.
        if end_of_game:
            playing_again=input("\nDo you want to play again ? Y or No:\n").lower()
            if playing_again =='n':
                playing = False