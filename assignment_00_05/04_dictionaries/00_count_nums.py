def get_user_numbers():
    
    user_numbers = []
    while True:
        user_input = input("\033[94m Enter a number: \033[0m")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    return user_numbers

def count_nums(num_lst):
   
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
 
    for num in sorted(num_dict):
        count = num_dict[num]
        time_word = "time" if count == 1 else "times"
        print(f"{num} appears {count} {time_word}.")

def main():
  
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
