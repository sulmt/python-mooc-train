#coding=utf-8

#Auti-Spider!!!!!!!!!!!!!!!!!!!!

import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding()
        return r.text
    except:
        print ""


def parsePage(ilt, html):   #获取商品名称和价格
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html) # extract price from the "V"
        nlt = re.findall(r'\"raw_title\"\:\".*?\"', html) #extract title
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            name = eval(nlt[i].split(":")[1])
        ilt.append([price, name])
    except:
        continue



def printGoodsList(ilt):
    tplt = "{:8}\t{:8}\t{:8}"  #modult
    print (tplt.format("序号","价格","名称"))
    count = 0 #序号
    for i in ilt:
        count += 1
        print (tplt.format(count, i[0], i[1]))



def main():
    goods = '书包'
    depth = 2 #爬取深度
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = [] #信息存放
    #out
    for i in range(depth):
        try:
            url = start_url + '&s =' + str(44 * i)#观察第一第二页面url末尾
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            print "error"

    printGoodsList(infoList)


main()


#url = "https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85"
#html = getHtmlText(url)
#print html