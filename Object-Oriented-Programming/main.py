#MIT practice: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-8-object-oriented-programming/
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def distance(self, other):
    x_distance = (self.x-other.x)**2
    y_distance = (self.y - other.y)**2
    return (x_distance + y_distance)**0.5

c = Coordinate(4, 2)
c2 = Coordinate(5,3)
print(c.distance(c2))

#self practice
class Dog(object):
  def __init__(self, age, floofiness): #both ints
    #assert type(age) == int and type(floofiness) == float
    try:
      self.age = int(age)
      self.floofiness = int(floofiness)
    except ValueError:
      print("Please use integers")
    except:
      print("Error.")
  def pet(self, times):
    self.times = times
    for time in range(times):
      print("You have pet the doggo.")
  def sniff(self, other):
    print("You have sniffed the other doggo.")

haoHao = Dog(2, 10)
gumbo = Dog(2, 9)
haoHao.pet(2)
haoHao.sniff(gumbo)
