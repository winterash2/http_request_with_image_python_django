import os
import requests
import json


url = 'http://localhost:8000/getimage/'
path_img = "cat.jpg"
with open(path_img, 'rb') as img:
    # name_img= os.path.basename(path_img)
    # files= {
    #     'image': (name_img,img,'multipart/form-data',{'Expires': '0'})
    #     # 'image': img
    # }
    # with requests.Session() as s:
    #     r = s.post(url,files=files)
    #     print(r.status_code)
    #     print(r.text)

    payload={}
    files=[
        ('image',('cat.jpg',img,'image/jpeg'))
        # ('image',('cat.jpg',open('cat.jpg','rb'),'image/jpeg'))
    ]
    headers = {}
    r = requests.request("POST", url, headers=headers, data=payload, files=files)

    response_dict = json.loads(r.text)
    print(response_dict)
    print(response_dict['time'])