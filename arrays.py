#lists as arrays
cars = ["volvo" , "Ford" , "BMW"]

x = cars[0]
print(x)

#change item
cars[0] = "Toyota"
print(cars[0])

#length of array
print(len(cars))

for x in cars:
    print(x)

#add an item in list
cars.append("Honda")

#remove item
#using index number
cars.pop(1)  #second item
#using name
cars.remove("volvo")

