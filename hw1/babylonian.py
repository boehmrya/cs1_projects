
import math

def babylonian():
     s = float(input("Input a real number x: "))
     xPrev = float(input("Guess the square root of " + str(s) + ": "))
     e = 0.0001
     i = 0

     while i < 1000: 
          
          part1 = s / xPrev
          x = (part1 + xPrev) / 2
          
          if math.fabs(x - xPrev) < e:
               return x
          else:
               i += 1
               xPrev = x

print(babylonian())
