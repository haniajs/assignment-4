def main():
    # Dictionary of planet gravity ratios compared to Earth
    gravity_ratios = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Prompt user for Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt user for planet name
    planet = input("Enter a planet: ")

    # Check if planet is valid and calculate weight
    if planet in gravity_ratios:
        planet_weight = round(earth_weight * gravity_ratios[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please try again.")

if __name__ == "__main__":
    main()

