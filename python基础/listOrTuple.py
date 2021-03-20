# 使用list和tuple
# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
len(classmates)

# 可变有序表
# 追加
classmates.append('Adam')
# 把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
# 删除list末尾的元素，用pop()方法：
classmates.pop()
# 指定第几个
classmates.pop(1)

# tuple
# 一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates2 = ('Michael', 'Bob', 'Tracy')

# 要定义一个只有1个元素的tuple，如果你这么定义
t = (1) # 是错的。括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
t = (1,) #这样才是元组
