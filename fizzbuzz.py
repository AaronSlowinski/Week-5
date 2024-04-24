def fizzbuzz(num):
    # Loop through numbers from 1 to num
    for i in range(1, num + 1):
        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # If divisible by both, print "FizzBuzz"
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")  # If divisible by 3, print "Fizz"
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz")  # If divisible by 5, print "Buzz"
        else:
            print(i)  # If not divisible by either, print the number itself

# Testing the function with an argument of 50
fizzbuzz(50)
