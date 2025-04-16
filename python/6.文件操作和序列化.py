# 1.文件操作
'''
with open(file, mode='r', encoding=None) as f:

mode:
    t
    b
    r
    +：可读可写
    r+
    rb
    rb+
    w
    w+
    wb
    wb+
    a
    a+
    ab
    ab+
默认为t（文本模式）

常用函数：	
file.close()
	
file.read([size]) 从文件读取指定的字节数，如果未给定或为负则读取所有。

file.readline([size]) 读取整行，包括 "\n" 字符。

file.readlines() 读取所有行并返回列表

file.seek(offset[, whence]) 移动文件读取指针到指定位置

file.tell() 返回文件当前位置。

file.write(str) 将字符串写入文件，返回的是写入的字符长度。

file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''

# 2.序列化
'''
## 序列化与反序列化：

**比特：**01100110 01100110 ，一位是一个bit（b）

**字节：**8个比特位是一个字节Byte（B）

1 KB = 1024（2的十次方）B

1 MB = 1024KB = 2的20次方 B 

1 GB = 1024MB

1TB = 1024GB

1PB = 1024TB

## 概念：

​		序列化：把对象转化为可传输的字节序列的过程称为序列化

​		反序列化：把字节序列还原为对象的过程称为反序列化

### 作用：

1. 方便数据存储：解决一对多问题，不用序列化可能需要存储多条信息，而序列化可以将多条信息合并成一条进行存储
2. 方便网络传输：将复杂的数据结构转化成字符串
3. 方便协议解释：序就是有序的意思，有序的字符串可以提供给大多数编程语言使用

## python中序列化模块pickle , json:

### 区别：

​			json可以在不同语言之间交换数据，而pickle只能在python之间使用

​			json只能序列化最基本的数据类型，而pickle可以序列化所有的数据类型，包括类，函数等等

### pickle：

```python
语法：
pickle.dumps(obj)#把任意对象序列化成一个字节序列
pickle.dump(obj，fp)#序列化到文件对象中
pickle.loads(obj)#反序列化
pickle.load(fp)#从文件对象中反序列化
```

```python
#  序列化：
# import pickle
# d = [1,2,3]
# print(pickle.dumps(d))
# 将序列化的字节序列内容保存到文件中去：
#  with open('./pickle.data',mode='wb') as fp:
#      pickle.dump(d,fp)
#  将文件中的字节序列内容反序列化：
#  with open('./pickle.data',mode='rb') as fp1:
#      print(pickle.load(fp1))
# 将字节序列反序列化：
# print(pickle.loads(bytes_d))
```

### json：

json模块用来对json数据进行编码

dump和dumps将一个python对象进行json格式的编码

```
语法：
json.dump(obj,fp,ensure_ascii=True)
obj:表示要序列化的对象
fp：文件描述符
ensure_ascii：可以将输入的非ascii字符转义输出，如果为ascii字符则为True，就按ascii字符输出，如果不为ascii字符则为Flase，该字符将进行转义输出，也就是原样输出
dumps函数不需要文件描述符，其他的和dump一样
```

```python
import json
d = {'key2':'v2','key3':'v3','key1':'v1'}
print(type(d))
#默认转换的json格式的数据是无序的
json1 = json.dumps(d,sort_keys=True)#sort_keys = True 对数据进行排序
print(type(json1))
print(json1)
# 将对象序列化，转化为json数据并写入文件中：
import json
d = {'key2':'v2','key3':'v3','key1':'v1'}
with open('./json.data',mode='w',encoding = 'utf-8') as fp:
    json.dump(d, fp)
   
```

load和loads，将json格式的数据解码为python对象

```python
语法:
json.load(fp)#将文件中json格式的数据进行解码，并写入文件中
json.loads(obj)#将json格式的数据进行解码，
```

### json格式转化表：

json中的数据格式和python中的数据格式转换

|             json类型             | python类型 |
| :------------------------------: | :--------: |
| {}其实也是字符串，只不过这样显示 |    dict    |
| []其实也是字符串，只不过这样显示 |    list    |
|             'string'             |    str     |
|              12/1.5              | int/float  |
|            true/false            | True/False |
|               null               |    None    |


'''