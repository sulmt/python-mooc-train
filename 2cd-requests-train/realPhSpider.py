#coding:utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import os
import requests
import time
import random

def get_url_onepage(url):
    #打开URL
    reponse_url1 = urllib2.urlopen(url)
    #BS进行处理
    soup = BeautifulSoup(reponse_url1)
    #正则表达式搜索到自己想要的连接
    pattern=re.compile(r'/arthtml/(\d)+(.)html')
    all_link_inonepage=[]
    #查看需要的URL
    for link in soup.find_all('a'):
        link_match=link.get('href')
        match=pattern.match(link_match)
        if match:
            a='http://www.99v3.com'+match.group()
            all_link_inonepage.append(str(a))
    return all_link_inonepage
def get_head_url(start_page,end_page):
    if start_page==1:
        return None
    #访问不同的连接
    head_list=['http://www.99v3.com/arttypehtml/2-{}.html'.\
                   format(str(i)) for i in range(start_page,end_page)]
    return head_list
#获取图片
def cripp_image(url):
    print '*'*20
    print url
    print '*'*20
    rest_time=random.random()*10
    time.sleep(rest_time)
    #加载Mozilla的header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
        url=url
        ,
        headers=headers
    )
    reponse_url1 = urllib2.urlopen(req)
    soup_image=BeautifulSoup(reponse_url1)
    title=soup_image.title.string.split('[')[0]
    print title
    newfolder = os.mkdir('F:\\ImageCri\\' + title)
    image_num=0
    for link in soup_image.find_all('img'):
        link_match=link.get('src')
        print link_match
        # image_num=image_num+1
        image_name = 'F:\\ImageCri\\' + title + '\\'+'{}.jpg'.format(str(image_num))
        image_num=image_num+1
        # image_name='{}.jpg'.format(str(image_num))
        rest_time = random.random() * 10
        time.sleep(rest_time)
        # content = requests.get(link_match).content
        # with open(image_name, "wb") as f:
        #     f.write(content)
        urllib.urlretrieve(link_match,image_name)

#得到所有的URL
def get_all_url_2(start,end):
    url=['http://www.b9f7.com/AAtupian/AAAtb/zipai/index-{}.html'.format(str(x)) for x in range(start,end)]
    all_link=[]
    for i in url:
        #加载header
        onepage=[]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        req = urllib2.Request(
            url=i
            ,
            headers=headers
        )
        time.sleep(random.random()*4)
        reponse_url1 = urllib2.urlopen(req)
        pattern = re.compile(r'/AAtupian/AAAwz/(\d)+(\w)+(.)html')
        soup_image = BeautifulSoup(reponse_url1)
        for link in soup_image.find_all('a'):
            link_match = link.get('href')
            if link_match != None:
                match = pattern.match(link_match)
                if match:
                    c = match.group()
                    a = 'http://www.b9f7.com' + match.group()
                    all_link.append(a)
    return all_link
#得到图片
def get_img_2(url):
    str_url=str(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
        url=str_url
        ,
        headers=headers
    )
    time.sleep(random.random() * 4)
    reponse_url1 = urllib2.urlopen(req)
    soup_image = BeautifulSoup(reponse_url1)
    title = unicode(soup_image.title.string.split('>')[1].split('<')[0])
    #保存到图片的路径，这里是可以修改的
    os.mkdir('F:\\ImageCri\\' + title)
    image_num=0
    for link in soup_image.find_all('img'):
        link_match = link.get('src')
        print link_match
        image_num=image_num+1
        image_name = 'F:\\ImageCri\\' + title + '\\' + '{}.jpg'.format(str(image_num))
        image_num = image_num + 1
        rest_time = random.random() * 4
        time.sleep(rest_time)
        content = requests.get(link_match,timeout=180).content
        with open(image_name, "wb") as f:
            f.write(content)


#RUN enjoy:)
if __name__=="__main__":
    itera=0
    for one_html in get_all_url_2(6,10):
        itera=itera+1
        print '第一个Page'+'-'*50
        try:
            print one_html
            get_img_2(one_html)
        except:
            continue

    #print get_all_url_2(3,5)
    # head_in_each_page=get_head_url(6,10)
    # all_link=[]
    # for i in head_in_each_page:
    #     all_link.append(get_url_onepage(i))
    # print all_link
    # for i in range(len(all_link)):
    #     for j in all_link[i]:
    #         cripp_image(j)

    #----------------------------------------------
    # cripp_image('http://33img.com/upload/image/20170315/31500003229.jpg')
    # urllib.urlretrieve('http://33img.com/upload/image/20170315/31500003229.jpg', 'hao.jpg')
    # url = 'http://p.urlpic.club/2016/upload/image/20170302/30200546071.jpg'
    # content = requests.get(url).content
    # with open("22221.jpg", "wb") as f:
    #     f.write(content)
    # urllib.urlretrieve(url, '2222.jpg')
    #---------------------------------------------
    # url=['http://www.99v3.com/arthtml/{}.html'.format(str(x)) for x in range(1889,1900)]
    # print url
    # for url_demo in url:
    #     cripp_image(url_demo)
    #-------------------------------
    # cripp_image('http://www.99v3.com/arthtml/1886.html')
    # link_match='https://pic.bb164.com/d4/3030/303018-3.jpg'
    # content = requests.get(link_match).content
    # with open('hao.jpg', "wb") as f:
    #     f.write(content)
    #--------------------------------
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    # }
    # req = urllib2.Request(
    #     url="http://www.b9f7.com/AAtupian/AAAtb/zipai/"
    #     ,
    #     headers=headers
    # )
    # reponse_url1 = urllib2.urlopen(req)
    # pattern = re.compile(r'/AAtupian/AAAwz/(\d)+(\w)+(.)html')
    # soup_image = BeautifulSoup(reponse_url1)
    # for link in soup_image.find_all('a'):
    #     link_match = link.get('href')
    #     link_name = link_match.text()
    #     print link_name
    #     if  link_match!=None:
    #         match = pattern.match(link_match)
    #         if match:
    #             c = match.group()
    #             a = 'http://www.b9f7.com' + match.group()
    #             print a
    #--------------------------------------------------------------
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    # }
    # req = urllib2.Request(
    #     url="http://www.b9f7.com/AAtupian/AAAwz/8139e3a4b82a184cb05cd7e007e4aabd.html"
    #     ,
    #     headers=headers
    # )
    # reponse_url1 = urllib2.urlopen(req)
    # soup_image = BeautifulSoup(reponse_url1)
    # title = unicode(soup_image.title.string.split('>')[1].split('<')[0])
    # os.mkdir('F:\\ImageCri\\' + title)
    # image_num=0
    # for link in soup_image.find_all('img'):
    #     link_match = link.get('src')
    #     print link_match
    #     image_num=image_num+1
    #     image_name = 'F:\\ImageCri\\' + title + '\\' + '{}.jpg'.format(str(image_num))
    #     image_num = image_num + 1
    #     rest_time = random.random() * 10
    #     time.sleep(rest_time)
    #     content = requests.get(link_match).content
    #     with open(image_name, "wb") as f:
    #         f.write(content)
    #--------------------------------------------------------------------------------
    # soup_image = BeautifulSoup(reponse_url1)
    # title = soup_image.title.string.split('[')[0]
    # print title
