#defining functions with functions as parameters
def calculate(func, x):
  print(func(x))

def square(x):
  return x**2

calculate(square, 20)
