import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import mpl_finance as mpf
from matplotlib.ticker import Formatter
import numpy as np
from datetime import datetime
from matplotlib.pyplot import MultipleLocator


frame = pd.read_excel('./rec_tmp/frame.xls')
# frame = frame.head(10)
ax = plt.subplot()
ax.set_title('002463')
frame.trade_date = frame.trade_date.apply(lambda x: dates.date2num(x))
data_mat = frame.iloc[:, 1:6]
mpf.candlestick_ohlc(ax, data_mat.as_matrix(), width=0.6, colorup='r', colordown='g',
                     alpha=1.0)


# 将x轴的浮点数格式化成日期小时分钟
# 默认的x轴格式化是日期被dates.date2num之后的浮点数，因为在上面乘以了1440，所以默认是错误的
# 只能自己将浮点数格式化为日期时间分钟
# 参考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%m/%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(np.round(x))
        # ind就是x轴的刻度数值，不是日期的下标

        return dates.num2date(ind).strftime(self.fmt)


formatter = MyFormatter(data_mat.iloc[:, 0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
    # label.set_rotation(90)
    label.set_horizontalalignment('center')

x_major_locator = MultipleLocator(30)
ax.xaxis.set_major_locator(x_major_locator)

plt.show()
