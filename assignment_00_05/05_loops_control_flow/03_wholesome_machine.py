AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("\033[94m Please type the following affirmation: \033[0m" + AFFIRMATION)

    user_feedback = input() 
    while user_feedback != AFFIRMATION:  
        print("That was not the affirmation.")
        print("\033[94m Please type the following affirmation: \033[0m" + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

if __name__ == '__main__':
    main()
