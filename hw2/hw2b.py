import math

def pythagoreanTriple():
     m = int(input("Enter a positive integer for M: "))

     x = 1
     while x <= m:
          y = x + 1
          while y <= m:
               zSquared = (x**2) + (y**2)
               z = math.sqrt(zSquared)
               if (z).is_integer():
                    print(str(x) + " " + str(y) + " " + str(int(z)))
               y += 1
          x += 1


pythagoreanTriple()                      
                    
