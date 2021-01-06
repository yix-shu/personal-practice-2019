"""
try: is paired with except: like if, elif, and else
"""
try:
  age = int(input("How old are you? "))
except ValueError:
  print("Oops, please enter a number!")
except:
  print("Error!")