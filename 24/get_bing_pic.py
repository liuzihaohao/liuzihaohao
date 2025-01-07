import requests,time,json,os
from bs4 import BeautifulSoup

url="https://cn.bing.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
}
res = requests.get(url, headers=headers)

soup=BeautifulSoup(res.text,"html.parser")
nowtime=time.localtime()

picid="_".join(str(soup.find_all(class_="img_cont")[0]["style"]).split(";")[0].split("\"")[1].split("=")[1].split("&")[0][:-5].split("_")[:-1])[4:]

obj={
    "id":picid,
    "img":{
        "800x480":"https://bing.com/th?id=OHR.{}_800x480.jpg&qlt=100".format(picid),
        "1920x1080":"https://bing.com/th?id=OHR.{}_1920x1080.jpg&qlt=100".format(picid),
        "UHD":"https://bing.com/th?id=OHR.{}_UHD.jpg&qlt=100".format(picid),
    },
    "title":soup.find_all(class_="musCardCont")[0].find_all("h3")[0].find_all("a")[0].text,
    "copyright":soup.find_all(class_="copyright-container")[0].text,
    "time":{
        "year":nowtime.tm_year,
        "mon":nowtime.tm_mon,
        "day":nowtime.tm_mday,
    },
}

def qzero(x):
    if len(x)==1:
        return "0"+x
    else:
        return x

obj1=obj
obj=json.dumps(obj)

cr_dir=os.path.join("/root/bingpic/",str(nowtime.tm_year))
try:
    os.makedirs(cr_dir)
except FileExistsError:
    pass
with open(os.path.join(cr_dir,str(nowtime.tm_year)+qzero(str(nowtime.tm_mon))+qzero(str(nowtime.tm_mday))+".json"),"w+",encoding="utf-8") as fp:
    fp.write(obj)

res = requests.get(obj1["img"]["800x480"], headers=headers)
with open(os.path.join(cr_dir,obj1["id"]+"_800x480.jpg"),'wb') as fp:
    fp.write(res.content)

res = requests.get(obj1["img"]["1920x1080"], headers=headers)
with open(os.path.join(cr_dir,obj1["id"]+"_1920x1080.jpg"),'wb') as fp:
    fp.write(res.content)

res = requests.get(obj1["img"]["UHD"], headers=headers)
with open(os.path.join(cr_dir,obj1["id"]+"_UHD.jpg"),'wb') as fp:
    fp.write(res.content)
