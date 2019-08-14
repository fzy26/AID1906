# 练习1:使用range生成1--10之间的数字,将数字的平方存入list01中
# list01 = []
# for item in range(1,11):
#     list01.append(item ** 2)

list01 = [item ** 2 for item in range(1,11)]
print(list01)
# 练习2:将list01中所有奇数存入list02
# list02 = []
# for item in list01:
#     if item % 2:
#         list02.append(item)
list02 = [item for item in list01 if item % 2]
print(list02)

# 练习3:将list01中所有偶数增加10之后存储list03

list03 = [item + 10 for item in list01 if item % 2 == 0]
print(list03)
