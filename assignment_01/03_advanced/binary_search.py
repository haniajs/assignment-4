def binary_search(arr, target):
    """Perform binary search on a sorted list."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Found the target
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

def main():
    print("Binary Search Project")
    try:
        # Input list of numbers
        user_input = input("Enter a list of numbers separated by spaces: ")
        num_list = list(map(int, user_input.strip().split()))

        # Sort the list
        num_list.sort()
        print(f"Sorted List: {num_list}")

        # Input target value
        target = int(input("Enter the number to search for: "))

        # Perform binary search
        result = binary_search(num_list, target)

        if result != -1:
            print(f"✅ Target found at index {result}")
        else:
            print("❌ Target not found in the list.")
    except ValueError:
        print("⚠️ Invalid input. Please enter only integers.")

if __name__ == "__main__":
    main()
