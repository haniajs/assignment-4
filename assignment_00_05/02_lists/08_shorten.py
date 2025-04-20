MAX_LENGTH = 3

def shorten(lst):
   
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

def main():
    
    sample_list = [10, 20, 30, 40, 50]
    shorten(sample_list)
    print("The final list is:", sample_list)

if __name__ == '__main__':
    main()
