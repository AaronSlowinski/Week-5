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

if __name__ == "__main__":
    guess_random_number(5, 0, 10)
































#task 3 - random number guessing game with binary search
def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    low = start
    high = stop
        
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