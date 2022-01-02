def sumOfDigits(n):

    # f(n) = n%10 + f(n//10)
    
    assert n>=0 and int(n) == n, 'The no has to be positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))

print(sumOfDigits(25))
print(sumOfDigits(125))
print(sumOfDigits(1254))