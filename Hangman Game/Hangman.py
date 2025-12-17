import random


words = ["apple", "banana", "cherry", "date", "elderberry"]

word = random.choice(words)


guessed = set()


incorrect = 0
max_incorrect = 6


while incorrect < max_incorrect and not all(c in guessed for c in word):

    display = ''.join([c if c in guessed else '_' for c in word])
    print(f"\nWord: {display}")
    print(f"Guessed letters: {', '.join(sorted(guessed))}")
    print(f"Incorrect guesses left: {max_incorrect - incorrect}")
    
    
    guess = input("Guess a letter: ").lower()
    
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    
    
    guessed.add(guess)
    
    
    if guess in word:
        print("Good guess!")
    else:
        incorrect += 1
        print("Wrong guess!")


if incorrect == max_incorrect:
    print(f"\nYou lost!!!! The word was '{word}'.")
else:
    print(f"\nYou won!!!! The word was '{word}'.")