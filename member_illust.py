# coding=utf-8

from pixiv_ import Pixiv
from gate_img import Imgs
import json
import os
#爬取某画师所有的画
class Member_illust:
    def __init__(self):
        self.pixiv=Pixiv() #实例化Pixiv
        self.imgs=Imgs()
        self.se=self.pixiv.se #传递se
        self.uid="4819066"
        self.pixiv.load_path="D:\备份\pixiv\画师\/"+self.uid+"/"
        self.all_url="https://www.pixiv.net/ajax/user/"+self.uid+"/profile/all" #获取所有插图作品目录
        self.medium_url="https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" #获取插图主页的url

    def get_Member_illust(self):
        if os.path.exists(self.pixiv.load_path) == False:
            os.mkdir(self.pixiv.load_path)

        obj=json.loads(self.pixiv.get_Html(self.all_url))
        illusts = obj["body"]["illusts"]
        if illusts == None:
            print ("获取作品目录失败")
            return
        print ("已获取所有插画作品")

        list=[]
        for file in os.listdir(self.pixiv.load_path):
            list.append(file.replace(".jpg",""))

        for illust in illusts :
            if illust in list:
                continue

            page_url=self.medium_url+illust
            img_url=self.pixiv.get_Imgs_Url(page_url)
            img_file = self.pixiv.download_Img(img_url, page_url, illust)
            if img_file == None:
                print ("下载失败"+illust)

        print ("已获取排行榜数据")


    def start(self):
        if self.pixiv.login() :
            self.get_Member_illust()


if __name__ =="__main__":
    Member_illust().start()