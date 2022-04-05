import requests
from bs4 import BeautifulSoup
import re

def read_sites():
    list = []
    with open('good_websites.txt', 'r') as f:
        line = f.readlines()
        for i in line:
            i = i.replace('\n', '')
            list.append(i)
    return list

def get_link(target):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'accept-encoding': 'gzip, deflate, br',
        'referer': 'https://www.lezy.cn/',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6'
    }
    try:
        res = requests.get(target, headers=headers,timeout=4)
        soup = BeautifulSoup(res.content, 'lxml')
        link = str(soup.find('span', text=re.compile(r'站点域名')).get_text())
        link_new = link.replace('站点域名：', '')
        return link_new
    except:
        return -1

def judge(link1,list):
    link2='http://'+link1+'/'
    link3='https://'+link1+'/'
    if link2 in list or link3 in list:
        return True
    else:
        return False

if __name__=='__main__':
    list=read_sites()
    print(list)
    origin= 'https://www.lezy.cn/site_'
    for i in range(0,435):
        target=origin+str(i)+'.html'
        href=get_link(target)
        if href!=-1 and href !='':
            if judge(href,list)==False:
                href='https://'+href+'/'
                list.append(href)
                print(href)
            else:
                continue
        else:
            print('找不到页面')
            continue
    with open('good_websites2.txt','w') as tf:
        textrue='\n'.join(list)
        tf.write(textrue)