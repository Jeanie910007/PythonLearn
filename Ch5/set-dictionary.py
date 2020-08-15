#集合的運算
s1={3,4,5}
s2={4,5,6,7}
#print(3 in s1) #看3有沒有在s1中
#print(10 in s1) #看10有沒有在s1中
#print(10 not in s1) #看10有沒有在s1中

#s3 = s1&s2 #交集
#s3 = s1|s2 #聯集
#s3 = s1-s2 #差集
#s3 = s1^s2 #反交集

#s=set("Hello") #把字串中的字母拆解集合 set(字串)
#print("H" in s) #測H是否在s集合中


#字典 key-value 配對
#dic = {"apple":"蘋果","bug":"蟲蟲"}
#dic["apple"]="小蘋果"
#print(dic["apple"])


#dic = {"apple":"蘋果","bug":"蟲蟲"}
#print("apple" in dic) #判斷key 是否存在
#print(dic) 
#del dic["apple"] #刪除字典中的鍊值對
#print("apple" in dic) #判斷key 是否存在

dic={x:x*2 for x in [3,4,5]} #從列表中的資料產生字典
print(dic)