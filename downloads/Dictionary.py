# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'} # keys: values pairs
# print(D['food'])
# D['quantity'] += 1
# print(D)
#
# F = {}
# F['height'] = 23
# F['age'] = 'six'
# print(F)
# kool = dict(height=23, age='six')
# print(kool)
# z = dict(zip(['height','age'], [23, 'six']))
# print(z)
#
# rec = {'mcd': {'food': 'Spam', 'quantity': 4, 'color': 'pink'},
#        'item': ['burger', 'fries']}
# print(rec['mcd']['quantity'])
# rec['item'].append('cake')
# print(rec['item'])
#
# # rec['age']
# if not 'age' in rec:
#     print('missing')
#
# print(rec.get('item', 0))
# print(rec.get('age', 0))
#
# print(rec.keys())
# print(rec.values())
# print(rec.items())
# k = list(rec.keys())
# k.sort()
# print(k)
#
# for key in k:
#     print(key, '--->>',rec[key])
#

squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)

sq = []
for x in [1,2,3,4,5]:
    sq.append(x ** 2)
print(sq)

