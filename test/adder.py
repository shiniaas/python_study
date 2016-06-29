def adder(x, y):
    if not(isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Input must be integers")
    return x + y