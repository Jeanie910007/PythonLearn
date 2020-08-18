#載入內建sys模組
# import sys as s
# print(s.platform)
# print(s.maxsize)


#建立geometry 模組,載入使用
# import geometry
# result = geometry.distance(1,1,5,5)
# print(result)
# result = geometry.slope(1,2,5,6)
# print(result)

#調整搜尋模組的路徑
# import sys
# sys.path.append("modules") #在模組的搜尋路徑新增路徑
# print(sys.path) #印出模組搜尋路徑
import geometry
print(geometry.distance(1,1,5,5))