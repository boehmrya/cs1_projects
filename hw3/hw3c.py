
import math

# determines if a floating point number f is
# within 1/1000 of a half integer (-0.5, 0, 0.5, 1, 1.5, ...)
def nearHalfInteger(f):
     # repeatedly subtract 0.5 until you get below 0
     # so we can compare the number to 0
     count = 0
     originalf = f
     f = math.fabs(f)
     while f >= 0:
          f -= 0.5
          count += 1 # track the number of subtractions
     if (0 > (math.fabs(f) - 0.001)):
          if originalf > 0:              
               return (count * 0.5)
          else:
               return (count * -0.5)
     elif (0 > (f + 0.5 - 0.001)):
          if originalf > 0:              
               return ((count - 1) * 0.5)
          else:
               return ((count- 1) * -0.5)
     else:
          return None


def main():
     n = int(input("Please enter a positive integer: "))
     i = 0
     numNearHalfInts = 0 # track the number of near half integers
     nearHalfInts = []
     while i < n:
          f = float(input("Please enter a floating point number: "))
          if nearHalfInteger(f):
               numNearHalfInts += 1
               nearHalfInts.append(f)
          i += 1
     for num in nearHalfInts:
          print(num)
     print("The number of near half integers is " + str(numNearHalfInts))


main()
