import requests
from bs4 import BeautifulSoup


def spider():
    headers = {'Connection': 'keep - alive',
               'Cookie': 'BAIDUID=0427D9CA054D5F52648EFA4CCD6E0B2E:FG=1; nonUnion=1; v_pg=205; s_ht_pageid=16; ft=1; v_pg=normal; hz=0; hword=4; hide_top=1; org=1; zhankai=1; tnwhiteft=XzFYUBclcMPGIANCmytknWnBQaFYTzclnHmYrH0dPjb3PZY',
               'Host': 'www.hao123.com',
               'Pragma': 'no - cache',
               'Rerer': 'https://cn.bing.com/',
               'sec - ch - ua': '" Not A;Brand"; v = "99", "Chromium"; v = "100", "Google Chrome"; v = "100"',
               'sec - ch - ua - mobile': '?0',
               'sec - ch - ua - platform': '"Windows"',
               'Sec - Fetch - Dest': 'document',
               'Sec - Fetch - Mode': 'navigate',
               'Sec - Fetch - Site': 'cross - site',
               'Sec - Fetch - User': '?1',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    target='https://www.hao123.com/'
    html=requests.get(target,headers=headers)
    soup=BeautifulSoup(html.content,'lxml')
    links=soup.find_all('a',class_='sitelink icon-site')
    list=[]
    for i in links:
        if i not in list:
            list.append(i.get('href'))
        else:
            continue
    with open('good_websites.txt','a')as f :
        for item in list:
            f.write(item+'\n')
if __name__=='__main__':
    spider()