import requests

import time


def getHTMLText(url):
    try:

        r = requests.get(url)

        r.raise_for_status()

        r.encoding = r.apparent_encoding

        return r.text

    except:

        return "Error!"


def main():
    url = "http://www.bilibili.com"

    print("Start the test.")

    start_time = time.clock()

    for i in range(100):
        getHTMLText(url)

    end_time = time.clock()

    print("It takes %f seconds to finish the work." % (end_time - start_time))


main()

