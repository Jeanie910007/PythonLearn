# 抓取PPT電影版網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個request 物件 附加Request Header 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

#解析原始碼 取得章節標題
# import bs4
# root=bs4.BeautifulSoup(data,"html.parser")
# print(root.title.string)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
# titles=root.find("div",class_="title") #尋找class = "title" 的div標籤
# print(titles.a.string)

titles=root.find_all("div",class_="title")
with open("data.txt",mode="w",encoding="utf-8") as file:
    for title in titles:
        if title.a != None: #如果標題有a則印出
            # print(title.a.string)
            file.write(title.a.string+"\n")

