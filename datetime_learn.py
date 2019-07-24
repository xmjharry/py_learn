import functools
import logging
import time
from datetime import datetime
from functools import wraps, partial

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# ax = plt.subplot(111)
#
# rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
# pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
#                    color='g', alpha=0.5)
#
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)
# plt.savefig('figpath.svg')
# exit(0)

sum_1 = functools.partial(np.sum, axis=0, dtype=float)

# data = [1, 2, 2, 3, 3, 4, 5, 6, 7]
# print(sum_1(data))
# exit(0)

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9],
                   "F": ["Q", "W", "E", "R",
                         "Q", "W", "E", "R",
                         "Q"],
                   })

table = df.pivot_table(values=['D', 'E'], index=['A', 'B'], columns=['C'],
                       aggfunc={'D': sum_1, 'E': [np.min, np.max, np.mean]},
                       fill_value=0)
print(table)
data = table.xs(('D', 'sum', 'large'), axis=1)
print(data)
exit(0)

# df = pd.DataFrame({'key1': list('aabba'),
#                    'key2': ['one', 'two', 'one', 'two', 'one'],
#                    'data1': np.random.randn(5),
#                    'data2': np.random.randn(5)})

df = pd.DataFrame({'data1': np.random.randint(1, 5, 5),
                   'data2': np.random.randint(1, 5, 5),
                   'data3': np.random.randint(1, 5, 5),
                   'data4': np.random.randint(1, 5, 5),
                   'data5': np.random.randint(1, 5, 5)})

pd.crosstab()
print(df)
divisor = df.sum(0).astype(float)
print(divisor)
print(df.div(divisor, axis=1))

exit(0)
grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states, years]).mean())
exit(0)

m_index3 = pd.MultiIndex.from_arrays([["A", 'A', "B", "B", "B", 'C'], ['x1', 'y1', 'x1', 'y1', 'y3', 'y1']],
                                     names=["class1", "class2"])
print(m_index3)
# m_index3 = pd.MultiIndex.from_product([["A", "B"], ['x1', 'y1', 'y3']], names=["class1", "class2"])
# print(m_index3)
df3 = pd.DataFrame(np.random.randint(1, 10, (2, 6)), columns=m_index3)
# df3.set_index(['A', 'B'])
print(df3)

exit(0)

df = pd.DataFrame(dict(city=['nanjing', 'beijing', 'shanghai', 'nanjing', 'wuxi', 'beijing', 'shengzheng', 'nanjing'],
                       provice=['JS', 'BJ', 'SH', 'JS', 'JS', 'BJ', 'GD', 'JS']))
print(df)
print(df.groupby('provice').size())
exit(0)

df1 = pd.DataFrame(np.arange(12).reshape(4, 3), index=[list("AABB"), [1, 2, 1, 2]], columns=[list("XXY"), [10, 11, 10]])
print(df1)
exit(0)

date_index = pd.date_range('1/1/2010', periods=6, freq='D')
df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]}, index=date_index)

print(df2)
date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
data = df2.reindex(date_index2, method='bfill')
# data = data.fillna(method='ffill')
print(data)

exit(0)

data = pd.DataFrame(np.random.normal(60, 1, (20, 5)), columns=list('AXEZV'),
                    index=pd.date_range('2019-06-25', periods=20, freq='2h20min'))
grouped = data.sort_index(axis=1)
print(grouped)

renameData = data.rename(dict(A='name', V='price'), axis=1)
print(renameData)

data.pivot

# data['A'] = [20190615, 20190616, 20190617, 20190618, 20190719]
# data['A'] = pd.to_datetime(data['A'], format='%Y%m%d')
# data['A'].name = '日期'
# data.set_index(data['A'], inplace=True)
data = data.A.resample('W-MON', closed='left', label='left').ohlc()
print(data)
exit(0)


def alertPoint(point):
    print('point is ', point)
    return 1.5 * point


image = Image.open(r'D:\Documents\Pictures\timg.jpg')
im_point = image.point(alertPoint)
im_point.show()

data = np.array(image)
print(data)
print('shape is ', data.shape)

image = image.convert("L")
data = np.array(image)
print(data)
print('shape is ', data.shape)
exit(0)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),  # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=50),
            ha='left',
            va='bottom',
            )
plt.show()
exit(0)

name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
num_list = [1.5, 0.6, 7.8, 6]
num_list1 = [1, 2, 3, 1]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n

plt.bar(x, num_list, width=width, label='boy', fc='y', align='edge')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='girl', tick_label=name_list, fc='r', align='edge')
plt.legend()
plt.show()

exit(0)

logging.basicConfig(level=logging.DEBUG)

data = np.random.binomial(9, 0.1, 10)
print(data)
print(np.sum(data))

print(datetime.now().strftime('%F'))

data = pd.DataFrame(np.random.normal(60, 1, (5, 5)), columns=list('ABCDE'))
data['A'] = [20190615, 20190616, 20190617, 20190618, 20190719]
data['A'] = pd.to_datetime(data['A'], format='%Y%m%d')
data['A'].name = '日期'
data.set_index(data['A'], inplace=True)
print(data['2019-06'])


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('instance', instance)
        if instance is None:
            print(111)
            return self
        else:
            print(222)
            return '测试数据'
            # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = Integer('z')


p = Point(3, 2)
print('x=', p.x)
print('y=', p.y)
print('z=', p.z)


# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        log.debug('This is a customer debug message')

        @wraps(func)
        def wrapper(*args, **kwargs):
            print('level', level, time.time())
            log.log(level, logmsg + str(time.time()))
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


# Example use
@logged(logging.ERROR)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


add(2, 3)
# logged(logging.ERROR)(add)(2,3)=decorate(add)(2,3)=wrapper(2,3)
add.set_message('Add called')
add(2, 3)

from inspect import signature
import logging


class MatchSignaturesMeta(type):

    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        print('sup is ', sup)
        print('self is ', self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)


# Example
class Root(metaclass=MatchSignaturesMeta):
    pass


# class A(Root):
#     def foo(self, x, y):
#         pass
#
#     def spam(self, x, *, z):
#         pass
#
#
# # Class with redefined methods, but slightly different signatures
# class B(A):
#     def foo(self, a, b):
#         pass
#
#     def spam(self, x, z):
#         pass
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3


b = B()
b.add(2)
print(b.n)
