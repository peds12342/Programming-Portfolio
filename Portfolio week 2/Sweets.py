sweets = int(input("How many sweets:"))
students = int(input("How many students:"))
forstudents = sweets // students
remainder = sweets % students
if forstudents == 1 and remainder == 1:
    print("Each pupil will get 1 sweet and there will be 1 sweet left over")
elif forstudents == 1 and remainder != 1:
    print("Each pupil will get 1 sweet and there will be", remainder, "sweets left over")
elif forstudents != 1 and remainder == 1:
    print("Each pupil will get", forstudents, "and there will be 1 student left over")
else:
    print("Each pupil will get", forstudents,"sweets and there will be", remainder,"sweets left over")