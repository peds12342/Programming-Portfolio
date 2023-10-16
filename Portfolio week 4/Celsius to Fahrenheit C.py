def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

def main():
    user_input = input("Enter a temperature in degrees Celsius (eg. 250C): ")

    if user_input[-1] == 'C':
        try:
            celsius_temp = float(user_input[:-1])
            fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
            print(f"The temperature in Fahrenheit will be {fahrenheit_temp}F.")
        except ValueError:
            print("Invalid Input.Please enter a valid number followed by 'C'.")
    else:
        print("Invalid input format.Please enter a temperature in degrees celsius with 'C'.")

if __name__ == "__main__":
    main()