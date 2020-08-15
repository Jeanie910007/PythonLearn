# #Point 實體物件的設計:平面座標上的點

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5


# p1=Point(3,4)
# p2=Point(5,6)
# print(p1.x,p1.y) # =p1.show
# print(p2.x,p2.y) # =p2.show

# p1.show()
# p2.show()
# result=p1.distance(0,0)
# print(result)


#File 實體物件的設計:包裝檔案讀取的程式
class File:
    def __init__(self, name):
        self.name=name
        self.file=None #尚未開啟檔案:初期是None
    def open(self):
        self.file=open(self.name,mode='r',encoding="utf-8")
    def Read(self):
        return self.file.read() #這裡的read是檔案讀取的read

# 讀取第一個檔案
f1=File("data1.txt")
f1.open()
data=f1.Read()
print(data)


# 讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.Read()
print(data)