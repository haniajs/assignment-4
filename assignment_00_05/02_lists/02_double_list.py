def double_numbers(numbers):

    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled

def main():
    numbers = [1, 2, 3, 4]
    numbers = double_numbers(numbers)
    print("Doubled list: ", numbers)

if __name__ == '__main__':
    main()
