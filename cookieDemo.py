# encoding: utf-8
import urllib2
import cookielib
import urllib


# # 声明一个CookieJar对象实例来保存coolie
# cookie = cookielib.CookieJar()
# # 创建cookie控制器
# handle = urllib2.HTTPCookieProcessor(cookie)
# # 通过handle创建opener
# opener = urllib2.build_opener(handle)
# url = "http://www.baidu.com"
#
# request = urllib2.Request(url)
# response = opener.open(request)
#
# for item in cookie:
#     print "Name: " + item.name
#     print "Values: " + item.value


# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handle = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handle)
#
# url = "http://www.baidu.com"
# request = urllib2.Request(url)
# response = opener.open(request)
#
# cookie.save(ignore_discard=True, ignore_expires=True)


# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#
# url = "http://www.baidu.com"
# request = urllib2.Request(url)
# response = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie)).open(request)
#
# print response.read()

filename = "baiduCookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
dataCode = urllib.urlencode({'username': '740494415@qq.com', 'password': 'Cfldcsdn123,'})
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
url = "https://passport.csdn.net/account/login"
request = urllib2.Request(url)
response = opener.open(request, dataCode)
cookie.save(ignore_expires=True, ignore_discard=True)

gradeUrl = 'http://my.csdn.net/my/score'
result = opener.open(gradeUrl)
print result.read()


