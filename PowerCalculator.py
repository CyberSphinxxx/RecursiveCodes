def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# Test the function
base = 2
exponent = 5
print(base, "raised to the power", exponent, "is", power(base, exponent))
