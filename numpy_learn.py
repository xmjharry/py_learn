import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'\d+/\d+/\d+')
ret = datepat.finditer(text)
for item in ret:
    print(item.group(0))

_list = []
for i in range(3):
    def func(i):
        def f_closure(a):
            return i + a

        return f_closure


    _list.append(func(i))

for f in _list:
    print(f(1))


# _list = []
# for i in range(3):
#     def func():
#         return i + 1
#     func.__doc__ = i
#     func.__hash__ = i
#     func.__repr__ = i
#     func.__defaults__ = tuple([i])  # 这个属性必须是tuple类型
#     func.__name__ = f'{i}'
#     func.hello = i  # 自定义一个属性并赋值
#     # 不能再玩了
#     _list.append(func)
#
# for f in _list:
#     print(f.__doc__,
#           f.__hash__,
#           f.__repr__,
#           f.__defaults__,
#           f.__name__,
#           f.hello,
#           f(),
#           )

def who(name):
    def do(what):
        print(name, 'say:', what)

    return do


spurs = {"Guard": "Parker", "Forward": "Duncan"}


def show_players():
    print(f"{'Position':^10}{'Name':^10}")
    for player in spurs:
        print(f"{player:^10}{spurs[player]:^10}")


show_players()
print(f'His name is {"Tom"}')

import logging


def log_header(logger_name):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(name)s] %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(logger_name)

    def _logging(something, level):
        if level == 'debug':
            logger.debug(something)
        elif level == 'warning':
            logger.warning(something)
        elif level == 'error':
            logger.error(something)
        else:
            raise Exception("I dont know what you want to do?")

    return _logging


project_1_logging = log_header('project_1')

project_2_logging = log_header('project_2')


def project_1():
    # do something
    project_1_logging('this is a debug info', 'debug')
    # do something
    project_1_logging('this is a warning info', 'warning')
    # do something
    project_1_logging('this is a error info', 'error')


def project_2():
    # do something
    project_2_logging('this is a debug info', 'debug')
    # do something
    project_2_logging('this is a warning info', 'warning')
    # do something
    project_2_logging('this is a critical info', 'error')


project_1()
project_2()


def foo():
    a = 1

    def bar():
        nonlocal a
        a = a + 1
        return a

    return bar


ret = foo()
print(ret())

pattern = re.compile(r'(true|false)python')
ret = pattern.finditer('truepythonfdsfsdfalsepythonsdsdspython')
for item in ret:
    print(item.group(0))
    print(item.group(1))
import unicodedata
import sys

print(sys.maxunicode)
print(chr(1))
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
s = '{name} has {n} messages.'
print(sys._getframe().f_locals)
import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
print(scanner.match())
