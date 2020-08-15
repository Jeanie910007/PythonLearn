#主程式
#要在封包資料夾中加 __init__.py 檔
import geometry.point
import geometry.line

result = geometry.point.distence(3,4)
print("距離",result)

result = geometry.line.slope(1,1,3,3)
print("斜率",result)