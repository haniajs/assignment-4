def print_one_digit(num):
    print("The one digit is:", num % 10)

def main():
    num = int(input("\033[94m Enter a number: \033[0m"))
    print_one_digit(num)

if __name__ == '__main__':
    main()
