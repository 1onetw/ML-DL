# 控制结构
## match case
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401|403|404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))

## while else
i=0
while i<10:
    print(i)
    i+=1
else:
    print("done")
    
## for else
for i in range(10):
    print(i)
else:
    print("done")

## end关键字：可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

## python推导式
### 列表推导式
# [表达式 for 变量 in 列表] 
# [表达式 for 变量 in 列表 if 条件]

### 字典推导式
# { key_expr: value_expr for value in collection }
# { key_expr: value_expr for value in collection if condition }

### 集合推导式
# { expression for item in Sequence }、
# { expression for item in Sequence if conditional }

### 元组推导式（生成器表达式）
# 元组推导式可以利用 range 区间，快速生成一个满足指定需求的元组。
# { expression for item in Sequence }、
# { expression for item in Sequence if conditional }
print("元组推导式：", range(12)) 

a = (x for x in range(1,10))
# a <generator object <genexpr> at 0x7faf6ee20a50>  # 返回的是生成器对象
tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
# (1, 2, 3, 4, 5, 6, 7, 8, 9)

## 迭代器和生成器
### 迭代器
# 迭代器是一个对象，它实现了迭代协议，包括 __iter__() 和 __next__() 方法。
# StopIteration 异常用于指示迭代器的结束。
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素

### 生成器
# 使用了 yield 的函数被称为生成器（generator）
# 可以在迭代过程中逐步产生值，而不是一次性返回所有结果,更简单点理解生成器就是一个迭代器。
def countdown(n):
    while n > 0:
        yield n
        n -= 1
 
# 创建生成器对象
generator = countdown(5)
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
