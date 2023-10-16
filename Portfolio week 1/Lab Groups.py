students = 24
total = int(input("How many students will there be:"))
classes = total // students
remainder = total % students
print("There will be", classes,"classes, and a left over group of", remainder,"students")