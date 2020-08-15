# 判斷式
#x = input ("請輸入數字:") #取得字串形式
#x = int(x) #將字串型態轉換成數字型態
#if x>100:
#    print("True 執行")
#elif x>50:
#    print("True 執行")
#else:
#    print("False 執行")

n1 = int (input("數字1: "))
n2 = int (input("數字2: "))
op = input("請輸入運算: +, -, *, /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算!")
    