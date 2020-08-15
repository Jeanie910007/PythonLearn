#網路連線
# import urllib.request as request
# src="http://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得原始碼(HTML CSS JS)
# print(data)

#串接 擷取公開資料
import urllib.request as request
import json #資料是json格式
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) #取得原始碼(HTML CSS JS)
# print(data)
#取得公司名稱
clist=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        # print(company["公司名稱"])
        file.write(company["公司地址"]+"\n") #LB的格式






