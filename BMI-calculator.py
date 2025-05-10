height = float(input("Enter your height(In m):"))
weight = float(input("Enter yout weight(In kg):"))

BMI = weight / (height * height)

print("Your BMI :" , BMI)

if BMI <= 18.5 and BMI > 2:
    print("Under weight.")
elif BMI <= 25:
    print("Normal")
elif BMI <= 30:
    print("Over weight")
else:
    print("Obesity")

a = float(input("Enter your marks:"))

if (a > 40): print (a , " is greater than 40. You pass!!!")

print("You pass") if a > 40 else print("Better luck next time.")

print(">") if a > 40 else print("=") if a == 40 else print("<")

if 30 > 40 or 35 < 85:
    print("Atleast one of the condition is True or both conditions are True.")

if not 30 > 40:
    print("30 is not greater than 40")
    if 30 > 20 and 50 < 60 :
        print("Both conditions are True")

if a > 80:
    pass