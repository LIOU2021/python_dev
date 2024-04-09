# 将__version__.py的档案载入，变成其他地方呼叫module1时就能直接call .__version__
from .__version__ import (
    __author__,
    __author_email__,
    __build__,
    __cake__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)

# 定义一个常量
PI = 3.14159

# 定义一个函数
def square_area(side_length):
    return side_length ** 2