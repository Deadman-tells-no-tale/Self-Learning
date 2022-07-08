import random
winning_word = ["programming", "html","python", "csharp", "godot", "gdscript", "unity", "unreal engine", "alyssa", "nintendo"]
random_chose = random.choice(winning_word)
#generate a random word
unsolved= ""

#generate as many blanks as letters in the word
#get a varible from user of a letter

#create an aski print to show the hangman
#create a while loop that shows how many life is left
#create a counter that detects how many lives/guesses are left
#create a for loop to check if the letter in Range of the word
guessed_word = []
lives = 0
while lives < 9:
    user_guess = input("What letter would you like to guess?:").lower
    if guessed_word == random_chose:
        print("Congratulations you won!")
        print(f"You completed the phrase:",{guessed_word})
        break
    elif guessed_word != random_chose:
        for user_guess in random_chose:
                for guess in range (0, len(random_chose)):
                    if user_guess in winning_word[guess]:
                        print(user_guess)
                        guessed_word[guess] += user_guess
                    else:
                        print("_")
    else:
        lives +=1
        print(f"you have {lives} many guesses left!")
print("Game Over!")
