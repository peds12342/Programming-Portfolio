num = int(input("Please enter number here: "))
if num in range(1, 13):
    print("Your number multiplied by 7 is", num * 7)
elif num not in range(1, 13):
    print("This number is not possible to be multiplied by 7, sorry")
