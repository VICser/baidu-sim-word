import requests
import random
from bs4 import BeautifulSoup

f = open("host_new.txt","a")
def gethtml(url):#传入目标链接，获取网页源码
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    s = requests.get(url,headers = header)#每次请求随机使用代理ip，设置超时限制为3秒
    s.encoding = "utf-8"
    text = s.text
    #print(text)
    return text

def get_ip(html):
    soup = BeautifulSoup(html,'html.parser')
    ip_items = soup.find_all("tr",class_="odd")
    for i in ip_items:
        a = i.find_all("td")
        ip = list(a)[1].get_text()
        port = list(a)[2].get_text()
        f.write(ip)
        f.write("\t")
        f.write(port)
        f.write("\n")
for  i in range(1,11):
    a = gethtml("http://www.xicidaili.com/nn/%s"%i)
    get_ip(a)