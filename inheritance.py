#parent class or base class is a class being inherited from
#child class or derived class is the class inherits from another class

class person:
    def __init__(self , fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(name):
        print(name.firstname , name.lastname)

p1 = person("Thushalini" , "Peranantham")
p1.printname()

#create a child class 
class student(person):
    pass

s1 = student("Shalini" , "Aravind")
s1.printname()

#add the __init__ function
