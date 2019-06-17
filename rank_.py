# coding=utf-8
from bs4 import BeautifulSoup
from pixiv_ import Pixiv
from gate_img import Imgs
import os
import json
import util
import time

class Rank:
    def __init__(self):
        self.pixiv=Pixiv() #实例化Pixiv
        self.imgs=Imgs()
        self.se=self.pixiv.se #传递se
        self.pixiv.load_path="D:\备份\pixiv\日推\/"+str(time.strftime('%Y%m',time.localtime(time.time()))).replace("2019","19")+\
                             "/"+str(time.strftime('%Y%m%d',time.localtime(time.time()))).replace("2019","19")
        self.rank_url="https://www.pixiv.net/ranking.php?mode=daily&" #排行榜地址
    def get_Rank_List(self):
        html=self.pixiv.get_Html(self.rank_url)
        #html=open("D://test","r").read()
        rank_soup = BeautifulSoup(html, 'lxml')  # 传入排行榜所在的html
        sections =rank_soup.find_all('section',attrs={'class','ranking-item'})

        filelist = []
        if os.path.exists(self.pixiv.load_path) == False:
            os.mkdir(self.pixiv.load_path)

        for file in os.listdir(self.pixiv.load_path):
            filelist.append(file.replace(".jpg", ""))

        filelist=json.dumps(filelist)
        print ("已获取排行榜数据")
        i=0
        for section in sections:
            a=section.find("a", attrs={'class', 'work'})
            if a == None:
                continue
            page_url=self.pixiv.main_url+ a.get("href")
            page_title=section.get("id")+"_#_"+util.deleteSpecialChar(section.get('data-title'))+"_#_"+util.deleteSpecialChar(section.get('data-user-name'))
            if page_title in json.loads(filelist):
                continue

            img_url=self.pixiv.get_Imgs_Url(page_url) #从图片所在页面或者原始大图的url
            if img_url == None:
                continue
            print("正在下载"+page_title)
            img_file=self.pixiv.download_Img(img_url,page_url,page_title) #下载原始图片
            if img_file != None:
                self.imgs.post_file(img_file) #下载成功则上传图片

    def start(self):
        if self.pixiv.login() :
            self.get_Rank_List()


if __name__ =="__main__":
    Rank().start()