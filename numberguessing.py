#number guessing name using loops
secret = 7
attempts = 0

while True:
    guess = int(input("Guess a number: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break