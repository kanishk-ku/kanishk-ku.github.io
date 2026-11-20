# print('Hi')

# Ak = input("Who is stronger and hard Avenger = ")
# if Ak == "Captain America":
#     print("...."*30)
#     print("Welcome Captin America Av")
#
# else:
#     print("---" * 30)
#     print("Welcome other Avenger")
#
# number = int(input("Enter the number = ")) # Type conversion
# if number >= 90:
#     grade = 'A'
# elif number >= 80:
#     grade = 'B'
# elif number >= 70:
#     grade = 'C'
# else:
#     grade = 'D'
# print("The Grade of student = ", grade)
# print()

# sum = 0
# num = int(input("Enter the number = "))
# for each in range(1, num):
#     sum += each   # sum = sum + each
#     if sum > 100:
#         break
# print("total sum is = ", sum)
#
# sum1 = 0
#
# # while (expression):
# #     statement
# while True:
#     n = int(input("Enter the number = "))
#     sum1 += n
#     print("sum is = ", sum1)
#     if n == 0:
#         break
# print("total sum is = ", sum1)

# list1 = [1, 2, 0, 3, 0, 4, 5]
# for i in list1:
#     if i == 0:
#         continue # skip particular iteration
#     c = 10/(i*100)
#     print("Percentage is = ", c)

# def load_balacing():
#     pass
#
# for i in [1, 2, 3]:
#     pass
import sys

# print(list(range(1, 20, 2)))
# print(list(range(30, 10, -2)))
# print(list(range(10, 20)))  #step size is positive for default value
# print(list(range(-10, 20)))
# print(sys.getsizeof(range(-10, 20)))
#
mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))
print(next(mylist))
print(next(mylist))
# """mylist = iter(["apple", "banana", "cherry"])
# for i in mylist:
#     print(i)"""

# for each in range(10):# start, the default value for start is always is zero
#     print(each)
#
# for each in range(10):  # start, the default value for start is always is zero
#     print(each, end= " ") # end is parameter
# print('\n')
#
# str1 = "Python Programming" # double quotes
# for i in str1:
#     print(i, end= " ")

name = input("Enter the name = ")
while name != "point break":
    print("Wrong password")
    name = input("Enter the password again = ")
print("Welocme User")
































