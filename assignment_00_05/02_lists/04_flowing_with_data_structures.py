def add_three_copies(data_list, data):
    
    for _ in range(3):
        data_list.append(data)

def main():
    message = input("\033[1;3m Enter a message to copy:  \033[0m")
    messages = []

    print("List before:", messages)
    add_three_copies(messages, message)
    print("List after:", messages)

if __name__ == '__main__':
    main()
