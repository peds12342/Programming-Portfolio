def main():
    temperature_celsius = []

    while True:
        user_input = input("Enter a temperature in degrees Celsius (e.g., 25C), or press Enter to finish: ")

        if user_input == "":
            break

        if user_input[-1] == 'C':
            try:
                celsius_temp = float(user_input[:-1])
                temperature_celsius.append(celsius_temp)
            except ValueError:
                print("Invalid input. Please enter a valid number followed by 'C' or press Enter to finish.")
        else:
            print("Invalid input format. Please enter a temperature in degrees Celsius with 'C'at the end or press Enter to finish.")

    if not temperature_celsius:
        print("No temperatures entered.")
    else:
        max_temp_celsius = max(temperature_celsius)
        min_temp_celsius = min(temperature_celsius)
        mean_temp_celsius = sum(temperature_celsius) / len(temperature_celsius)

        print(f"Maximum temperature: {max_temp_celsius}°C")
        print(f"Minimum temperature: {min_temp_celsius}°C")
        print(f"Mean temperature: {mean_temp_celsius}°C")


if __name__ == "__main__":
    main()

