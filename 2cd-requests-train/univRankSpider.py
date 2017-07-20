#coding=utf-8
#步骤一：获取排名网站内容（getHtmlText）
#步骤二：提取有用信息至数据结构（fillUnivList）
#步骤三：利用数据结构并输出结果（printUnivList）

import requests
from bs4 import BeautifulSoup
import bs4
import re


def getHtmlText(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        demo = req.text
        print("step 1 succ essfully get the rank url")
        return demo
    except:
        print("error")

#print getHtmlText(url)

#print getHtmlText(url)
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:   #每个tr就是一所大学的信息
        #过滤非大学信息
        if isinstance(tr, bs4.element.Tag):
            #检测tr是否和bs4的元素标签类型一致
            tds = tr("td")
            ulist.append([tds[0].contents[0].string, tds[1].string, tds[2].string])



def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0].encode("gb2312"), u[1].encode("utf-8"), u[2].encode("utf-8")))



# 定向爬取
#def main():
#url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
#uinfo = [] #make universal rank into uinfo
#html = getHtmlText(url)
#fillUnivList(uinfo, html)
#printUnivList(uinfo, num)
def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    num = 30
    uinfo = [] #make universal rank into uinfo
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, num)


main()