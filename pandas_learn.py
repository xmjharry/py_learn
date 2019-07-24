import os

path = r'C:\Users\Administrator\Desktop\image'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, str(count) + ".jpg"))
    count += 1




# header = ['a', 'b', 'c']
# values = [[1, 2, 3], [1, 2, 3]]
# print(list(zip(header, zip(*values))))
# data_dict = {h: v for h, v in zip(header, zip(*values))}
# print(data_dict)

# result = pd.read_csv('examples/ex5.csv')
# sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
# result = pd.read_csv('examples/ex5.csv', na_values=sentinels)
# print(result)

# dates = pd.date_range('20130101', periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# df.apply()
# df.index.name = 'date'
# df.columns.name = 'state'
# index = df.index
# print(df)
# print(index)
# print(index.is_unique)
# df = df.reindex(columns=list('AXCD'))
# df = df.drop(columns=list('X'))
# print(df)
# df.index = np.arange(1, 7)
# df.columns = np.arange(1, 4)
# print(df)
# frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# series = frame.iloc[0]
# frame = frame.sub(series, axis=1)
# print(frame)

# ser = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
# print(ser.iloc[:1])
# print(ser.loc['a':'b'])

# count = df['A'].value_counts()
# count[::].plot(kind='barh', rot=0)
#
# # with open(os.path.join(os.path.dirname(__file__), 'resource', 'house.txt'), encoding='utf-8') as f:
# #     content = f.read()
# content = json.load(open(os.path.join(os.path.dirname(__file__), 'resource', 'house.txt'), encoding='utf-8'))
# frame = pd.DataFrame(content)
# frame = frame[frame.id == 1]
# # frame = np.where(frame.community.str.contains('San'), 'Xuki', 2)
#
# arr = np.empty((4, 4))
# print(arr)
# d = arr[1:3, 1]
# print(d)
# print(arr.transpose)

# points = np.arange(-5, 5, 1)  # 1000 equally spaced points
# xs, ys = np.meshgrid(points, points)
# z = np.sqrt(xs ** 2 + ys ** 2)
# plt.imshow(z, cmap=plt.cm.gray)
# plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#
# X = np.array([[0, 1, 2],
#               [2, 1, 0]])
# print(X)
# a = np.cov(X)
# np.random.normal()
# print(a)
#
# s = np.random.normal(loc=0, scale=1, size=100)
# print(s)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.dates as dates

fig, axes = plt.subplots(2, 2)

print(axes.flatten())
print(type(axes))
print(fig)




exit(0)

print(id(plt.gcf()))
print(id(plt.gca()))

fig, axes = plt.subplots()

plt.figure()

print(id(plt.gcf()))
print(id(plt.gca()))

print(id(fig))
print(id(axes))

exit(0)

frame = pd.read_excel('./rec_tmp/frame.xls')

pd.qcut()
plt.plot(frame.trade_date, frame.close, label='close')
plt.plot(frame.trade_date, frame.high, label='high', color='y')
plt.plot(frame.trade_date, frame.low, label='high', color='r')

# plt.minorticks_on()
plt.grid(axis='y')

# plt.xticks(['2019-01-01','2019-02-05'], ['New Year','Spring Festival'])
plt.legend()
plt.show()

exit(0)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
frame.trade_date = pd.to_datetime(frame.trade_date, format='%Y%m%d')
print(frame.trade_date.dt.month.value_counts())
frame.set_index('trade_date', inplace=True)
frame_1 = frame['2019-01']
frame_period = frame_1.to_period('A')
frame.plot()

# print(pd.qcut(np.array([1, 7, 5, 4, 6, 3]), 3, False))
# print(type(type))
# plt.show()


import pandas.util.testing as tm

x = np.arange(0, 100, 10)
projection = 'polar'
axes = plt.subplot(221, projection=projection)

# axes.set_xlim((0, 80))
# axes.set_xticks([10, 25, 75])
# axes.set_xticklabels([r'$aaaa$', r'$asasa$', r'$csdaa$'])
# axes.spines['right'].set_color(None)
l1, = axes.plot([0.25 * np.pi] * 10, x, color='green', marker='o', linestyle='dashed', linewidth=1, markersize=8,
                label=r'$%s$' % projection)
axes.legend([l1], ['qwerty'])
axes.text(10, 20, r'$%s$' % projection, color='r', fontsize=18)

axes.annotate('annotate', xy=(0.25 * np.pi, 50), xytext=(20, -20), textcoords='offset points',
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=.2', color='red'),
              bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k', lw=1, alpha=0.4), color='r')

plt.subplot(222)
plt.plot(x, -x)

plt.subplot(223)
plt.plot(x, x ** 2)

plt.subplot(224)
plt.plot(x, np.log(x))

plt.show()

exit(0)

x = np.arange(0, 6)
y = x * x
plt.plot(x, y, marker='o')
for xy in zip(x, y):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
plt.show()

exit(0)

plt.scatter

n = 10

X = np.arange(n)

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, Y1)
plt.bar(X, -Y2)

# plt.xticks(())
# plt.yticks(())

axes = plt.gca()

axes.spines['right'].set_color(None)
axes.spines['top'].set_color(None)
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')

axes.spines['bottom'].set_position(('data', 0))
axes.spines['left'].set_position(('data', -0.4))

for x, y in zip(X, Y1):
    plt.text(x, y + 0.04, f'{y:.2f}', ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.annotate(f'{-y:.2f}', xy=(x, -y - 0.04))

plt.show()

exit(0)

n = 1024

X = np.random.normal(50, 1, n)
Y = np.random.normal(50, 1, n)
# color = np.arctan(X)
color = np.linspace(0, 1, n)
print(color)
plt.scatter(X, Y, s=10, c=color, cmap='plasma')
ret = plt.show()
print('axis is ', plt.gca())

exit(0)

x = np.linspace(-1, 2, 5)
y = 2 * x + 5
line = plt.plot(x, y, color='r')
print('line is', line)
print('line size is', len(line))
plt.annotate

plt.show()

a, *b = (1, 2, 3, 4,)
print('a is ', a)
print('b is ', b)
x = np.array([3, 1, 2])
print(np.argsort(x))

data = pd.DataFrame(
    {'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

data.replace
print(data['food'].str)
from numpy import nan as NA

np.random.gamma()

# df = pd.DataFrame(np.random.randn(6, 3))

# df.iloc[2:, 1] = NA
# df.iloc[4:, 2] = NA
# print(df.fillna(method='bfill'))


# print(frame.resample('M', on='trade_date').sum())
#
# rng = pd.date_range('20180101', periods=12)
# ts = pd.Series(np.arange(1, 13), index=rng)
# ts_5d_leftclosed = ts.resample('5D', closed='right`', label='right').sum()
# print(ts_5d_leftclosed)

# print(frame['2019-01-11':'2019-01-11'])
# print(frame.truncate(before='2019-01', after='2019-01'))
# data = frame[(frame.trade_date >= 20190201) &
#              (frame.trade_date <= 20190231)]
# print(data)


# frame = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=list('cdb'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# frame.to_excel('./rec_tmp/frame.xls', index=False)

# data = frame.loc['Utah', 'd'] vbv
# data = frame['d']
# data = frame.apply(lambda x: x.mean(), axis=0)
# data = frame.applymap(lambda x: x - 1)
#
# data = frame.drop(['b', 'd'], axis=1)
#
# data = frame.sort_index(axis=0)
# data = frame.sort_values(by='Utah', ascending=False, axis=1)
#
# frame = pd.DataFrame({'b': [4.3, 7, -3, 2, 2], 'a': [0, 1, 0, 1, 0], 'c': [-2, 5, 8, -2.5, -2]})
# data = frame.describe()
# print(data)
# data = frame.rank(method='dense')
#
#
#
# print('over')


from collections import abc
from operator import itemgetter
import html
from decimal import localcontext

from sqlalchemy import Column, String, create_engine

from sqlalchemy.ext.declarative import declarative_base


class Desc(object):

    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")
        return 'xuki'

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc()

    def __getattr__(self, item):
        print('__getattr__')
        return 'qwerty'


# 以下为测试代码
t = TestDesc()
print(t.x)
