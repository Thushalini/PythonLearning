fruits = ["apple" , "banana" , "cherry" , "pappaya"]

for x in fruits:
    print(x)

for y in "love":
    print(y)
    if y == "v":
        break

for x in "lucky":
    if x == 'k':
        continue
    print(x)

for x in range(6):
    print(x)
for x in range(3,9):
    print(x)
else :
    print("Finally fiished.")
for x in range(3 , 30 , 5):
    if x == 18 : break
    print(x)
else:
    print("Finished!")
#if else doesn't work then loop stopped by break statement

#nested for loop
description = ("tasty" , "healthy")
food = ["apple" , "soup" , "salad"]

for x in description:
    for y in food:
        print(x,y)

for x in "father":
    pass


