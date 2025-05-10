#This is the program to calculate electricity charge according to the usage units per month of user

unit = int(input("Enter the number of units:"))
print(unit)

if(unit <= 100):
  amount = unit * 50.0
  print("The electricity charge is:",amount)
elif(unit > 100 and unit <= 200):
  amount = unit * 100.0
  print("The electricity charge is:",amount)
elif(unit >= 200):
  amount = unit * 150.0
  print("The electricity charge is:",amount)
else:
  print("Invalid input check your input")
  
