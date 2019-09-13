import requests
import os
url="http://pic.netbian.com/uploads/allimg/190514/214437-15578414771479.jpg"
root ="D://pythonClawer//pics//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.midir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("Success")
    else:
        print("Already Exist")
except:
    
    print("Failure")
