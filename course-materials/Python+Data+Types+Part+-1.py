# for program run please remove the '#' character according to requirement
# r = '2 ** 2'
# print(len(r))  # 6
# print(len(str(2 ** 2))) # len(4) = 1
# print(str(2 ** 2)) # 4
#
# import math
# print(math.pi)
# print(math.sqrt(85))
# import random
# print(random.random())
# print(random.randint(1, 2))
# print(random.choice([1, 2, 3]))
#
# S = 'spam'
#    s p a m
#    0 1 2 3
#   -4-3-2-1  reverse order
# print(len(S))
# S[index]
# print(S[1])
# 
# """negative indexes"""
# print(S[-1])
# print(S[-3])
# print(S[-3] == S[1])   # True
# print(S[len(S) - 1])  """S[4 - 1] = S[3]"""
# """Slices  X[I:J]
# I = 0   J = len(string)"""
# S = 'spam'
#    s p a m
#    0 1 2 3
# print(S[1:])  # substring = 'pam'
# print(S[0:3])  # J = len(string) = 3  but counting 0:len(string) - 1=2  0,1,2
# print(S[:])
# print(S[:2])
# print(S + S) # addition  two variables
# print(S + 'xyz') # concatenation
# print(S*3)
#
# """Immutability"""
# print(S)
# print(S[0])
# S[0] = 'z'
# """TypeError: 'str' object does not support item assignment"""
# But we can run expression to make new objects
# S = 'z' + S[1:]   # concatenation
# print(S)
# D = 'shrubbery'
# print(S)
# L = list(S) # Type Conversion
# print(L)
# L[1] = 'c' # List is mutable but strings are immutable
# print(L)
#
# """bytearray"""
# B = bytearray(b'spam')
# print(B)
# print(type(B))
# B.extend(b'eggs')
# print(B)
# print(B.decode())
# g = B.decode()
# print(type(g))
#
# """Type-Specific Methods"""
#
# S = 'spam'
# print(S.find('pa'))
# r = S.replace('pa', 'XYZ')
# print(S)
# print(r)
#
# line = 'aa,bb,cc,dd'
# print(line.split(','))
# line = 'aa bb cc dd'
# print(line.split(' '))
# print(line.upper())
# print(line.lower())
# line = 'spam'
# print(line.isalpha())
# line = '   aa bb cc dd    '
# print(line.rstrip().split(' '))
#
#
# formatting method
# print('%s' % ('spam'))
# print('%s and eggs %s' % ('spam', 'KOOL'))
# print('{1} and {0} eggs '.format('spam', 'KOOL'))
# print('{} and {} eggs '.format('spam', 'KOOL'))
# print('{:,.2f}'.format(2344.45566))