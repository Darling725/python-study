temp = input("今年是几几年:\n")
year = int(temp)

if (not bool(year % 4) and  bool(year % 100)) or not bool(year % 400):
    print(f"{temp}是闰年")
else:
    print(f"{temp}不是闰年")

input("几几年就去洗")
