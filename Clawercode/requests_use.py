import requests
a=requests.get("http://course.buaa.edu.cn/")
b=a.status_code
print(b)
print(a.text)
print(a.encoding)
print(a.apparent_encoding)
