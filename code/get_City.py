#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pandas as pd


def read_excel():
    # 打开文件
    inpath = 'city1.json'
    outpath = inpath.split('.')[0] + '_outfile' + '.xlsx'
    # outpath = unicode('outfile.xlsx', 'utf-8')
    return inpath, outpath


def getCity(inpath):
    with open(inpath, 'r') as f:
        data = json.load(f)
    gLen = len(data['data'])
    city = []
    for i in range(gLen):
        city.append(data['data'][i]['c'])
    return city


def flatten(nested):
    try:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


def dataProcess(data):
    data = data.dropna(axis=0, how='all', thresh=None)  # 一行全为空舍弃(axis=1)为行删除
    data = data.drop_duplicates()  # 去除重复行
    data.to_excel('citydealfile.xlsx')
    return data


def main():
    inpath, outpath = read_excel()
    # url = 'http://maoyan.com/board/4?offset=' + str(offset)
    # url = 'http://www.360doc.com/content/12/0601/21/6818730_215294560.shtml'
    # url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/13.html'
    # url = 'http://data.acmr.com.cn/member/city/city_md.asp'
    # html = get_one_page(url)
    # for item in parse_one_page(html):
    #     write_to_file(item)
    cityData = getCity(inpath)  # 获取city名称
    flatCity = flatten(cityData)  # 递归生成器连接
    cityData = pd.DataFrame(flatCity, columns=['city'])  # DataFrame转换字符串
    cityData.to_excel(outpath)  # 输出city到excel
    dataProcess(cityData)


if __name__ == '__main__':
    main()