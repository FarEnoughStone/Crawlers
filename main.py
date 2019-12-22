#!/usr/bin/python3

import urllib.request
import novel_utils
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

URL="https://www.ionemanhua.com/10261/1/167.html"
text_url="http://www.303afaf.com/arts/573719.html"
headers = {"user-agent":"Mozilla/5.0"}

# if __name__ == "__main__":
    
#     # 利用PhantomJS加载网页
#     browser = webdriver.PhantomJS(executable_path=r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe")
#     # browser=webdriver.Chrome(executable_path=r"D:\Program Files (x86)\chromedriver.exe")
#     browser.set_page_load_timeout(30) # 最大等待时间为30s
#     #当加载时间超过30秒后，自动停止加载该页面
#     try:
#         browser.get(URL)
#     except TimeoutException:
#         browser.execute_script('window.stop()')
#     source = browser.page_source #获取网页源代码
#     # browser.quit()
#     #解析网页，获取下载图片的网址
#     soup = BeautifulSoup(source, 'html.parser')
#     print(soup.title)
#     img_list=soup.find_all(class_="mh_comicpic")
#     print(len(img_list))
#     for node in img_list:
#         try:
#             print(node.img['src'])
#         except Exception:
#             print(node.img)


if __name__ == "__main__":
    novel_utils.requestWeb(text_url)
    # response=urllib.request.Request(text_url, headers=headers)
    # html=urllib.request.urlopen(response)
    # print("请求返回码："+str(html.getcode()))
    # # print(html.read().decode("utf-8"))
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup.title)
    # text_list=soup.find_all(class_="cont")
    # print(text_list[0].div)
    
    # mh_mangalist=soup.find_all(class_="mh_mangalist tc")
    # print(mh_mangalist)
    # mh_comicpic=mh_mangalist[0].find_all('div')
    # print(len(mh_comicpic))
    # for node in mh_comicpic:
    #     print(node.get_text())