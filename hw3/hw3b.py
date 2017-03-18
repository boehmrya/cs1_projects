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


print(nearHalfInteger(3.00004)) #should return true
print(nearHalfInteger(4.51)) #should return true
print(nearHalfInteger(-9.99999999)) #should return true
print(nearHalfInteger(-3.49999)) #should return true
print(nearHalfInteger(11.8)) #should return true

