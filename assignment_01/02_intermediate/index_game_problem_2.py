def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Slice indices out of range."

def index_game():
    sample_list = [10, 20, 30, 40, 50] 
    print("Current List:", sample_list)

    while True:
        print("\nChoose an operation: access, modify, slice, or quit")
        choice = input("Enter choice: ").strip().lower()

        if choice == "access":
            idx = int(input("Enter index to access: "))
            result = access_element(sample_list, idx)
            print("Result:", result)

        elif choice == "modify":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
           
            try:
                new_val = int(new_val)
            except ValueError:
                pass
            result = modify_element(sample_list, idx, new_val)
            print("Updated List:", result)

        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(sample_list, start, end)
            print("Sliced List:", result)

        elif choice == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

index_game()
