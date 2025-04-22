def main():
    num: int = 7
    num = subtract_seven(num)
    print("This should be zero:", num)

def subtract_seven(num):
    return num - 7

if __name__ == '__main__':
    main()
