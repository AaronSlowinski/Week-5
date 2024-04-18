import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    
    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = int(input("Enter your guess: "))
        
        if guess == target:
            print("Congratulations! You've guessed the number correctly.")
            return
        elif guess < target:
            print("Guess higher!")
        else:
            print("Guess lower!")
        
        tries -= 1
    
    print("Sorry, you didn't guess the number. Better luck next time!")