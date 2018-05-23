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

#0 5次
#1 报错
#2 break跳出循环，continue执行下一个循环
#3 变量集
#4 0，1，2，3，4，5，6，7，8，9
#5 2 3
#6 必须进入循环体，在循环中设置跳出
#7
string = 'IloveFishC.com'
for i in string:
    print(i)

#0
secret = "FishC.com"
a = input("请输入密码:")
i = 3
while i > 0:
    if a == secret:
        break
    elif '*' in a:
        a = input("密码中不能含有\"*\"!宁还有三次机会! 请输入密码:")
        continue
    else:
        s1 = "密码输入错误!您还有 "+str(i)+" 次机会请输入密码:"
        a = input(s1)
        i-=1
if i >0:
    print("密码输入正确，进入程序......")
else :
    print("超过重试次数")

#1
for i in range(100,1000):
    s = 0
    for j in str(i):
        s=s+int(j)**3
    if i == s:
        print(i)
    else :
        continue

#2
for i in range(4):
    for j in range(4):
        s='红球'+str(i)+'个'+'黄球'+str(j)+'个'+'蓝球'+str(8-i-j)+'个'
        print(s)
