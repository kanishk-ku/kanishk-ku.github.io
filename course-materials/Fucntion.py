#
#
# def hello():
#     print("Hello Frank")
#     return ''
#
# print(hello())
#
# def func1(a, b):
#     c = a + b
#     print(a)
#     return f"Result is =", c # f-string
# print(func1(10, 20))
# print(func1(b=10,a=20)) # positional arguments: 'a' and 'b'
#
# def func1(a, b):
#     c = a + b
#     return c
#
# result = 20 + func1(1, 12)
# print(result)

# def fun2(name, skill, age=30):
#     print(name, "\t", skill, age)
# print("Name  \t  skill age")
# print(fun2("Kelvin","python", 32))
#
# print(fun2("Kelvin","python"))

# def fun2(name, skill, age=30, ):
#     print(name, "\t", skill, age)
# print("Name  \t  skill age")
#
# print(fun2("Kelvin","python"))
# # order of define arguments are like
# """positional arguments --> default arguments"""
#
# def fun2(name="Kelvin", skill="python", age=30, ):
#     print(name, "\t", skill, age)
# print("Name  \t  skill age")
#
# print(fun2())
# def addition(a, *args): # variable-length arguments
#     print(type(args))  # tuple
#     c = a + sum(args)
#     return c
#
# print(addition(10))
# print(addition(10, 50, 12, 20))

# def func1(**kwargs):
#     print(type(kwargs))   # ** with kwargs is dictionary and * with args is tuple
#     print(kwargs)
# print(func1(name="XYZ", age=30, skill= "Quantam"))
#
# def func1(arg, age=30, *args, **kwargs):
#     print(arg, age)
#     print(sum(args))
#     print(kwargs)
#     print("*"*40)
#
# print(func1("Kelvin", 31, 1,2,3,4,5, skill="python", emp= 1234))
#
# print(func1("ram", skill="python", emp= 1234))
# print(func1("kool"))

# c = 1
# print(id(c))

# def func2(list1):
#     print("Inside List", list1)
#     print("Inside address", id(list1))
#     list1.append(45)
#     print("inside after appending", list1)
#     print("Inside address", id(list1))
#
# list2 = [10, 80, 90]
# print("before appending",list2)
# print(id(list2))
# print(func2(list2))
# print("after appending",list2)
# print(id(list2))

# a = 8

# def func3():
#     list1 = []
#     def enc():
#         c = a + 2
#         for i in range(c):
#             list1.append(i)
#         return list1
#     print(enc())
#     return ''
# print(func3())

# a = 8
#
# def func3():
#     list1 = []
#     def enc():
#         for i in range(a):
#             list1.append(i)
#         return list1
#     print(enc())
#     return ''
# print(func3())

# def f():
#     k =20
#     return k
# print(f())
# print(k)

def fun():
    global k
    k = k + 30
    return k
k = 10
print("before call the function, global variable value is =",k)
print(fun())
print("after call the function , global variable value is =",k)















































































