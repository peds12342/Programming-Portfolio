num = int(input("Please enter number here: "))
timestablesbackwards = [(7*12), (7*11), (7*10), (7*9), (7*8), (7*7), (7*6), (7*5), (7*4), (7*3), (7*2), (7*1), (7*0)]
if num in range(1, 13):
    print("Your number multiplied by 7 is", num * 7)
elif num in range(-13, 0):
    print(timestablesbackwards)