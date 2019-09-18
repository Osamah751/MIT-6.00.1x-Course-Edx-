


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    for i in range(0,exp,-1):
        base = recurPower(base, exp)
    return (base)

print (recurPower(2,5))
