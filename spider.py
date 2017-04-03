import sys
import urllib.parse
import requests
from selenium import webdriver
from bs4 import BeautifulSoup,NavigableString

def scraping(url, output_name):
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
    driver.get(url)
    html = driver.page_source
    with open("yui.html", "w") as fout:
       fout.write(html)
    soup = BeautifulSoup(html, "lxml")
    liLists = soup.findAll("h3")
    countSite = 0
    for liList in liLists:
        if isinstance(liList.find("a"), type(None)):
            continue
        else:
            alist = liList.find("a")
            if isinstance(alist, NavigableString):
                continue
            elif isinstance(alist.get("href"), type(None)):
                continue
            else:
                hreflist = alist.get("href")
                if isinstance(hreflist, type(None)):
                    continue
                else:
                    if "search.yahoo.co.jp" in hreflist:
                        continue
                    else:
                        print(hreflist)
                        with open(output_name, "a") as fout:
                            fout.write(hreflist + "\n")
                        countSite = countSite + 1

    print("合計サイト数" + repr(countSite))

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) != 3:
        print("Usage: python scraping.py [url] [output name]")
        exit()
    key = urllib.parse.quote(argvs[1])
    url = "http://search.yahoo.co.jp/search?p=" + key + "&ei=UTF-8&b=1"
    output_name = argvs[2]
    print(argvs[0],argvs[1],argvs[2],url)
    scraping(url, output_name)
