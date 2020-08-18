import blog.count
import blog.printcase
c = blog.count #縮寫
p = blog.printcase #縮寫

x = input("輸入x值: ")
y = input("輸入y值: ")
w = input("輸入計算符號: ")
x = int(x)
y = int(y)
if w=="+":
    print(c.plus(x,y))
elif w=="-":
    print(c.minus(x,y))
elif w=="*":
    print(c.times(x,y))
elif w=="/":
    print(c.divided(x,y))
else:
    print("Error Input!")

p.two(x)