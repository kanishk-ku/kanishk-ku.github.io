#
#
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
# A = ["Captain", "Iron-Man", "Hulk", "Spider", "Batman", "Catwoman"]
#
# for i in A:
#     print(i)

# A = ["Captain", "Iron-Man", "Hulk", "Spider", "Batman", "Catwoman"]
# print(max(A))  # ASCII Value, thwe value of S is maximum
# print(min(A))  # ASCII Value, thwe value of B is minimum
#
# list1 = [0, 5, 3, 2, 1]
# print(max(list1))
# print(min((list1)))

# list1 = [0, 5, 3, 2, 1]
# print(dir(list1))
#
# list1.append(90)
# print(list1)

# A = ["Captain", "Iron-Man", "Hulk", "Spider", "Batman", "Catwoman"]
# A.append("Black Widow")
# print(A)

# list.extend(sequence)
# A.extend(["Black Widow", "Flash"])
# print(A)
# B = ["Captain", "Iron-Man", "Hulk", "Spider", "Batman", "Catwoman"]
# B.append(["Black Widow", "Flash"])
# print(B)

# inf = ["Space", "Mind", "Tree", "A"]
# #        0        1       2      3
# inf.insert(2, 12)  # insert item before that pass index
# inf.insert(1, "alpha")
# inf.insert(6, "Mind")
# print(inf)
#
# print(inf.remove("Mind"))
# print(inf.pop(1))
# print(inf)


# s = [0, 5, 3, 2, 1]
# s.sort(reverse=True)  # default value of reverse = False
# print(s)
#
# list2 = [("b", 20), ("c", 10), ("a", 30), ("d", 40)]
# print(list2)
# list2.sort() # default value of sort first occurrence of item
# print(list2)
#
# list2.sort(key = lambda x: x[1])
# print(list2)

# t = [0, 5, 3, 2, 1, 4]
# #    5  4  3  2  1  0
# print(sum(t))
# print(t.clear())
# print(t)
#

"""	count()
	index()
	copy()
	sort()
	reverse()
	sum()
	clear()
"""






# list_ip = ["192.168.2.1", "192.168.0.3", "192.168.2.09"]
# list_ip.sort(key = lambda x: x.rsplit(".", 1)[-1])
# print(list_ip)

# max1 = max(s) + 1
# def fun2(x):
#     if x == 0:
#         return max1
#     else:
#         return x
#
# s.sort(key = fun2)
# print(s)


# c = ['Space', 'alpha', 'Mind', 12, 'Tree', 'A', 'Mind']
# print(c.count("Mind"))
# print(c.count("M"))

# y = c.copy()
# # print(y)
# print(id(c))
# print(id(y))

"""o	Changing Lists in Place - 2
	Index and slice assignments
	List method calls
	More on sorting lists
	Other common list methods and operations 
"""

# L = ['Space', 'alpha', 'Mind', 12, 'Tree', 'A', 'Mind']
# print(L[3])

# print(L[1:3])
# L[1:3] = ["beta", "Peace"]   # slice assignment: two thinks it will delete earlier item in slice range and insert new item in place
# # Replace and insertion
# print(L)
# L[1:2] = ["gamma", "Peace"] # add slice assignment add more item in place one item
# print(L)
# print(L[2:4])
# L[2:4] = []   # Deletion
# print(L)

# L[3] = 40
# print(L)

"""o	Changing Lists in Place - 2
	List method calls
	More on sorting lists
	Other common list methods and operations 
"""

L = ['Space', 'alpha', 'Tree', 'Alpha', 'Mind']
# L.append("please")
# L.sort()
# print(L)   #Capital alphabet is low ASCII Value as compared to lowercase alphabets
# print(L + ["please"]) # Concatenation
# L = L + ['mind']
#
# L.sort(key = str.lower, reverse = True)
# print(ord('A'))
# print(ord('a'))
# print(L)


"""o  Dictionaries
	{}
	Creating a dictionary
	Features
"""

# Dictionary_name = { key1 : value1, key2 : value2 }  syntax of dictionary
# item == key and value pair
# key of dictionary cannot be changed
# keys are unique
# keys may be string, int, float and tuple, tuple does not contain any list
# d = { (1, 2) : "t", 2: "r", 1: "e"}
# print(d)
# d[(1, 2)] = ["1", 12, "ac"]
# print(d)
# value of dictionary can be changed and can be anything
# hashable type ---- immutable types( tuple, int, float, string) as a key,
# unhashable type --- mutable types( list ) is not used as key
# complexity of dictionary value is O(1)

"""o	Dictionaries in Action - 2
	Dictionary Operation – 2 & 3
•	Accessing the values of dictionary
•	Deleting item from dictionary
•	Updating and adding in dictionary
•	Adding item to dictionary
	Changing Lists in Place - 2
"""
#
# port = { 23 : "Telnet", 20 : "FTP", 80 : "http"}
# # port[50] = "new"
#
# port[80] = ['grill', 'bake', 'fry']
# print(port)

# print(port.keys())
# print(port.values())
# print(port.items())
# print(len(port))

# port = { 23 : "Telnet", 20 : "FTP", 80 : "http"}
# port[20] = "Lucky"
#
# port[30] = "FRP"
# print(port)

# print(port[20])
#
# # del dictionay[key]
# del port[23]
# print(port)


"""o	Dictionary Methods – 2 & 3
Directory methods
	copy()
	get()
	setdefault()
	items()
	keys()
	values()
	update()
"""

d1 = { 23 : "Telnet", 20 : "FTP"}
d2 = {80 : "http", 70: "t", 60000: "hvhjjh"}
# dict1.update(dict2)
d1.update(d2)
# print(d1)
# print(d2)




# port = { 23 : "Telnet", 20 : "FTP", 80 : "http", 70: "t", 60000: "hvhjjh"}
# import sys
# print(sys.getsizeof(port.items()))
# print(sys.getsizeof(port.keys()))
# print(sys.getsizeof(port.values()))

# print(port.items())
# print(port.keys())
# print(port.values())
# print(port.setdefault(50, "unknow item"))



# port1 = port.copy()
# print(port1)
#
# print(port1.get(20))
# print(port1.get(50, "t"))
# print(port1.get(20, "t"))



# print(dir({}))
# """['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__'
# , '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items',
# 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']"""
#
# print(port.__len__())
# print(port.__class__())
# print(list(port.__reversed__()))

"""keys, items, values"""

port = { 23 : "Telnet", 20 : "FTP", 80 : "http", 70: "t", 60000: "hvhjjh"}
# print(port.keys())
# print(port.values())
# print(port.items())
# print(port.clear())
# ip = port.copy()
# print(ip)
# print(id(ip), id(port))
# print(port.fromkeys({"2":23}))
# print(port.fromkeys("2",'2'))
# print(port.pop(70))
# print(port.popitem())
# {'name': 'Bob', 'age' : 40} Traditional literal expression
# D = {}
# D['name'] = 'Bob'
# D['age'] = 40
# print(D)
"""dict(zip(keylist, valueslist))"""   # Zipped key/values tuples form
# F = {}
# F = F.fromkeys([1, 2, 3], "Q")
# print(F)
# F = dict(zip([1, 2, 3],["Q","A","T"]))
# print(F)

"""Dictionary Comprehension
Dictionary Nesting"""
# print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
# D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
# print(D)

# D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
# print(D)
# U = {x: x ** 3 for x in [1, 2, 3, 4]}
# print(U)
#
# N = {
#     'a' : {
#           1 : 'Best',
#           2 : 'Tale'
#     }
# }
#
# print(N['a'][1])

# N = {
#     'a' : {
#           1 : 'Best',
#           2 : 'Tale'
#     }
# }
# print(len(N))
# o = { 23 : "Telnet", 20 : "FTP", 80 : "http", 70: "t", 60000: "hvhjjh"}
# print(max(o))
# print(min(o))

"""
o	With Item
o	Without Items
o	Set Methods
"""
# s = {1, "2", (3, 4)}  # not take list
# print(s)

# print(type(s))
# s2 = set()
# # print(type(s2))
#
# print(dir(s2))

# s  = set()
# s.add("k")
# s.add("k")
# print(s)

s2  = {5, 3, 4}
s3 = {3}
s4 = {2, 3}
# print(type(s2))
# print(s2.intersection(s3))
# print(s2, s3)
# print(s2.difference(s3))
# print(s2, s3)
# print(s2.isdisjoint(s4))
# print(s4.issubset(s2))
# print(s4.issuperset(s3))
# print(s4.symmetric_difference(s3))
# print(s4, s3)
# print(s4.symmetric_difference_update(s3))
# print(s4, s3)
print(s4.union(s2))
# print(s2.intersection_update(s3))
# print(s2, s3)
# print(s2.difference_update(s3))
# print(s2, s3)
# print(s2)
# print(s2)
#
# s2.remove(1)
# # print(s2)
# s2.update((1, 5))
# print(s2)
# print(s2.pop())
# print(s2.discard(3))
# print(s2)





























































