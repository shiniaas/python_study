from functools import reduce

def add1(x,y):
    return x+y

def add(x, y, f):
    return (f(x)+f(y))

def f(x):
    return x*x

def is_odd(n):
    return n % 2 == 1

print(add(-1, 1, abs))

r = map(f, [1,2,3,4,5,6,7,8,9,10])
print(list(r))

a = reduce(add1, [1,3,5,7,9])
print(a)

b = list(filter(is_odd, [1,2,3,5,8]))
print(b)