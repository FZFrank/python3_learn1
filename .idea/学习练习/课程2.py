import random
secret = random.randint(1,10)
print('------------------我爱鱼C工作室----------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")

while temp.isdigit() != True:
    temp = input("输入格式不正确，请重新输入整数：")

guess = 0

while guess != secret:
    guess = int(temp)
    if guess == secret:
        print("卧槽，你是小甲鱼心里的蛔虫马?!")
        print("哼，猜中了也没有奖励")
    else:
        if guess > secret:
            print("哥，大了大了~~")
        else:
            print("嘿，小了！小了！！")
        temp = input("哎呀，猜错了，请重新输入吧：")
print("游戏结束，不玩啦^_^")