from __future__ import division
import numpy as np


# print 1/2
# name = raw_input("input your name: ")
# print 'hello' + " " + name
# raw_input("Press <enter>")
# name = list('Perl')
# name[2:] = list('aa')
# number = [1, 5]
# number[1:1] = [2, 3, 4]
# number.insert(3, 'aa')
# number.reverse()
# cmp(10, 10)
# number.sort(cmp)
# print 'PI: %-10.5s' % np.pi
#
# from string import maketrans
#
# table = maketrans('cs', 'kz')
# print "nadn  jaknkj  vjsdnjkn clllks".translate(table, " ")


# people = {
#     'Alice': {
#         'phone': '123',
#         'addr': 'awqcvdbc'
#     },
#
#     'Bob': {
#         'phone': '213',
#         'addr': 'asdaadac'
#     },
#
#     'Jim': {
#         'phone': '231',
#         'addr': 'afdabfbc'
#     },
#
# }
#
# labels = {
#     'phone': 'Phone Number',
#     'addr': 'address'
# }
#
# name = raw_input('Name: ')
#
# request = raw_input('Phone number(p) or address(a)? ')
#
# if request == 'p':
#     key = 'phone'
# if request == 'a':
#     key = 'addr'
#
# if name in people:
#     print "%s's %s is %s." % (name, labels[key], people[name][key])
# from copy import deepcopy
# x = {'username': 'admin', 'machins': ['foo', 'bar', 'baz']}
# y = x.copy()
# dc = deepcopy(x)
# y['username'] = 'mln'
# y['machins'].remove('bar')
# print x, dc
strings = [('a', 2), ('b', 3), ('c', 3), ('d', 2), ('e', 1)]
# strings = {'a': 2, 'b': 3, 'c': 3, 'd': 2, 'e': 1}

for index, string in enumerate(strings):
    if 'a' in string:
        strings[index] = 'aa'

print strings

print ''.join(reversed("hello,world!"))
# print train[:, :3]

# scope={}
# from math import sqrt
# exec 'sqrt = 1' in scope
# print scope['sqrt']

fibs = [0, 1]
num = raw_input('How many Fibonacci numbers do you want?: ')
for i in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])

print fibs
