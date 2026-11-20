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
print(d1)
print(d2)

