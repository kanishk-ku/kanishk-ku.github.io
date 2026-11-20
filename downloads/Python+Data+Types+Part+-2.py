
# """Type-Specific Methods"""

# S = 'spam'
#  print(dir(S))
#  print(S + 'NI!')
#  print(S.__add__('NI!'))  

# directory method 
# built-in methods which are already in Python librarys.

#  """split() method # callable method"""  
# directory method

#  help(S.replace)  # def replace(old, new, count=-1, /):

#  S = 'A\nB\tC' # \n is end of line \t is tab
#  print(len(S))
#  print(S)
#  print(ord('\n')) # ASCII Value
#  S = 'A\0B\0C'
#  print(S)
#  print(bytearray(b'A\0B\0C'))
#  m = """aa
#  bb
#  ccc""" # doc string
#  print(m)

# m = 'sp\xc4m'
# print(m)
# bytes strings
# print(b'a/x01c')
# print(u'sp\u00c4m')
# print('spam'.encode('utf8'))  # 4 bytes
# print('spam'.encode('utf16')) # 10 bytes

# print('sp\xc4\u00c4\U000000c4m')
# g = b'spaam'
# print(g.decode())


# regrex expression
import re
match = re.match('Hello[ \t]*(.*)', 'Hello Python world')
print(match.group(1))
print(match.group())
print(re.split('\t','Hello [ \t]*(.*), Python, world' ))
