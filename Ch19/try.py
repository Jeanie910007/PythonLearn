# 抓取PPT電影版網頁原始碼 (HTML)
import urllib.request as req
url="https://www.google.com/search?sxsrf=ALeKk03VMy6xxRVwXYi007cUTpfAWi3dgQ%3A1597389476935&ei=pDo2X_HTOJC2mAXcq4GgCQ&q=%E9%82%B1%E7%BE%A4%E7%94%AF&oq=%E9%82%B1%E7%BE%A4%E7%94%AF&gs_lcp=CgZwc3ktYWIQAzIFCAAQzQIyBQgAEM0CMgUIABDNAjoECAAQRzoCCAA6BQgAELEDOgQIIxAnOggIABCxAxCDAToECAAQDVDRjxRYm5sUYMmeFGgAcAF4AIABNIgBhgSSAQIxMpgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwjxtdzCk5rrAhUQG6YKHdxVAJQQ4dUDCAw&uact=5"
#建立一個request 物件 附加Request Header 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="rc") #尋找class = "title" 的div標籤
for title in titles:
    if title.h3.string != None:
        print(title.h3.string)

# titles=root.find_all("div",class_="title")
# for title in titles:
#     if title.a != None: #如果標題有a則印出
#         print(title.a.string)