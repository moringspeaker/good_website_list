import requests
from bs4 import BeautifulSoup
import re
# list=[]
# with open('good_websites.txt','r') as f:
#     line=f.readlines()
#     for i in line:
#         i=i.replace('\n','')
#         list.append(i)

target='https://www.lezy.cn/site_44.html'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'accept-encoding':'gzip, deflate, br',
    'referer':'https://www.lezy.cn/',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6'
}
res=requests.get(target,headers=headers)
soup=BeautifulSoup(res.content,'lxml')
link=str(soup.find('span',text=re.compile(r'站点域名')).get_text())
link_new=link.replace('站点域名：','')
print(link_new)
