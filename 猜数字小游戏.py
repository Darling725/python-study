input("Python做的第一个猜数字小游戏")

import random#提名random

answer = random.randint(1,10)#用random使answer变成随机数

counts = 5#用户可以猜的次数，可以改

while counts > 0:
    temp = input("猜猜我想的数字:\n")
    guess = int(temp)#int()把guess变成数字
    if guess == answer:
        print("猜对了！！")
        print("你怎么这么厉害")
        break#避免用户猜对却一直重复，用beak直接跳出while循环
    else:
        if guess > answer:
            print("大了哦")
        else:
            print("小了哦")
    counts = counts - 1#必须与前面的else对齐，用户猜错就能运行-1
    

    
print("游戏结束")

input("···按回车结束游戏···")
