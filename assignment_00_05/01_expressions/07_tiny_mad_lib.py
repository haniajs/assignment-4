sentence_start : str = "Panaversity is fun. I learned to program and used python to make my "

def main():
    adjective : str = input("\033[1;3m Enter an adjective and press enter: \033[0m")
    noun : str = input("\033[1;3m Enter a noun and press enter: \033[0m")
    verb : str = input("\033[1;3m Enter a verb and press enter: \033[0m")

    print(sentence_start + adjective + " " + noun + " " + verb + ".")

if __name__ == '__main__':
    main()
