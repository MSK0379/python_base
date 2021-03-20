# 字符编码
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

# Python的字符串
print('包含中文的str')
# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('苗'))
print(chr(ord('苗')))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

# 格式化
# 1.用%实现
# 2.format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

r = 1
s = 2
print(f'The area of a circle with radius {r} is {s:.2f}')