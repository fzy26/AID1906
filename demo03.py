"""
    字典：
    15:35
    练习:exercise04.py
    练习:exercise05.py
    练习:exercise06.py
"""

# 1. 创建字典
# 空
dict01 = {}
dict01 = dict()

# 具有默认值
dict02 = {"qtx":18,"ls":20,"ww":23}
list01 = [["a","b"],("c","d")]
dict02 = dict(list01)
print(dict02)

# 2. 添加元素
# 第一次(没有该键)添加
dict02["键"] = "值"

# 3. 修改元素
dict02["键"] = "值2"
dict02["a"] = "B"
print(dict02)

# 4. 删除
del dict02["键"]
print(dict02)

# 5.查找单个元素
# 在查找元素时,如果字典中不存在该键，则错误.
# 所以查找前，一定通过in判断。
if "qtx" in dict02:
    print(dict02["qtx"])
else:
    print("不存在")
# del dict02["qtx"]#　KeyError:

# 获取所有元素
for key in dict02:
    print(key)# 键
    print(dict02[key])# 键 --> 值

# # (键,值)
# for item in dict02.items():
#     print(item[0])
#     print(item[1])

# (键,值)
for key,value in dict02.items():
    print(key)
    print(value)

# 获取字典中所有值
for value in dict02.values():
    print(value)


# 在python3.6以后,字典在功能上体现了加入的顺序.
dict02["三丰"] = 128
dict02["无忌"] = 28
dict02["翠山"] = 35
for item in dict02:
    print(item)






