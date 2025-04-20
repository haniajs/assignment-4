def main():
    num1 = int(input("\033[1;3m Please enter a first number to be divided:  \033[0m"))
    num2 = int(input("\033[1;3m Please enter a second number to be divide by:  \033[0m"))
    
    quotient = num1 // num2
    remainder = num1 % num2
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
