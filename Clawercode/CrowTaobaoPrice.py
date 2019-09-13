#CrowTaobaoPrice.py
import requests
import re
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30,headers={'cookie':'t=cc37d3493690cfd489c8d3f3921af77e; cookie2=1ecffd9adff3c570426de2ac00208d57; _tb_token_=5884ade1a35e7; thw=cn; cna=zEThFa52QCUCAXjkp/dH1yn0; v=0; unb=3391797780; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBy3K1E6cpaRO4Hek%3D&nk2=BdwmLF%2Bck47xMMP2RQ%3D%3D&id2=UNN0mIDEPzxSmg%3D%3D; csg=72d886bc; lgc=flydragon6666; cookie17=UNN0mIDEPzxSmg%3D%3D; dnk=flydragon6666; skt=3ffebf8e7613c350; existShop=MTU2NjIwNDAyMQ%3D%3D; uc4=nk4=0%40B1B1McImu8%2FTaynlAQ0bJMMP0EjRjEwS&id4=0%40UgQ8c3lD6qQsdNndedX76%2FCFqkOD; tracknick=flydragon6666; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=60e; _nk_=flydragon6666; cookie1=BxZucS8VnoG%2BhEcwQvvZCncaJc6DCAJFMIdVw3eaVG8%3D; mt=ci=8_1; enc=O%2BUIE0qNvwAFzPewnTjBQJWsUMzr0NIO%2BV7bUTULAT3Wdm6m3rq7OSMCZsEdJC2Y8piIDr9R9z5YoGe0FQgpUQ%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=ACD701577F0D3B481562535C028B3680; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; swfstore=50142; uc1=cookie14=UoTaHokcwWrp1A%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D; isg=BIeH7NYTlkTGmhM__DXLQ2eKFjtbm941f5cIj1l1lZY9yKWKY15TvriCasAzIDPm; l=cBPuAnbgvnRteMRDBOfa-urza779yIOb8sPzaNbMiICPOW1M54M1WZeZ5_YHCnGNK6cW-37uMFCUB7YOIydZGhZfP3k_J_f..; whl=-1%260%260%261566204766964'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
def main():
    goods = '书包'
    depth = 4
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()

