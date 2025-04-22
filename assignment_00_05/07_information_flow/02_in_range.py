def in_range(n, low, high):
  
    return low <= n <= high

def main():
    print(in_range(5, 1, 10)) 
    print(in_range(0, 1, 10))  
    print(in_range(10, 1, 10)) 
    print(in_range(1, 1, 10))  
    print(in_range(11, 1, 10)) 

if __name__ == '__main__':
    main()
