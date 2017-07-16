import requests
import time


#  getHtml
def getHtml(url):
    try:
        req = requests.get(url, timeout=30)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        return req.text
    except:
        return "exception"


def getTime():
    url = "http://www.fjbsm.gov.cn"
    start = time.time()
    for i in range(100):
        getHtml(url)
    end = time.time()
    print("It takes %f seconds to finish the work." % (end - start))


getTime()

