#MIT Lecture: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-slides-code/MIT6_0001F16_Lec9.pdf
class Dog(object):
  def __init__(self, breed, age, gender):
    self.breed = breed
    self.age = age
    self.gender = gender
    self.name = None
  
  #setters functions

  #name = "" is a default argument
  def set_name(self, nameo = ""):
    self.name = nameo
  
  
  #getters functions
  def get_age(self):
    return self.age
  def get_gender(self):
    return self.gender
  def get_breed(self):
    return self.breed
  def get_name(self):
    return self.name

myDog = Dog("Shih Tzu", 9, "female")

print(myDog.get_age())
#myDog.set_name("Hao hao")
print(myDog.get_name())


#CLASS INHERITANCE/SUBCLASS

class ShihTzu(Dog):
  def speak(self):
    print("Woof!")
  
doggo = ShihTzu("Shih Tzu", 9, "female")
print(doggo.speak())