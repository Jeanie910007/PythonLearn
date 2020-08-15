# 抓取PPT電影版網頁原始碼 (HTML)
import urllib.request as req
def getData(url):
    #建立一個request 物件 附加Request Header 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")

    for title in titles:
        if title.a != None and "Re:" not in title.a.string: #如果標題有a則印出
            print(title.a.string)
    #抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁") #找內文是 ‹ 上頁的a標籤
    # print(nextLink["href"])
    return nextLink["href"]



pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
counter = 0
while counter<20:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    counter+=1