
import urllib.request
import re
import requests

'''
定向爬虫：
    爬取网页数据，获取想要的图片
    https://www.jikexueyuan.com/ 爬取极客学院网站首页的图片
'''

def get_baidu_com():
    res=urllib.request.urlopen("https://www.jikexueyuan.com/")
    html=res.read()
    pic_url=re.findall('img src="(http:.*?)"',html.decode("utf-8"),re.S)
    i=0
    for each in pic_url:
        print('now downloading:' + each)
        pic = requests.get(each)
        fp=open("F:\pics\\"+str(i)+".png",'wb')
        fp.write(pic.content)
        fp.close()
        i +=1

get_baidu_com()
