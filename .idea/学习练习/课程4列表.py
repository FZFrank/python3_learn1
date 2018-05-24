#0 [1,2,3,4,5]
#1 list1[1][2][0]='小鱿鱼'
#2 sort
#3 sort(reverse=True)
#4 copy拷贝列表，clear清空列表,无参数
#5
list1 = []
for x in range(10):
    for y in range(10):
        if x%2 == 0 and y%2 != 0:
            list1.append((x,y))
print(list1)

等价于

list1 = [(x,y) for x in range(10) for y in range(10) if x%2 == 0 if y%2 != 0]

#6
list1 = ['1.just do it','2.一切皆有可能','3.让编程改变世界','4.impossible is noting']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [ y+':'+x.split('.')[1] for x in list1 for y in list2 if x.split('.')[0] == y.split('.')[0]]
for each in list3:
    print(each)

#7