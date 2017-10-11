# import cPickle as pickle
#
# f = open('C:/Users/Administrator/Desktop/RNN_Text_Classify-master/data/subj0.pkl', 'rb')
# info = pickle.load(f)
# f.close()
# print info   # show file

import random
#
# print zip(range(4), range(2, 6))
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[0:-1])
# word = 'cloud'
# print(min(word))
# print('Life is short, you need Python.'.split(' '))
# print('you' in 'Life is short, you need Python.')
# print(list('Life is short, you need Python.').count('is'))
# print( [5] * 2)
# # print dir(str)
# print('you' in 'Life is short, you need Python.')
# print ('Life is short, you need Python.').find('you')

# import nltk
# nltk.download()
# print(text1.collocations("monstrous"))

# -*- coding: utf-8 -*-
import pandas as pdimport, re

with open("s03e09.txt") as f:
    data = f.read()

data = data.split('Opening Credits]')[1]
data = data.split('[End Credits')[0]

regex1 = r"^$\n"
subst = ""
data = re.sub(regex1, subst, data, 0, re.MULTILINE)

regex2 = r"^-+$\n"
data = re.sub(regex2, subst, data, 0, re.MULTILINE)
lines = data.split('\n')

myrows = []
num = 1
for line in lines:
    myrows.append([num, line])
    num += 1

df = pdimport.DataFrame(myrows)
df.columns = ['line', 'text']
print df

df.to_csv('data.csv', index=False)
