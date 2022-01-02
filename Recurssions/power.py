def power(base,exp):

    # f(a,b) = a * f(a,b-1)  

    assert exp>=0 and int(exp) == exp, 'The exp must be positive integer'
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)

print(power(3,4))

print(3**4)