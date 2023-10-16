password = input("Please enter password:")
password2 = input("Please enter password:")
if password == password2:
    print("Password is set.")
else:
    print("Password does not match.")
passlength = len(password)
if passlength in range(8, 13):
    print("Password is set.")
else:
    print("Password is too long.")
Bad_password = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
if password in Bad_password:
    print("Password bad, not angry just disappointed")