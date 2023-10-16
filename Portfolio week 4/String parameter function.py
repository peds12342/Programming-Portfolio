def remove_last_character(input_string):
    if len(input_string)<= 1:
        return input_string
    else:
        return input_string[: -1]

def main():
    input_string = input("Enter a string: ")
    modified_string = remove_last_character(input_string)
    print(f"Original: '{input_string}', Modified: '{modified_string}'")

if __name__ == "__main__":
    main()