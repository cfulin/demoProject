#!/usr/bin/python
# coding: utf-8


# # import re
# # import urllib
# #
# #
# # def getHtml(url):
# #     page = urllib.urlopen(url)
# #     html = page.read()
# #     return html
# #
# #
# # def getMp4(html):
# #     r = r"href='(http.*\.mp4)'"
# #     re_mp4 = re.compile(r)
# #     mp4List = re.findall(re_mp4, html)
# #     filename = 1
# #     for mp4url in mp4List:
# #         urllib.urlretrieve(mp4url, "%s.mp4" % filename)
# #         print 'file "%s.mp4" done' % filename
# #         filename += 1
# # url = "http://v.youku.com/v_show/id_XMjYxMjEyNDU0MA==.html"
# # html = getHtml(url)
# # getMp4(html)
#
#
#
#
# # import re
# #
# #
# # pattern = re.compile(r'hello world')
# # match = pattern.match('hello world!')
# #
# # if match:
# #     print match.group()
#
#
# #
# # # 冒泡排序
# # array = [4, 5, 0, 2, 3, 7, 1, 6]
# #
# # for i in range(len(array) - 1, 1, -1):
# #     for j in range(0, i):
# #         if array[j] > array[j + 1]:
# #             array[j], array[j + 1] = array[j + 1], array[j]
# # print array
#
# # theString = 'saaaay yes no yaaaass'
# # print theString.strip('say') #say后面有空格
#
#
#
# # -*- coding:utf-8 -*-
# import urllib
# import urllib2
# import re
# import thread
# import time
#
#
# # 糗事百科爬虫类
# class QSBK:
#     # 初始化方法，定义一些变量
#     def __init__(self):
#         self.pageIndex = 1
#         self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         # 初始化headers
#         self.headers = {'User-Agent': self.user_agent}
#         # 存放段子的变量，每一个元素是每一页的段子们
#         self.stories = []
#         # 存放程序是否继续运行的变量
#         self.enable = False
#
#     # 传入某一页的索引获得页面代码
#     def getPage(self, pageIndex):
#         try:
#             url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
#             # 构建请求的request
#             request = urllib2.Request(url, headers=self.headers)
#             # 利用urlopen获取页面代码
#             response = urllib2.urlopen(request)
#             # 将页面转化为UTF-8编码
#             pageCode = response.read().decode('utf-8')
#             return pageCode
#
#         except urllib2.URLError, e:
#             if hasattr(e, "reason"):
#                 print u"连接糗事百科失败,错误原因", e.reason
#                 return None
#
#     # 传入某一页代码，返回本页不带图片的段子列表
#     def getPageItems(self, pageIndex):
#         pageCode = self.getPage(pageIndex)
#         if not pageCode:
#             print "页面加载失败...."
#             return None
#         # pattern = re.compile('<div class=author clearfix>.*?<img src=.*? alt=(.*?)>.*?<div.*?' +
#         #                      '<span>(.*?)</span>.*?stats-vote><i class=number>(.*?)</i>.*?' +
#         #                      '<i class=number>(.*?)</i>', re.S)
#         pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</', re.S)
#         items = re.findall(pattern, pageCode)
#         # 用来存储每页的段子们
#         pageStories = []
#         # 遍历正则表达式匹配的信息
#         # for item in items:
#         #     # 是否含有图片
#         #     haveImg = re.search("img", item[3])
#         #     # 如果不含有图片，把它加入list中
#         #     if not haveImg:
#         #         replaceBR = re.compile('<br/>')
#         #         text = re.sub(replaceBR, "\n", item[1])
#         #         # item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
#         #         pageStories.append([item[0].strip(), text.strip(), item[2].strip(), item[4].strip()])
#         # return pageStories
#         for item in items:
#             pageStories.append([item[0].strip(), item[1].strip(), item[2].strip()])
#         return pageStories
#
#     # 加载并提取页面的内容，加入到列表中
#     def loadPage(self):
#         # 如果当前未看的页数少于2页，则加载新一页
#         if self.enable == True:
#             if len(self.stories) < 2:
#                 # 获取新一页
#                 pageStories = self.getPageItems(self.pageIndex)
#                 # 将该页的段子存放到全局list中
#                 if pageStories:
#                     self.stories.append(pageStories)
#                     # 获取完之后页码索引加一，表示下次读取下一页
#                     self.pageIndex += 1
#
#     # 调用该方法，每次敲回车打印输出一个段子
#     def getOneStory(self, pageStories, page):
#         # 遍历一页的段子
#         for story in pageStories:
#             # 等待用户输入
#             input = raw_input()
#             # 每当输入回车一次，判断一下是否要加载新页面
#             self.loadPage()
#             # 如果输入Q则程序结束
#             if input == "Q":
#                 self.enable = False
#                 return
#             print u"第%d页\t发布人:%s\t 赞:%s\n%s" % (page, story[0], story[2], story[1])
#
#     # 开始方法
#     def start(self):
#         print u"正在读取糗事百科,按回车查看新段子，Q退出"
#         # 使变量为True，程序可以正常运行
#         self.enable = True
#         # 先加载一页内容
#         self.loadPage()
#         # 局部变量，控制当前读到了第几页
#         nowPage = 0
#         while self.enable:
#             if len(self.stories) > 0:
#                 # 从全局list中获取一页的段子
#                 pageStories = self.stories[0]
#                 # 当前读到的页数加一
#                 nowPage += 1
#                 # 将全局list中第一个元素删除，因为已经取出
#                 del self.stories[0]
#                 # 输出该页的段子
#                 self.getOneStory(pageStories, nowPage)
#
#
# spider = QSBK()
# spider.start()
#
# print [x * x for x in range(1, 11) if x % 2 == 0]


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


def main():
    # 打印1000以内的素数:
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


def is_palindrome(n):
    return int(str(n)[::-1]) == n


def count():
    def f(j):
        # def g():
        return j*j
        # return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


from PIL import Image


def changeImage():
    im = Image.open('C:/Users/Administrator/Desktop/1111.jpg')
    print(im.format, im.size, im.mode)
    im.thumbnail((1000, 500))
    im.save('C:/Users/Administrator/Desktop/11111.jpg', 'JPEG')


from multiprocessing import Process, Pool
import os, time, random


def run_proc(name):
    print("Run child process %s %s" % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s %s...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f' % (name, (start - end)))


def chinese_to_pinyin(x):
    """参数为字符串，返回为该字符串对应的汉语拼音"""
    y = ''
    # dic = {}
    # with open("unicode_pinyin.txt") as f:
    #     for i in f.readlines():
    #         dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        # try:
        #     y += dic[i] + ' '
        # except:
        #     y += 'XXXX '  # 非法字符我们用XXXX代替
    return y


if __name__ == '__main__':
    # main()
    # print(_not_divisible(3))
    # output = filter(is_palindrome, range(1, 1000))
    # print(list(output))
    # print(range(100))[::-1]
    # f1, f2, f3 = count()
    # print(f1)
    # print(f2)
    # print(f3)
    # changeImage()
    # print("Parent process %s ", os.getpid())
    # p = Process(target=run_proc, args=("test",))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')
    # print("Parent process %s ", os.getpid())
    # p = Pool(5)
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')
    print(chinese_to_pinyin(u"陈"))