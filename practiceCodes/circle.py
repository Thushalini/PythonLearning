print("Calculate the circle's diameter,circumference and area")

#take user input as a float number
radius = float(input(f"Enter radius:"))
print("radius is" , radius)
#calculation
diameter = 2 * radius
circumference = 2 * 22 / 7 * radius
area = 22 / 7 * radius * radius

print("Circle's diameter:",diameter)
print("Circle's circumference:",circumference)
print("Circle's area:",area)
