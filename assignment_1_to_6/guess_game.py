import random

def guess_the_number():
    number = random.randint(1, 100)
    guesses_left = 7
    print("Welcom to the number guessing game!")
    print("I am thinking a number between 1 to 100.")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess of another number: "))
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue

        if guess < number:
            print("Too low number. Tell the another!")
        elif guess > number:
            print("Too high number. Tell the another!")
        else:
            print(f"Congratulation! you got the correct number in {7 - guesses_left + 1} tries.")
            return
        
        guesses_left -= 1
        print(f"\nYou run out of guess. The number was {number}.")

guess_the_number()
