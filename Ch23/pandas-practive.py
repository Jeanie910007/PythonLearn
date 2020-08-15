#載入 pandas 模組
import pandas as pd;
# #建立 Series
# data1 = pd.Series([ 10, 15, 20])
# data2 = pd.Series([ "ning", "lulu", "bae"])
#基本 Series 操作
# print(data)
# print("Max",data.max())
# print("Medium",data.median())
# data = data*2
# print(data)
# data2=data2=="lulu"
# print(data2)

#建立 DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,40000,50000]
})
#基本 DataFrame 操作
# print(data)
# 取得特定的欄位
# print(data["name"])
# 取得特定的列
print(data.iloc[0])