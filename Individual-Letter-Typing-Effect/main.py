'''
import time
string = "Hello, my name is Yixing. Today we will be playing a game..."
letters = list(string)
for letter in letters:
  print(letter, end='')
  time.sleep(0.1)
'''
import time
import sys
def delay_print(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

delay_print("Hello, my name is Yixing. Today we will be playing a game...")