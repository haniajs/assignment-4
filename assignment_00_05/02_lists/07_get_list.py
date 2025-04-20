def main():
    values = []
    while True:
        user_input = input(f"\033[94m Enter a value: \033[0m")
        if user_input == "":
            break
        values.append(user_input)
    print("Here's the list:", values)

if __name__ == '__main__':
    main()
