
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


def farthestConsecutivePrimes(n):
    primes = []
    i = 2
    # build a list of all primes less then or equal to n
    while i <= n:
        if isPrime(i):
            primes.append(i)
        i += 1

    # find the two farthest consecutive primes
    j = 0
    maxDistance = 0
    lowPrime = 0
    highPrime = 0
    while j < (len(primes) - 1):
        distance = primes[j + 1] - primes[j]
        if distance > maxDistance:
            maxDistance = distance
            lowPrime = primes[j]
            highPrime = primes[j + 1]
        j += 1

    return [lowPrime, highPrime]


print(farthestConsecutivePrimes(150))

