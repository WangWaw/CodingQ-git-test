from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
# 网易云音乐歌单首页的url
url = 'http://music.163.com/#/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# 用PhantomJS接口创建一个Selenium的Webdriver
# driver = webdriver.PhantomJS()
# options = webdriver.ChromeOptions()
options = Options()
options.add_argument('headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)
# 创建储存歌单的文件
csv_file = open("playlist.csv", "w", encoding='utf-8-sig', newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])
# 解析每一页，直到下一页为空
while url != 'javascript:void(0)':
    # 用WebDriver加载页面
    driver.get(url)
    # 切换到内容的iframe
    driver.switch_to.frame("contentFrame")
    # 定位歌单标签
    data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    # 解析每一页的所有歌单
    for i in range(len(data)):
        # 获取播放数
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0]) > 1000:
            # 获取播放数大于1000万的歌单封面
            msk = data[i].find_element_by_css_selector("a.msk")
            # 把封面标题，连接，播放数写到文件
            writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
    # 定位下一页的url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
csv_file.close()
