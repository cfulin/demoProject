#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import os

url = 'http://pvp.qq.com/web201605/js/herolist.json'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
html = requests.get(url, headers=head)
html = requests.get(url)
html_json = html.json()

hero_name = list(map(lambda x: x['cname'], html_json))
hero_number = list(map(lambda x: x['ename'], html_json))

def main():
    ii = 0
    for v in hero_number:
        path = "D:/Users/Administrator/PycharmProjects/demoProject/picture/" + hero_name[ii]
        strPath = path.encode("utf8")
        # name = hero_name[ii]
        os.mkdir(strPath)
        # os.chdir("D:/Users/Administrator/PycharmProjects/demoProject/picture/" + hero_name[ii])
        ii += 1
        for u in range(12):
            onehero_links = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' \
                            + str(v) + '/' + str(v) + '-bigskin-' + str(u) + '.jpg'
            im = requests.get(onehero_links)
            if im.status_code == 200:
                iv = re.split('-', onehero_links)
                open(iv[-1], 'wb').write(im.content)

if __name__ == '__main__':
    main()
