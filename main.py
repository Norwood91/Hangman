import random

word_list = ['Peter', 'Stewie', 'Meg', 'Brian', 'Chris', 'Louis', 'Bart', 'Homer', 'Maggie', 'Lisa', 'Marge']

chosen_word = random.choice(word_list).lower()
print(chosen_word)

placeholder = ''

for char in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

user_guess = input("Please guess a letter: ").lower()

display = ''

for letter in chosen_word:
    if letter == user_guess:
        display += letter
    else:
        display += '_'
print(display)

