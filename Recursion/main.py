#MIT example: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-slides-code/MIT6_0001F16_Lec6.pdf

#Factorial
def factorial(a):
  if a == 1:
    return a
  else:
    return a*factorial(a-1)
#print(factorial(5))

#Fibonacci
def fib(a):
  if a == 1 or a == 2:
    return 1
  else:
    return fib(a-1) + fib(a-2)
#print(fib(6))