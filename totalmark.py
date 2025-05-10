#This is a program to calculate total marks
#way 1
module = 1
total = 0
while module <= 4 :
  mark = float(input("Enter your module mark :"))
  module += 1
  total += mark
print("The total of for modules' marks" , total)

#way 2
def totalmark(mark):
  print("total mark",total)
  average = total / 4
  if average > 75:
    print("You got 'A'")
  elif average > 65 and average < 75:
    print("You got 'B'")
  elif average < 65 and average > 45:
    print("You got 'C'")
  else:
    print("You fail")
    print("You have to take repeat")
    
  
total = 0
module = 1
while module <= 4:
  mark = float(input("Enter module mark"))
  total += mark
  totalmark(mark)
  module += 1
