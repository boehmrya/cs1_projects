

def histogram(n):
     i = 0
     firstQuartile = ""
     secondQuartile = ""
     thirdQuartile = ""
     fourthQuartile = ""
     
     while i < n:
          num = int(input("Enter a number between 0 and 100: "))
          if 0 <= num <= 25:
               firstQuartile += "*"
          elif 26 <= num <= 50:
               secondQuartile += "*"
          elif 51 <= num <= 75:
               thirdQuartile += "*"
          elif 76 <= num <= 100:
               fourthQuartile += "*"
          else:
               # don't increment i by 1 if they enter an invalid number
               print("The number you entered is not between 0 and 100.  Try again")
               continue 
          i += 1

     print("[0, 25]    " + firstQuartile)
     print("(25, 50]   " + secondQuartile)
     print("(50, 75]   " + thirdQuartile)
     print("(75, 100]  " + fourthQuartile)
     

histogram(5)
