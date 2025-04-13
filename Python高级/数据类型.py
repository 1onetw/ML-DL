import math
import random


# 数据类型

## 数据类型 bytes：不可变的二进制序列
x1 = bytes("hello", encoding="utf-8")

x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")
    
## 数据类型转换
eval("[1, 2]") # 字符串转表达式
repr(x) # 将对象转换为字符串

frozenset('hello') # 转化为不可变集合

chr(65) # 将整数转换为字符
ord('A') # 将字符转换为整数

hex(2) # 将整数转换为十六进制字符串
oct(3) # 将整数转换为八进制字符串4

## 运算符
### 位运算符 & | ^ ~ << >>
### 逻辑运算符 and or not
### 成员运算符 in not in
### 身份运算符 is is not   id() 函数用于获取对象内存地址
"""
    is 与 == 区别：

    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
"""

## 数字
### 数学函数
abs(-1)
round(1.5) # 四舍五入
round(1.5, 1) # 保留一位小数
math.ceil(1.1) # 向上取整
math.floor(1.1)
math.log(2) # 自然对数
math.log10(100) # 以10为底的对数
math.exp(2) # e^2
math.sqrt(4) # 平方根
math.pow(2, 3)
math.factorial(5) # 阶乘
math.pi
math.e

### 随机数函数
# random.choice(seq) # 从序列中随机选择一个元素
# randrange ([start,] stop [,step]) # 随机选择一个整数，范围是 [start, stop) 或 [0, stop)
random.random() # 随机选择一个浮点数，范围是 [0.0, 1.0)
# shuffle(lst) # 将列表中的元素随机排序
# random.uniform(x, y) # 随机选择一个浮点数，范围是 [x, y)

### 三角函数
math.acos(x)
math.asin(x)
math.atan(x)
math.cos(x)
math.sin(x)
math.tan(x)

## 字符串
### 转义字符
#### \r 表示原始字符串，不进行转义
#### \n 表示换行
#### \t 表示制表符
#### \b 表示退格符
#### \f 表示换页符
#### \r 表示回车符
#### \' 表示单引号
#### \" 表示双引号
#### \\ 表示反斜杠
#### \xhh 表示十六进制字符
#### \ooo 表示八进制字符
#### \0 表示空字符

### \r实现百分比进度条
import time
# 动态更新控制台进度显示：
# - 使用回车符'\r'覆盖当前行，实现进度条原地更新效果
# - {i:3}% 将进度值格式化为3位固定宽度的百分比数
# - end='' 禁止自动换行，保持输出在同一行
# - flush=True 强制立即刷新输出缓冲区，确保实时显示
for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    time.sleep(0.05)
print()

### Unicode字符串
"""
    在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。

    在Python3中，所有的字符串都是Unicode字符串。
"""

### 字符串内置函数
str1 = "Hello, World!"
# str.capitalize() # 将字符串的第一个字符转换为大写

# str.casefold() # 将字符串转换为小写

# str.center(width [, fillchar]) # 将字符串居中，并填充指定字符

# str.count(sub [, start [, end]]) # 返回字符串中子字符串出现的次数

str1.encode(encoding='utf-8', errors='strict') # 将字符串编码为bytes对象,如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

# str.endswith(suffix [, start [, end]]) # 判断字符串是否以指定后缀结尾

bytes.decode(encoding="utf-8", errors="strict") # 将bytes对象解码为字符串

str1.find(str, beg=0, end=len(str1)) # 检测字符串中是否包含子字符串，如果包含则返回子字符串的索引，否则返回-1
	
str1.index(str, beg=0, end=len(string)) # 检测字符串中是否包含子字符串，如果包含则返回子字符串的索引，否则报一个ValueError 的异常

# isalnum() # 判断字符串是否只包含字母和数字

# isalpha() # 判断字符串是否只包含字母

# isdigit() # 判断字符串是否只包含数字

# islower() # 判断字符串是否只包含小写字母

# isspace() # 判断字符串是否只包含空格

# isupper() # 判断字符串是否只包含大写字母

# str.join(seq) # 将序列中的元素连接成一个字符串，元素之间用指定的分隔符连接
# split(str="", num=string.count(str)) # 将字符串分割成列表，分隔符为指定的字符串，num表示分割次数，默认值为-1，表示分割所有

# strip() # 删除字符串首尾的空格
# lstrip() # 删除字符串左侧的空格 
# rstrip() # 删除字符串右侧的空格

# str.replace(old, new [, max]) # 将字符串中的old替换为new，如果max指定了替换次数，则替换次数最多为max次

# swapcase() # 将字符串中的大写字母转换为小写字母，小写字母转换为大写字母

# title() # 将字符串中的每个单词的首字母转换为大写字母，其余字母转换为小写字母

## 列表
### 列表比较
# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

### 列表内置函数
"""
    列表内置函数
    
    列表的常用内置函数如下：
    
    append() 添加一个元素到列表的末尾
    clear() 清空列表
    copy() 返回列表的浅拷贝
    count() 返回列表中指定元素的出现次数
    extend() 将一个列表的元素添加到另一个列表的末尾
    index() 返回列表中指定元素的索引
    insert() 在指定位置插入一个元素
    pop([index=-1]) 删除列表中指定位置的元素(默认最后一个元素)，并返回该元素的值,
    remove() 删除列表中指定值的元素
    reverse() 反转列表中的元素
    sort( key=None, reverse=False) 对列表中的元素进行排序
    
"""

## 元组
"""
关于元组是不可变的
所谓元组的不可变指的是元组所指向的内存中的内容不可变。
"""

tup = ('r', 'u', 'n', 'o', 'o', 'b')
id(tup)     # 查看内存地址
tup = (1,2,3)
id(tup) # 内存地址不一样了

## 字典
# dict.copy() # 浅拷贝
# dict.get(key, default=None) # 返回指定键的值，如果键不存在，则返回默认值
# dict.update(dict2) # 更新字典，将dict2中的键值对添加到dict中，如果键已经存在，则更新其值
# dict.fromkeys(seq[, value]) # 创建一个新字典，以指定的键和默认值创建字典
# dict.pop(key[,default]) # 删除指定键的键值对，并返回该键的值，如果键不存在，则返回默认值
# dict.popitem() # 删除字典中的最后一个键值对，并返回该键值对的元组

## 集合：无序不重复的元素序列
# add()	为集合添加元素
# clear()	移除集合中的所有元素
# copy()	拷贝一个集合
# discard()	删除集合中指定的元素,该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
# pop()	随机移除元素
# update(1,2,3)	给集合添加多个元素

