import random
from hangman_art import stages
from word_file import word_list

words = word_list

stage_images = stages

lives = 6

chosen_word = random.choice(words).lower()

placeholder = ''

for char in range(len(chosen_word)):
    placeholder += '_'

print()
print("WELCOME TO HANGMAN, created by Robert L. Norwood!")
print("Good luck and have fun!")
print("*****************************************")
print()
print(f"Word to guess: {placeholder}")
print(stage_images[6])

game_running = True

correct_letters = []

while game_running:

    print(f"You currently have {lives} lives left!")
    user_guess = input("Please guess a letter: ").lower()

    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}, please guess again!")

    display = ''

    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)


    if user_guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {user_guess}, but that letter isn't in the word. You lose a life!")
        if lives == 0:
            game_running = False
            print("YOU LOSE! The correct word was: ", chosen_word)
            print("Better luck next time.")

    if '_' not in display:
        game_running = False
        print("YOU WIN, great job!")

    print(stage_images[lives])




