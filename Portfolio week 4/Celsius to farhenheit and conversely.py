def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9 / 5) + 32
    return fahrenheit_temp


def farhenheit_to_celsius(farhenheit_temp):
    celsius_temp = (farhenheit_temp - 32) * 5 / 9
    return celsius_temp


def main():
    choice = input("Choose an option:\n1. Celsius to Fahrenheit\n2.Fahrenheit to Celsius\nEnter 1 or 2: ")

    if choice == "1":
        celsius_temp = float(input("Enter a temperature in degrees Celsius: "))
        farhenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"{celsius_temp}C is equal to {farhenheit_temp}F.")
    elif choice == "2":
        fahrenheit_temp = float(input("Enter a temperature in degrees Fahrenheit: "))
        celsius_temp = farhenheit_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp}F is equal to {celsius_temp}C.")
    else:
        print("Invalid choice.Please enter 1 or 2.")


if __name__ == "__main__":
    main()
