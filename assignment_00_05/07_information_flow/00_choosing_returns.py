ADULT_AGE: int = 18 

def is_adult(age: int) -> bool:
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age: int = int(input("\033[1;3m How old is this person?: \033[0m"))
    print(is_adult(age))

if __name__ == "__main__":
    main()
