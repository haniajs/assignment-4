def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0
    for fruit, price in fruits.items():
        quantity = int(input(f"\033[1;3m How many ({fruit}) do you want to buy?: \033[0m"))
        total_cost += price * quantity

    print(f"Your total cost is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
