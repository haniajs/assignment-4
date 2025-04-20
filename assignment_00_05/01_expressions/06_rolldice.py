import random

def roll_dice(num_dice: int = 2, num_sides: int = 6):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls)
    
    print(f"Dice have {num_sides} sides each.")
    for i, roll in enumerate(rolls, start=1):
        print(f"Die {i}: {roll}")
    print(f"Total of {num_dice} dice: {total}")

def main():
    roll_dice()

if __name__ == '__main__':
    main()