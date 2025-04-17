# 1.模块
'''
介绍：
    模块即 .py文件
功能：
    代码复用：将常用的功能封装到模块中，可以在多个程序中重复使用。

    命名空间管理：模块可以避免命名冲突，不同模块中的同名函数或变量不会互相干扰。

    代码组织：将代码按功能划分到不同的模块中，使程序结构更清晰。

导入：
    import ...
    from ... import ...
    as ...
'''
import sys
sys.path # 查看模块搜索路径

## __name__、__main__
'''
一个模块被另一个程序第一次引入时，其主程序将运行。

如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。

说明：每个模块都有一个 __name__ 属性。

    如果模块是被直接运行，__name__ 的值为 __main__，__main__是当前主模块的名称

    如果模块是被导入的，__name__ 的值为模块名。
'''

## dir()函数: 查看模块中的所有定义名称，没有给定参数时，返回当前模块的定义名称列表

## 标准模块：math、os、sys、time、datetime、random、re、json、pickle、collections（提供额外的数据结构）、functools（高阶函数工具）、threading、multiprocessing

# 2.包：一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# import sound.effects.echo
# from sound.effects import echo

## __init__.py、__all__：
# __init__.py：标识一个目录是一个包，可以是空文件，也可以包含包的初始化代码。
# __all__：定义了在使用 from package import * 时，哪些模块会被导入。它是一个列表，包含要导入的模块名称。




