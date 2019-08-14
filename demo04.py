"""
    字典推导式
    练习：exercise07.py
    练习：exercise08.py
"""
# 需求:range(10)  key 0---9   value 键的平方

dict01 = {}
for item in range(10):
    dict01[item] = item ** 2

dict02 = {item: item ** 2 for item in range(10)}

# 需求:range(10) 大于5的数， key 0---9   value 键的平方
dict01 = {}
for item in range(10):
    if item > 5:
        dict01[item] = item ** 2

dict02 = {item: item ** 2 for item in range(10) if item > 5}
print(dict01)
print(dict02)





