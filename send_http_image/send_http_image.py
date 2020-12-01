import os
import requests


url = 'http://localhost:8000/getimage/'
path_img = "cat.jpg"
with open(path_img, 'rb') as img:
    name_img= os.path.basename(path_img)
    files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
    with requests.Session() as s:
        r = s.post(url,files=files)
        print(r.status_code)
