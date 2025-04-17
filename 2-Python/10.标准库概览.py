# 1.os
import os

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)

# 在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:

# 2.shutil：针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

# 3.glob：用于从目录通配符搜索中生成文件列表
import glob
glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']

# 4.sys
## 命令行参数
import sys
print(sys.argv)
['demo.py', 'one', 'two', 'three']

## 大多脚本的定向终止
sys.exit(0)

# 5.datetime: 用于处理日期和时间
import datetime

#获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45

## 6.数据压缩：zlib，gzip，bz2，zipfile，以及 tarfile
import zlib
s = b'witch which has which witches wrist watch'
len(s)
# 41
t = zlib.compress(s)
len(t)
# 37
zlib.decompress(t)
b'witch which has which witches wrist watch'
zlib.crc32(s) # CRC32校验
# 226805979