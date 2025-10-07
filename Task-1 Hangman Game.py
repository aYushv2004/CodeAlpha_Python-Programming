import random

word_list = ["apple", "table", "chair", "water", "house", "music", "train", "phone", "smile", "bread"]
chosen_word = random.choice(word_list)
display_word = ["_" for _ in chosen_word]
incorrect_guesses_limit = 6
incorrect_guesses = 0
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display_word))
while incorrect_guesses < incorrect_guesses_limit and "_" in display_word:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {incorrect_guesses_limit - incorrect_guesses} guesses left.")

    print(" ".join(display_word))
if "_" not in display_word:
    print(f"Congratulations! You guessed the word: {chosen_word}")
else:
    print(f"You ran out of guesses! The word was: {chosen_word}")