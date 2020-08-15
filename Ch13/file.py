#儲存檔案
# file = open("data.txt", mode="w",encoding="utf-8") #中文編碼utf8
# file.write("Hello File\nSecond Line\n測試中文")
# file.close()
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")

#讀取檔案
#把檔案中的數字資料一行一行讀取

# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)


# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)


#使用JSON格式讀寫 複寫
import json
with open("config.json",mode='r') as file:
    data=json.load(file)  #data 是字典形式
print(data)
# print("name",data["name"])
# print("version",data["version"])
data["name"]="New name" #修改變數資料
#把最新資料複寫回資料中
with open("config.json",mode='w') as file:
    json.dump(data,file)