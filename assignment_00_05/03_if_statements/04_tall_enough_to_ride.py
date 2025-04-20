def main():
    MIN_HEIGHT = 50 

    while True:
        height_input = input("\033[1;3m How tall are you? \033[0m")

        if height_input.strip() == "":
            print("Goodbye!")
            break

        try:
            height = int(height_input)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
