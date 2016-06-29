import time
import functools

def lazy_sum(argv):
    def sum():
        t = 0
        for i in argv:
            t = t + i
        return t
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call : %s()' % func.__name__)
        r = func(*args, **kw)
        print('end call : %s()' % func.__name__)
        return r
    return wrapper

@log
def now():
    print(time.ctime())

def log1(textOrFunc):

    #text = textOrFunc if isinstance(textOrFunc, str) else  'call :'
    if(isinstance(textOrFunc, str)):
        text = textOrFunc
    else:
        print(type(textOrFunc))
        text = 'call :'


    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper

    return decorator if isinstance(textOrFunc, str) else decorator(textOrFunc)

@log1('a')
def now1():
    print(time.ctime())

if __name__ == '__main__':
    string = 'abc'
    f = lazy_sum([1, 2, 3, 4, 5])
    print(f())
    f1, f2, f3 = count()
    print(f1(), f2(), f3())
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
    now()
    now1()
    print(string)
    if(type(type(string)) == r"<class 'str'>"):
        print('ok')