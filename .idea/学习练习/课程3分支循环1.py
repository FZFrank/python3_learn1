#0  if money>=100:
#1 断言，不满足条件时直接报错终止程序
#2 x,y,z=y,z,x
#3 x
#没有

#0
score = int(input("input score:"))
if score < 0 or score > 100:
    print("输入错误")
elif 60 <= score <80:
    print("C")
elif 90 <= score <=100:
    print("A")
elif 80 <= score < 90:
    print("B")
else:
    print("D")

#1
x=1,y=2,z=3
small=x if (x<y and x<z) else (y if y<z else z)