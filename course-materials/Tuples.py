# T = (1, 2, 3)
# print(len(T))
# print(T[0])
# print(T + (5, 6)) # concatenation
# print(T)
# # T[0] = 2 immutable
# print(T.index(3))
# T = (1, 2, 2, 3)
# print(T.count(2))
# r = ('spam', 1, 1.2, [1, 2])
# print(r)

# Files
# f = open('List.py', 'r')
# print(f.read())

f = open('List.py', 'w')
f.write('Hello')
print(f.write('Hello'))
f.close()
