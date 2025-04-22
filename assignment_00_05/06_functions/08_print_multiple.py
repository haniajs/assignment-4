def print_multiple(message: str, repeat: int):
    for i in range(repeat):
        print(message)

def main():
    message = input("\033[94m Enter a message: \033[0m")
    repeat = int(input("\033[94m Enter a number: \033[0m"))
    print_multiple(message, repeat)

if __name__ == '__main__':
    main()