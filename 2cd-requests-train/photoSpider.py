#coding=utf-8

import requests
import os
url = "http://i-4.yxdown.com/2017/4/28/KDE5Mngp/0383c72f-04e2-435d-bec5-c4f8e84a2c61.jpg"
#root = "E://pytext//pic//"
root = "E://pic//"
#root = "E://py爬虫//" 中文乱码但还是能执行的
#root = "E://py爬虫//pic"  报错？？？因为有中文的原因？？
path = root + url.split('/')[-1]
print root
os.mkdir(root)
#print path
try:
   # r = requests.get(url)
    if not os.path.exists(root): #if root no exist,create it
        os.mkdir(root)
    if not os.path.exists(path):# if path no exist,get the url
        r = requests.get(url)
        with open(path,'wb') as f:  #open the path file to operate and as file
            f.write(r.content) #write in
            f.close()
            print("success")
    else:
        print("error")
except:
    print("find exception")