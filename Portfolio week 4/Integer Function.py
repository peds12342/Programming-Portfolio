def is_integer_in_range():
    try:
        number = int(input("Enter an integer:"))
        return 0 <= number <= 100
    except ValueError:
        return False

result = is_integer_in_range()
print("Is the integer in the range 0 to 100?", result)