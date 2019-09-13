'''
baidu
import requests
keyword="Python"
try:
    kv={'wd':keyword} #360为'q'
    r=requests.get("http://www.baidu.com/s",params=kv)#url="http://www.so.com/s"
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("Error")
'''

360
import requests
keyword="Python"
try:
    kv={'q':keyword} #360为'q'
    r=requests.get("http://www.so.com/s",params=kv)#url="http://www.so.com/s"
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("Error")
