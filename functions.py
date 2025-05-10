def my_func():
  print("Hello this is Shalini")
#function calling
my_func()

def func(fname):
  print("My first name is " , fname)
func("Thushalini")
func("Peranantham")

def func(fname , lname):
  print(fname , " " , lname)
func("Thushalini" , "Peranantham")

def my_func(*kids):
  print("First child :" , kids[0])
my_func("Angathan" , "Anojan" , "Thushalini")

def my_function(child3, child2, child1):
  print("The eldest child is " + child1)

my_function(child1 = "Angathan", child2 = "Anojan", child3 = "Thushalini")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Peranantham", lname = "Anojan")

def my_function(country = "Sri Lanka"):
  print("I am from " + country)

my_function("India")
my_function()
my_function("Brazil")

def func(food):
  for x in food:
    print(x)
fruits = ["apple" , "mango" , "cherry"]
func(fruits)

def func(x):
  return 5 * x
print(func(6))
print(func(9))

def my_func():
  pass

#positional only argument
def my_function(x, /):
  print(x)

my_function(3)
#my_function(x=3)   is occur error

#keyword only argument
def my_function(*,x):
  print(x)

my_function(x=3)
#my_function(3)   is occur error

#combine positional only and keyword only function
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

