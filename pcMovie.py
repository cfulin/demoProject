# -*- coding: utf-8 -*-
import requests
import codecs
import json
from requests.exceptions import RequestException
import re
import multiprocessing


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


def parse_one_page(html):
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
    #                      + '<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">'
    #                      + '(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>', re.S)

    # pattern = re.compile('<em.*?class="">(.*?)</em>.*?', re.S)
    # '<em.*?class="">(\d+)</em>.*?'
    # + '<div.*?class="hd"><apan.*?class="title">(\d+)</span></div>'

    pattern = re.compile('<div.*?class="item">.*?<div.*?class="pic">.*?'
                         + '<em.*?class="">(.*?)</em>.*?'
                         + '<div.*?class="info">.*?<span.*?class="title">(.*?)'
                         + '</span>.*?<span.*?class="title">&nbsp;/&nbsp;(.*?)</span>.*?'
                         + '<span.*?class="other">&nbsp;/&nbsp;(.*?)</span>.*?</a>.*?'
                         + '<div.*?class="bd">.*?<p.*?class="">.*?'
                         + u'导演:.*?(.*?)&nbsp;&nbsp;&nbsp;'
                         + u'主演:.*?(.*?)<br>'
                         + '\s                            (.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\s                       </p>'
                         + '.*?<div.*?class="star">.*?"v:average">(.*?)</span>'
                         + u'.*?<span>(.*?)人评价</span>.*?<p.*?class="quote">.*?'
                         + '<span.*?class="inq">(.*?)</span>.*?</p>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            # "index": item[0],
            # "title": item[2],
            # "actor": item[3].strip()[3:],
            # "time": item[4].strip()[5:],
            # "score": item[5] + item[6],
            # "image": item[1]

            "index": item[0],
            "ch-title": item[1],
            "eg-title": item[2],
            "hk-title": item[3],
            "director": item[4],
            "actor": item[5],
            "year": item[6],
            "country": item[7],
            "type": item[8],
            "score": item[9],
            "people": item[10],
            "content": item[11]
        }


def write_to_file(content):
    with codecs.open('result.txt', 'a', 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    # url = 'http://maoyan.com/board/4?offset=' + str(offset)
    url = 'https://movie.douban.com/top250?start={0}&filter='.format(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

        # print html


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    # pool.map(main, [i * 10 for i in range(10)])
    pool.map(main, [i * 25 for i in range(11)])
