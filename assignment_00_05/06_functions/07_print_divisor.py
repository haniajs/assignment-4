def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    num = int(input("\033[94m Enter a number: \033[0m"))
    print_divisors(num)

if __name__ == '__main__':
    main()
