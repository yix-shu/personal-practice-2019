#Notes: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec1.pdf

#The Food problem
class Food(object):
  def __init__(self, n, v, w):
    self.name = n
    self.value = v
    self.calories = w
  def getValue(self):
    return self.value
  def getCalories(self):
    return self.calories
  
  def density(self):
    return self.getValue()/self.getCalories()
  
def buildMenu(names, values, calories):
  menu = []
  for i in range(len(values)):
    menu.append(Food(names[i], values[i], calories[i]))
  return menu


def greedy(items, maxCost, keyFunction): #this is a greedy algorithm, which means it helps reach an optimal solution. This function helps compilate the list of items that will be under the requested/desired maxCalories/maxCost
  itemsCopy = sorted(items, key=keyFunction, reverse = True)
  #keyFunction is an umbrella term for the "best" functions/results the user wants (like density)
  result = []
  totalValue, totalCost = 0.0, 0.0
  for i in range(len(itemsCopy)):
    if(totalCost + itemsCopy[i].getCost() <= maxCost):
      result.append(itemsCopy[i])
      totalCost += itemsCopy[i].getCost()
      totalValue += itemsCopy[i].getValue()
  return (totalValue, totalCost)

def testGreedy(items, constraint, keyFunction):
  taken, val = greedy(items, constraint, keyFunction)
  print('Total value of items taken =', val)
  for item in taken:
    print(' ', item)

