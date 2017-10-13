#!/usr/bin/python
# -*- coding: utf-8 -*-
# # def method_friendly_decorator(method_to_decorate):
# #     def wrapper(self, lie):
# #         lie = lie - 3  # 女性福音 :-)
# #         return method_to_decorate(self, lie)
# #     return wrapper
# #
# #
# # class Lucy(object):
# #
# #     def __init__(self):
# #         self.age = 32
# #
# #     @method_friendly_decorator
# #     def sayYourAge(self, lie):
# #         print("I am %s, what did you think?" % (self.age + lie))
# #
# # l = Lucy()
# # l.sayYourAge(-3)
#
# def binarysearch(l, t):
#     low, high = 0, len(l) - 1
#
#     while low < high:
#         mid = (low + high) / 2
#         if(l[mid] > t):
#             high = mid
#         elif(l[mid] < t):
#             low = mid + 1
#         else:
#             return mid
#     return low if l[low] == t else False
#
# l = [1, 2, 3, 4, 11, 56, 66, 333, 2222]
# print(binarysearch(l, 11))

# n = int(raw_input("please input number: "))
# r = ""
# while(n > 0):
#     if(n % 2 == 0):
#         r += '2'
#         n = (n - 2) / 2
#     else:
#         r += '1'
#         n = (n - 1) / 2
# print r[::-1]
# n = eval(raw_input(""))11
# n = str(raw_input(""))
# s = str(raw_input(""))
# from __future__ import division
# s ="aaabbaaac"
# # print ('%.2f' % (len(s) / 4))
# # print(round(len(s) / 4, 2))
# # print(len(s) / 4)
# r = 0
# # while(len(s) >= 1 & len(s) <= 50):
# for i in range(len(s)):
#     if(i != len(s) - 1):
#         if(s[i] != s[i + 1]):
#             r += 1
# print('%.2f' % (len(s) / (r + 1)))
# if __name__ == '__main__':
#     pass


# def fact(k):
#     if (k == 1):
#         return 1
#     return k * fact(k - 1)
#
#
# if __name__ == '__main__':
#     n = str(raw_input(""))
#     k = 0
#     for i in range(len(n)):
#         if (i != len(n) - 1):
#             break
#         elif (n[i] != n[i + 1]):
#             k += 1
#     print fact(k)


# def quickSort(num, l, r):
#     if l >= r:  # 如果只有一个数字时，结束递归
#         return
#     flag = l
#     for i in range(l+1, r+1):  # 默认以第一个数字作为基准数，从第二个数开始比较，生成索引时要注意右部的值
#         if num[flag] > num[i]:
#             tmp = num[i]
#             del num[i]
#             num.insert(flag, tmp)
#             flag += 1
#     quickSort(num, l, flag-1)  # 将基准数前后部分分别递归排序
#     quickSort(num, flag+1, r)
#
# num = [1, -2, 4, 7, 6, 3, 2, 3]
# quickSort(num, 0, 7)
# print(num)


import random

list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
#
#
# def qsort(L):
#     if len(L) < 2:
#         return L
#     pivot_element = random.choice(L)
#     small = [i for i in L if i < pivot_element]
#     large = [i for i in L if i > pivot_element]
#     return qsort(small) + [pivot_element] + qsort(large)
#
#
# print(qsort(list1 + list2))
# z = 0
# g = lambda x, y=2, z = 0 : x + y**z
# print(g(1, z=10))

# a = [1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
# a.sort()
# last = a[-1]
# for i in range(len(a)-2, -1, -1):
#     if last == a[i]:
#         del a[i]
#     else:
#         last = a[i]
# print(a)



# def quickSort(L):
#     if len(L) < 2:
#         return L
#     s = random.choice(L)
#     small = [i for i in L if i < s]
#     large = [i for i in L if i > s]
#     return quickSort(small) + [s] + quickSort(large)
#
# print(quickSort(list1 + list2))


# import re
# from datetime import datetime, timezone, timedelta
#
# def to_timestamp(dt_str, tz_str):
#     dt_str = datetime.strptime(dt_str, "%Y-%m-%d, %H:%M:%S")
#     tz_str = re.match(r'^[\w]{3}([+-][\d]+):00$', tz_str).group(1)
#     utcz = dt_str.replace(tzinfo=timezone(timedelta(hours=tz_str)))
#     uts = utcz.timestamp()
#     return uts
#
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# print(t1)
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# print(t2)

# def flatten(nested):
#     try:
#         try: nested + ''
#         except TypeError: pass
#         else: raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):
#                 yield element
#     except TypeError:
#         yield nested
#
# print(list(flatten([['caca'], ['casca', 'c'], ['caa', 'qqq', ['dddd', 'sad']], ['fgaj', 'hfu']])))


import codecs
import json
import re
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response = response.text
            return response
        else:
            return None
    except RequestException:
        return None


def write_to_file(content):
    with codecs.open('city.txt', 'a', 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

# <span style="FONT-SIZE: 15pt; FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'">
# 个）：太原市、大同市、朔州市、忻州市、阳泉市、晋中市、吕梁市、长治市、临汾市、晋城市、运城市</span>
def parse_one_page(html):
    # pattern = re.compile('<p.*?class="MsoNormal".*?'
    #                      + '<span.*?style="FONT-SIZE:.*?15pt.*?>(.*?)</span>', re.S)
    # pattern = re.compile('<table.*?class="citytr".*?<td><a.*?>(.*?)</a></td>', re.S)
    pattern = re.compile(u'<td>(.*?)市', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "city": item[0]
        }


def main():
    # url = 'http://maoyan.com/board/4?offset=' + str(offset)
    # url = 'http://www.360doc.com/content/12/0601/21/6818730_215294560.shtml'
    # url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/13.html'
    url = 'http://data.acmr.com.cn/member/city/city_md.asp'
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    main()