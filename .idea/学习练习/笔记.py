#IDLE
#r'' 原始字符串，将''内的字符串全部转义，但结尾的\不能转义
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
print("密码输入正确，进入程序......")