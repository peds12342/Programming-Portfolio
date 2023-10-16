def count_upper_and_lower_letters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

input_string = ("Hello World")
upper, lower = count_upper_and_lower_letters(input_string)
print(f"Upper case letters: {upper}")
print(f"lower case letters: {lower}")