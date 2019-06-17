# coding: utf-8
import requests
import json
import util
import os
import time
import config

class Imgs:

    def __init__(self): #sss
        self.headers = {
            'Referer': 'https://byteio.cn',
            #'Content - Type': 'multipart / form - data;boundary = ----WebKitFormBoundaryYzhjgNULijJxORZz;charset=utf-8"'
        }
        self.user_key=config.gate_user_key
        self.api_url="https://api.byteio.cn/gate/img/api/upload"
        self.localhlst_url="http://localhost:8080/img/api/upload"

    def post_file(self,path):
        if len(config.gate_user_key) <5:
            return
        if os.path.getsize(path) > 9*1024*1024 :
            print ("图片："+path+"过大，无法上传")
            return

        title=((path).split("\\")[-1])
        filename=title
        if "_#_" in title:
            title = title.split("_#_")[0] + "//" + title.split("_#_")[2]
        title=title.split(".")[0]
        datas=json.dumps({
            "user_key": self.user_key,
            "title": title,
            "desc": "pixiv",
        })#.decode('raw_unicode_escape')
        files={
            "params":(None,datas),
            "pic" : (filename,open(path,'rb').read())
        }
        try:
            rsp = requests.post(self.api_url, files=files, headers=self.headers)
            if rsp.status_code ==200 :
                if util.isJson(rsp.content):
                    status = json.loads(rsp.content)
                    print (status["desc"])
                    if status["code"] == "0":
                        time.sleep(5*60)

            else:
                print ("上传连接失败："+str(rsp.status_code))

        except Exception as e:
            print ("上传连接出错："+str(e))

if __name__ == "__main__":
    imgs = Imgs()
    imgs.post_file("D:\psdcode\Python\测试.jpg")