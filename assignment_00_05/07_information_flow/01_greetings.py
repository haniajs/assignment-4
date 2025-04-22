def main():
    name = input("\033[1;3m What's your name? \033[0m")
    greet(name)

def greet(name):
    print("Greetings " + name + "!")

if __name__ == '__main__':
    main()
