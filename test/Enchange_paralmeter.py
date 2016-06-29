#可变参数
def calc(*num):
    sum = 0
    for i in num:
        sum = sum + i*i
    return sum

def calc1(num):
    sum = 0
    for i in num:
        sum = sum + i*i
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)

s = [1,2,3]
print(calc(1,2,3))

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*s))
print(*s)
print(calc1(s))

person('lifan', 20, city='Wuhan')
person('Adam', 45, gender='M', job='Engineer')
