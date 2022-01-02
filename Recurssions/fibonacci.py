def fibonacci(n):
    assert n >=0 and int(n) == n, 'Fibonacci number cannot be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(5))


def printfibnonaccinos(n):
    f1 = 0
    f2 = 1
    if n == 1:
        print(f1)
    elif n == 2:
        print(f1," ",f2 )
    else:
        print(f1, f2, end= ' ')
        for i in range(3,n+1):
            f3 = f1 + f2
            print(f3, end= ' ')
            f1 = f2
            f2 = f3

printfibnonaccinos(20)