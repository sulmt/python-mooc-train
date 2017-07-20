import requests
kv = {"wd": "python"}
req = requests.get("http://www.baidu.com/s", params = kv)
print ("the status_code is %f" % req.status_code)
print req,requests.__url__
req.encoding = req.apparent_encoding
print ("length:%f" % len(req.text))


