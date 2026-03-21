import random
def hangman():
    words = ['hangman', 'telephone', 'science', 'laptop', 'pencil', 'stationary']
    word_to_guess = random.choice(words)
    guessed_word = ['_'] * len(word_to_guess)
    max_attempts = 6
    attempts = 0
    guessed_letters = []
    print('Welcome to the Hangman Game! \n Guess the word one letter at a time.')
    print('Word: ',''.join(guessed_word))
    print(f'You have {max_attempts} attempts to guess the word.')
    while (attempts < max_attempts) and ('_'in guessed_word):
        guess = input('\n Enter a letter: ').lower()
        if len(guess) != 1 or (not guess.isalpha()):
            print('Please enter a single valid letter.')
            continue
        # Check if guess is correct
        if guess in guessed_word:
            print('You already guessed that letter, try again.')
            continue
        guessed_letters.append(guess)
        if guess in word_to_guess:
            print(f'Good Guess!.{guess} is in the word')
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts += 1
            print(f'Wrong Guess.You have {max_attempts-attempts} attempts left')
        print('Word:',''.join(guessed_word))
    if '_' not in guessed_word:
        print(f'\nCongatulations! You guessed the word {word_to_guess}')
    else:
        print(f'\nGame Over! The word was {word_to_guess}')

hangman()
