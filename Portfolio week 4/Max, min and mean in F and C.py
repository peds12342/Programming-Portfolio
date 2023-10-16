def main():
    temperature_celsius = []

    for i in range(6):
        user_input = input(f"Enter temperature {i + 1} in degrees Celsius (e.g., 25C): ")
        if user_input[-1] == 'C':
            try:
                celsius_temp = float(user_input[:-1])
                temperature_celsius.append(celsius_temp)
            except ValueError:
                print("Invalid input. Please enter a valid number followed by 'C'.")
                return
        else:
            print("Invalid input format. Please enter a temperature in degrees Celsius with 'C' suffix.")
            return

    max_temp_celsius = max(temperature_celsius)
    min_temp_celsius = min(temperature_celsius)
    mean_temp_celsius = sum(temperature_celsius) / len(temperature_celsius)

    print(f"Maximum temperature: {max_temp_celsius}°C")
    print(f"Minimum temperature: {min_temp_celsius}°C")
    print(f"Mean temperature: {mean_temp_celsius}°C")

if __name__ == "__main__":
    main()
