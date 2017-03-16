n = int(input("Type a nonnegative integer: "))

if n < 0:
    print("Please input a nonnegative integer next time. Bye!")
else:     
    originalN = n
    suffix = ""
    while n > 0:
        suffix = str(n % 2) + suffix
        print(suffix)
        n = n//2
    
    # The input n = 0 is dealt with as a special case
    if suffix == "":
        suffix = "0"

    print("The binary equivalent of", originalN, "is", suffix)
