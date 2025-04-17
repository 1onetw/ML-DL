# 1.错误
'''
运行前检测出来的为错误
'''

# 2.异常
'''
运行时检测出来的为异常

异常处理语句：
    try:
        # 运行代码
    except:
        # 异常处理代码
    else:
        # 没有异常时执行的代码
    finally:
        # 不管有没有异常都会执行的代码

抛出异常：
    raise Exception('错误信息')
    
用户自定义异常：
    class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
    try:
        raise MyError('错误信息')
    except MyError as e:
        print(e.value)
        
'''
# 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message