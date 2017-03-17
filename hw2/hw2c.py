import math

# Returns True if n is a prime; False otherwise
def isPrime(n):
    factor = 2 # initial value of possible factor
    factorUpperBound = math.sqrt(n) # the largest possible factor we need to test is sqrt(n)
    
    # loop to generate and test all possible factors
    while (factor <= factorUpperBound):
        # test if n is evenly divisible by factor
        if (n % factor == 0):
            return False
        
        factor = factor + 1
        
    return True


def printTwinPrimes():
     m = int(input("Please type a positive integer: "))
     primes = [] # a list to hold all prime numbers

     # test each number for primality
     # add to list of primes if it is prime
     i = 2
     while i <= m:
          if isPrime(i):
               primes.append(i)
          i += 1

     # go through the list of primes and check which ones are
     # two number apart, print them if so
     j = 0
     while j < len(primes):
          k = j + 1
          while k < len(primes):
               if primes[k] == (primes[j] + 2):
                    print(str(primes[j]) + " " + str(primes[k]))
               k += 1
          j += 1


printTwinPrimes()
          
