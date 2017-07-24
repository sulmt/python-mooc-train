#coding=utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import re
#import trackback
from io import open

# 3 steps

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print ""

def stockList(lst, stockURL): #get a list of all stocks number from eastmoney web
    html = getHtmlText(stockURL)
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all('a')
    for i in a:
        try:
         #   href = i.get('href')
            href = i.attrs['href']
         #   list = re.findall(r'[s][hz]\d{6}', href)[0]
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue
#    print lst

def stockInfo(lst, stockURL, fpath):  #write in
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHtmlText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stock_info = soup.find('div',attrs={'class':'stock-bets'})
            stock_name = stock_info.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': stock_name.text.split()[0]})#try text->string?
            # all the stock information except name
            keyList = stock_info.find_all('dt')
            valueList = stock_info.find_all('dd')


           for i in range(len(keyList)): #if no rangelen?
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value
           # print infoDict.decode('unicode-escape')
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')    #unicoude ->  str bug 在3X版本中已经修复 不纠结
               # for iw in infoDict:
               #     f.write(iw.decode('unicode-escape'))
               #     f.write('\n')
            f.close()

        except:
            #traceback.print_exc()#track the exception and feed back information
            continue



def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    outpath = "E://BaiduStockInfo.txt"
    stockLst = []
    stockList(stockLst, stock_list_url)
    stockInfo(stockLst, stock_info_url, outpath)


main()

