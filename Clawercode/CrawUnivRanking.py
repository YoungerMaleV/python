import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance (tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])#判断是否为标签类型
    
def printUnivList(ulist,num):
    tplt="{0:^20}\t{1:{3}^20}\t{2:^20}"
    print(tplt.format("排名","学校","成绩",chr(12288)))
    for i in range (num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    unifo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html=getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,20) #20univs
    
main()
