
x = float(input("Input a real number x: "))
t = int(input("Input a nonnegative integer t: "))

sumTotal = 1 # track the sum of each part
counter = 1 

while counter <= t:
     num = x**counter
     fact = counter - 1
     den = counter
     while fact >= 1:
          den = den * fact
          fact -= 1
     counter += 1

     part = num / den
     sumTotal += part

print(sumTotal)
     

        
