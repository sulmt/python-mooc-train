import requests

def getHtml(url):
    try:
        kv = {"user-Agent": "Mozilla/5.0"}
        req = requests.get(url, kv)
        req.raise_for_status() #200 check
        req.encoding = req.apparent_encoding
        print req.text
    except:
        print "error"

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
getHtml(url)
