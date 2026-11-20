# t1 = () # empty tuple
# if t1:
#     print("Something in Tuple")
# else:
#     print("Tuple is empty")

# tup1 = ('Python', 'PHP', 123, 1,  7,  9)
# #          0        1     2   3   4   5
# #         -6       -5    -4  -3  -2  -1

# print(tup1[2])
# print(tup1[-1])
# print(tup1[-6])

# print(tup1[start:end:step size])
# default value of start is always zero &
# default value of step size always 1

# print(tup1[:3:])
# print(tup1[:-1])  """ for negative position, default value of start is always starting position, it means -len(tuple) """

# tup1 = ('Python', 'PHP', 123, 1,  7,  9)
# #          0        1     2   3   4   5
# #         -6       -5    -4  -3  -2  -1
# print(tup1[-len(tup1):-1])
#
# print(tup1[0:4:2])

# tup1 = (1,  7,  11, 3, 7, 1, 3, 4, 3)
# print(tup1.count(3))  # count occurrence of item = frequency of item
# print(tup1.count(7))
# print(tup1.count(11))

# Tuple.index(given item)
# print(tup1.index(9))
# print(tup1.index(7))
# print(len(tup1))

# print(max(tup1))
# print(min(tup1))

# tup1 = (1,  7,  11, 3)
# tup2 = (7, 1, 3, 4, 3)
# print(tup1 + tup2)
#
# print(tup2 * 3)

# print(11 in tup1)
# print(4 in tup1)
# print(4 not in tup1)

# tuple =  (1,  7,  11,  3)
#         a   b    c   d
# a,b,c,d = tuple
# # important conditon of unpacking of tuples
# # no. of items in tuple == no. of variables
#
# print(c)
# print(b)

# tup1 =  (1,  'ab',  11,  'c',  3)
# for item in tup1:
#     print(item)

# list1 = ["Tony", "Steve", "Bruce"]
# print(list1)
#
# # In operator
# print("Tony" in list1)  # Membership
#
# for item in list1:
#     print(item, end=' ')
# list comprehension
# res = [ c * 4 for c in "SPAM"]
# print(res)
#
# # for loop
# res = []
# for c in "SPAM":
#     res.append(c * 3)
# print(res)
#
# # map(function, list)
# print(list(map(abs, [1,  -11 ,  11,  -1,  3])))

# # Indexing, Slicing and Matrixes
# L = ['spam', 'SPAM', 'Spam'] # Python is case sensitive
# print(L[1])
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# #            0       1       2      --  outside list
# #         (0 1 2)  (0 1 2) (0 1 2)  --  inside list
# print(matrix[0][1])
#
# print(L[1:2])

# A = ["Captain", "Iron-Man", "Hulk", "Spider"]
#       0          1          2        3
# print(A[2])
# print(A[0:2])

# A[1] = "Black Widow"  # mutable data structure/type
# print(A)

# del A[1]
# print(A)
# del A
# print(A)
# A = ["Captain", "Iron-Man", "Hulk", "Spider"]
# A2 = ["Batman", "Catwoman"]
# print(A + A2)
#
# print(A2 * 4)

# print("Iron-Man" in A)
# print("Thor" in A)
# print("Thor" not  in A)
A = ["Captain", "Iron-Man", "Hulk", "Spider", "Batman", "Catwoman"]

for i in A:
     print(i)