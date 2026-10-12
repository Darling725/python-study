input ("有一个长阶梯，若每步上 2 阶，最后剩 1 阶；若每步上 3 阶，最后剩 2 阶；若每步上 5 阶，最后剩 4 阶；若每步上 6 阶，最后剩 5 阶；只有每步上 7 阶，最后刚好一阶也不剩\n一共有多少台阶？\n")
step = 0
while step < 10000:
    if step % 2 == 1 and step % 3 == 2 and step % 5 == 4 and step % 6 == 5 and step % 7 == 0:
        print(f"一共有{step}个台阶")
        break
    else:
        step = step + 7

input("回车结束")
