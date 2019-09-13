import requests
url = "https://www.baidu.com"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encooding
    print(r.text[:1000])#打印前1000个字符

except:
    print("Error")
