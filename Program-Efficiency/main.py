#MIT LECTURE:https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-slides-code/MIT6_0001F16_Lec10.pdf 
import time #using the time module to measure efficienty

#function we are timing
def c_to_f(c):
  return c*9/5 + 32

#timing a program

start = time.time()
c_to_f(100000)#function we are timing

end = time.time() - start
print(end)
