import urllib2
import urllib
import requests
values = {"username": "740494415@qq.com", "password": "Cfldcsdn123,"}
data = urllib.urlencode(values)

user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
handers = {'User-Agent': user_agent}
url = 'http://blog.csdn.net/cqcre'

request = urllib2.Request(url, data, handers)

try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print response.read()

