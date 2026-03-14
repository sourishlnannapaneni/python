import random
word_list = ["Java", "Python", "Telugu", "Birthday", "Workplace", "School", "Homework"]

def jumble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

def get_hint(word):
    return f"The first letter of the word is:{word[0].upper()}"

def play_game():
    score = 0
    round = 5
    print("Welcome to the Word Jumble Game!")
    for round_number in range(1, round + 1):
        word = random.choice(word_list)
        scrambled_word = jumble_word(word)
        print("Your task is to guess the original word from the scrambled version.")
        print(f"\nRound : {round_number}")
        print(f"Here is the scrambled word = {scrambled_word}")
        hint_choice = input("Do you want to get a hint? (yes/no): ")
        if hint_choice == "yes":
            print(get_hint(word))
    
        guess = input("Guess the original word: ").lower()
        while not guess.isalpha():
            print("Please enter a valid word!")
            guess = input("Guess the original word: ").lower()
        
        if guess == word:
            print("Congratulations, you guessed it right!")
            score = score + 1
        else:
            print(f"You made a wrong guess. \n The correct word is: {word}")
    
    print(f"\nGAME OVER!\nYour final score is: {score}/{round}")

play_game()
