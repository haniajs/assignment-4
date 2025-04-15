def main():

    C: int = 299792458 
    
    while True:
        user_input = input("\033[1;3m Enter kilos of mass (or type 'stop' to exit): \033[0m")

        if user_input.lower() == 'stop':
            print("Goodbye!")
            break

        try:
            mass_in_kg: float = float(user_input)

            # Calculate energy
            energy_in_joules: float = mass_in_kg * (C ** 2)

            # Display work to the user
            print("e = m * C^2...")
            print("m = " + str(mass_in_kg) + " kg")
            print("C = " + str(C) + " m/s")
            print(str(energy_in_joules) + " joules of energy!\n")
        except ValueError:
            print("Please enter a valid number for mass.\n")

if __name__ == '__main__':
    main()
