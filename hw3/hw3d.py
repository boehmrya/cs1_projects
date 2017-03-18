
import random

def twoDRandomWalk(n = 100, printOn = False):
     x = 0 # x coordinate position
     y = 0 # y coordinate position
     numSteps = 0 # track the number of steps

     # take steps until you reach the outer boundary
     while x < n or y < n:
          direction = random.randint(1,4)
          if direction == 1:
               x += 1
          elif direction == 2:
               x -= 1
          elif direction == 3:
               y += 1
          else:
               y -= 1
          if printOn == True:
               print(x, y) # print the steps if necessary
          numSteps += 1

     return numSteps


print(twoDRandomWalk(20, True))
          
