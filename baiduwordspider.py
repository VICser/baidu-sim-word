import requests
import random
import csv
from bs4 import BeautifulSoup

def get_host_and_port(file_path):
    fp = open(file_path,'r')#加载ip地址文件
    ips = fp.readlines()
    proxys = list()
    for p in ips:#将文件中的ip与端口处理成我们需要的格式
        ip =p.strip().split('\t')
        proxy = 'http:\\' +  ip[0].strip() + ':' + ip[1].strip()
        proxies = {'proxy':proxy}
        #print(proxies)
        proxys.append(proxies)
    return proxys

def gethtml(url,proxys):#传入目标链接，获取网页源码
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    try:
        s = requests.get(url,headers = header)#每次请求随机使用代理ip，设置超时限制为3秒
        s.encoding = "utf-8"
        text = s.text
    #print(text)
        return text
    except Exception as e:
        print(e)


def get_sim_word(html):#网页源码解析函数，获取需要信息
    soup = BeautifulSoup(html,'html.parser')
    key_item = soup.select("a[class='viewTip-icon']")
    #print(key_item)
    if key_item != None:
        if len(key_item) > 0 and key_item[0].get_text() == "同义词":
            sim_word = soup.select("h1")
            if len(sim_word) > 0:
                print("同义词为"+sim_word[0].get_text())
                word = sim_word[0].get_text()
                return word
            else:
                print("error: 未获取到同义词")
        else:
            print("没有同义词")

def test():
    test_url = gethtml("https://baike.baidu.com/item/帝都")
    get_sim_word(test_url)

def main():
    dir = "./data/"
    host_file_path = dir + "host_new.txt"
    word_file_path = dir +"wordsWithCount.csv"
    sim_word_file = dir +"baidu_sim_word.csv"
    proxys = get_host_and_port(host_file_path)
    word_pool = []
    with open(word_file_path,"r",encoding="utf-8") as f:
        reader = csv.reader( (line.replace('\0','') for line in f) )
        for line in reader:
            word_pool.append(line[0])
    with open(sim_word_file,"a",encoding="GB18030") as g:
        for line in word_pool:
            print(line)
            html = gethtml("https://baike.baidu.com/item/"+line,proxys)
            sim_word = get_sim_word(html)
            if sim_word != None:
                print("get one!!!")
                g.write(line)
                g.write(",")
                g.write(sim_word)
                g.write("\n")

if __name__ == '__main__':
    main()