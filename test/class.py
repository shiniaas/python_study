class Student(object):
    pass

# 可以自由地给一个实例变量绑定属性
bart = Student()
print(bart)
bart.name = "Bart Simpson"
print(bart.name)
print('\n')


# 类中函数的第一个参数必须为self,__init__函数是类初始化的时候运行的
class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def judge_score(self):
        if self.score >= 90:
            print("A")
        elif self.score >= 80:
            print("B")
        else:
            print("C")

student1 = Student1("John", 90)
print("%s:%s" %(student1.name, student1.score))
print(hasattr(student1, 'name'))    # 判断某个类是否有某个属性

student1.judge_score()
print('\n')


# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_info(self):
        print("%s:%s" %(self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")

student2 = Student2("Mike", 80)
student2.print_info()
student2.set_score(1)
student2.print_info()
# student2.set_score(101)
print('\n')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)