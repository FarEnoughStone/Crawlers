import urllib.request
import _thread
import threading
from bs4 import BeautifulSoup

novel_dir="f:/Crawlers Novel/"
headers = {"user-agent":"Mozilla/5.0"}

rootUrl="http://www.303afaf.com"
baseUrlStart="http://www.303afaf.com/artlist/19"
baseUrlEnd=".html"


def requestWeb(url):
    response=urllib.request.Request(url, headers=headers)
    html=urllib.request.urlopen(response)
    if html.getcode()==200:
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.title)
        text_list=soup.find_all(class_="cont")
        writeToFile(str(soup.title),str(text_list[0].div))



def writeToFile(title,conext):
    filename=novel_dir+title.replace("</title>","").replace("<title>","")+".txt"
    file=open(filename,'w+')
    text=conext.replace("<br/>","\r\n")
    file.write(text)
    file.close


def getUrl(url):
    print("开始访问："+url)
    response=urllib.request.Request(url, headers=headers)
    html=urllib.request.urlopen(response)
    if html.getcode()==200:
        soup = BeautifulSoup(html, 'html.parser')
        node_list=soup.find_all(class_="name")
        for node in node_list:
            # print(node.a["title"])
            nodeUrl=rootUrl+str(node.a["href"])
            try:
                requestWeb(nodeUrl)
            except Exception:
                print("异常："+nodeUrl)


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.startNum = num
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        for i in range(self.startNum*10,self.startNum*10+10): 
            theUrl=baseUrlStart+"-"+str(i)+baseUrlEnd
            getUrl(theUrl)



if __name__ == "__main__":
    # for i in range(40,53): #not include 100
    #     thThread=myThread(i)
    #     thThread.start()
    for i in range(530,536): 
            theUrl=baseUrlStart+"-"+str(i)+baseUrlEnd
            getUrl(theUrl)

    