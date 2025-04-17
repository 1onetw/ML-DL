# 函数
## 参数传递
"""
python 函数的参数传递：

不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""

## 参数
# 必需参数：调用函数时必须传入的参数，顺序必须与函数定义时的顺序一致。
# 默认参数：函数定义时可以给参数设置默认值，调用函数时可以不传入该参数。默认参数必须放在必需参数的后面。
# 可变参数：可以传入任意数量的参数，函数定义时使用 *args 来接收。接收的参数会被封装成一个元组。
# 可变关键字参数：函数定义时使用 **kwargs 来接收。接收的参数会被封装成一个字典。
# 关键字参数：调用函数时传入的参数名必须与函数定义时的参数名一致。

## 匿名函数
# lambda [arg1 [,arg2,.....argn]]:expression
x = lambda a : a + 10
print(x(5))

# map()函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

# filter()函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]

# 使用 reduce() 和 lambda 函数计算乘积
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出：120


