#######单独使用beautifulsoup不能爬取动态网页的全部数据#######


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import csv
# 网易云音乐歌单首页的url
url = 'http://music.163.com/#/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
html = requests.get(url, headers=headers)
content = html.text

print(content)

# soup = BeautifulSoup(content)
# result = soup.findall(id='m-pl-container')
#
# # 创建储存歌单的文件
# csv_file = open("playlist.csv", "w", encoding='GB2312', newline='')
# writer = csv.writer(csv_file)
# writer.writerow(['标题', '播放数', '链接'])
# # 解析每一页，直到下一页为空
# while url != 'javascript:void(0)':
#     html = requests.get(url).content
#     soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#     result = soup('div')
#
# csv_file.close()



