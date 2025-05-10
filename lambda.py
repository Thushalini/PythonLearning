#lambda function can take any no of arguments but have only one expression
x = lambda a : a * 6
print(x(5))

def func(n):
    return lambda a : a * n
doubler = func(2)
tripler = func(3) 

print(doubler(5))
print(tripler(5))

