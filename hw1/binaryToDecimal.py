# Get input
n = int(input("Input a nonnegative binary integer: "))

dec = 0 # we will build the decimal equivalent in this variable
placeValue = 1 # the place value of the right most bit is 1

# repeatedly extract bits from n, right to left
while n > 0:
     bit = n % 10 # get the rightmost bit
     dec = dec + bit * placeValue # update dec by value of new bit
     n = n // 10 # everything except the last digit is reassigned to n
     placeValue = placeValue * 2 # update place value

print(dec)
