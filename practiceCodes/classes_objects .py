class myclass:
    x = 5
    name = "vel"

p1 = myclass()
print(p1.x)
print(p1.name)

#__init__() function to assign values to object properties, or 
#other operations that are necessary to do when the object is being created

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("John" , 36)

print(p1.name , p1.age)
print(p1)    #without __str__() function

class car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.year}"
    
    #object methods
    def func(self):
        print("My first car is " , self.brand)
    
c1 = car("volvo" , 2005)
print(c1.brand)
print(c1)

c1.func()

#self parameter is a reference to the current instance of class, and 
#is used to access variables that belongs to the class

#self has to be the first parameter of any functionin class but we can name it as whatever we like

class dress:
    def __init__(first , type , color):
        first.type = type
        first.color = color

    def __str__(one):
        return f"{one.type} {one.color}"
    
    def bday(wear):
        print("My last birth day dress is " , wear.color , wear.type)

d1 = dress("frock" , "black")
d1.bday()

#modify object properties
d1.color = "red"
d1.bday()

#delete object property
del d1.type

#delete object
del d1

class persons:
    pass