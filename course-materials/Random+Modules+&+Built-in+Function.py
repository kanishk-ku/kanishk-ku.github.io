#
#
import random
# random.randint(start, end)
# print(random.randint(5, 20))
# without range
from functools import reduce

"""print(random.randint(5))
TypeError: Random.randint() missing 1 required positional argument: 'b'"""

""" random.randrange(start=0, stop, step size=1)
start+(step*n) < = stop # True
"""
"""
print(random.randrange(10))

print(random.randrange(10, 30))
print(random.randrange(10, 30, 2)) # step size/interger is a multiple of output
"""
# random.choice(sequence)
"""print(random.choice((1, 2, 3)))
print(random.choice('abcad'))
print(random.choice([3, 4, 5]))"""

"""# random.shuffle(list)
list1 = [14, 12, 56, 90]
print(list1)
print(random.shuffle(list1)) # None
print(list1)"""

"""random.shuffle(sequence, length)
class_10th = [3.5, 3.5, 3.5, 3.5, 3.5, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
sample1 = random.sample(class_10th, 5)
print(sample1)

print(random.random()) #range is between 0 and 1"""

# print(random.uniform(3, 10))
"""	Tombola game
•	Number must be interger
•	Ranges from 1 to 100
•	Non-repeatable
import random
list1 = list(range(1, 101))
random.shuffle(list1)
for each in list1:
    print(each)
    input("Press enter to get next value = ")"""

"""	OTP generator
•	OTP must contain the numbers and letters
•	OTP length should be 6

def password_gen():
    str1 = "1234567890"
    str2 = "abcdefghijklmnopqrstuvwxyz"
    list1 = random.sample(str1, 3)
    list2 = random.sample(str2, 3)
    print("before extend = ", list1)
    list1.extend(list2)
    print("after extend = ", list1)
    random.shuffle(list1)
    otp = "".join(list1)
    return otp
print(password_gen())

 Lambda arg1, arg2, …..argn : expression

l = lambda x : x ** 2
print(l(9))
l1 = lambda x, y : x + y
print(l1(4, 7))
lambda can take any number of arguments and retuens only one expression

filter(function1, list1)

list1 = [1,2,3,4,5,6]
def fun1(x):
    t = x * 2
    if t // 2 == 1:
        return True
    else:
        return False

res = filter(fun1, list1)
print(list(res))

list1 = [1,2,3,4,5,6]
list2 = filter(lambda x: x % 2 == 0, list1)
print(list(list2))

map(function1, iterable)

list1 = [0, 10, 37, 38, 45]
def fun1(temp):
    f = 9/5*temp+32
    f = round(f, 2)
    return f
we = map(fun1, list1)
print(list(we))

list1 = [0, 10, 37, 38, 45]
a = map(lambda temp: 9/5*temp+32, list1)
print(list(a)) 

reduce(function, list)

from functools import reduce
list1 = [0, 10, 37, 38, 45]
def fun1(x, y):
    c = x+y
    return c
we = reduce(fun1, list1)
print(we)
print(sum(list1))

isinstance(variable, type)

list1 = [12.3, 4.7, '3']
b = 20
for i in list1:
    try:
        if isinstance(i, float):
            k = i/b*100
            print(k)
    except Exception as e:
        print(e)

list1 = [12.3, 4.7, '3', 'a', 2]
b = 20
other = []
for i in list1:
        if isinstance(i, float):
            k = i/b*100
            print(k)
        else:
            other.append(i)
print(other)

eval(string expression)"""
# exp = "12+10*2"
# print(eval(exp))
# print(type(exp))
# t = eval(exp)
# print(type(t))

# list1 = [1, 2, 3]
# str1 = str(list1)
# l1 = eval(str1)  # removes the quotes
# print(l1)
# print(type(l1))

# repr()  ---> returns string object or string representaation of passing objects
# l1 = []
# str1 = "Mohit"
# l1.append(str(str1))
# print(l1)
# l1.append(repr(str1))
# print(l1)

import datetime
print(str(datetime.datetime.now()))

print(repr(datetime.datetime.now()))













