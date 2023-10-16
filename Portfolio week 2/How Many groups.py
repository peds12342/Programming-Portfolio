students = input("How many students are there:")
group = input("What will be the size of the group: ")
groups = students // group
remainder = students % group
if groups == 1 and remainder == 1:
    print("There will be 1 group with student left over.")
elif groups == 1 and remainder != 1:
    print("There will be 1 group with", remainder,"students left over.")
elif groups != 1 and remainder == 1:
    print("There will be", groups, "groups with 1 student left over")
else:
    print("There will be ", groups, "groups with", remainder, "students left over.")
