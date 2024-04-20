"""
Aaron S.
Week 5 Workshop: Guess the number game
04/20/2024
"""

import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    
    while tries != 0:
        print(f"Number of tires left: {tries}")
        guess = int(input("Guess a number between 0 and 10: "))
        
        if guess == target:
            print("Congratulations! You've guessed the number correctly.")
            return
        elif guess < target:
            print("Guess higher!")
        else:
            print("Guess lower!")
        
        tries -= 1
    
    print("Sorry, you didn't guess the number. Better luck next time!")

# if __name__ == "__main__":
#    guess_random_number(5, 0, 10)



# Task 2: Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)
    print(f"Target number: {target_number}")

    for guess in range(start, stop + 1):
        if tries == 0:
            print("Out of tries!")
            return
        print(f"Trying with: {guess}")
        if guess == target_number:
            print("Success! The computer guessed the number.")
            return
        tries -= 1

    print("Failed to guess the number within the tries provided.")

# if __name__ == "__main__":
#    guess_random_num_linear(5, 0, 10)



#task 3 - random number guessing game with binary search
def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    low = start
    high = stop
        
    print(f"Number to guess: {target}")
    
    while tries != 0:
        print(f"Number of tries left: {tries}")
        guess = (low + high) // 2
            
        if guess == target:
            print("Congratulations! You've guessed the number correctly.")
            return
        elif guess < target:
            print("Guess higher!")
            low = guess + 1
        else:
            print("Guess lower!")
            high = guess - 1
            
        tries -= 1
        
    print("Sorry, you didn't guess the number. Better luck next time!")
    
if __name__ == "__main__":
    guess_random_num_binary(5, 0, 100)