#coding=utf-8
import urllib2
import urllib
import re
import time
from  random  import   choice
iplist=['202.194.101.150','124.240.187.89','124.240.187.89']
ip=choice(iplist)
gic="众筹"
gjc=urllib.quote(gic)
url="https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd="+str(gjc)
headers={"Get":url,
      "Host":"sp0.baidu.com",
      "Referer":"https://www.baidu.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36"
}
proxy_support=urllib2.ProxyHandler({'http':'http://'+ip}) #代理
opener=urllib2.build_opener(proxy_support) #代理
urllib2.install_opener(opener)   #代理
req=urllib2.Request(url)
for key  in headers:
    req.add_header(key, headers[key])
html=urllib2.urlopen(req).read()
html_decode=html.decode("gbk")
time.sleep(0.2),
result=re.findall(""(.*?)"",html_decode)
for  item  in result:
    print item
