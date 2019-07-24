import pandas as pd
import tushare as ts

ts.set_token('04beaad46e3ff10b1970c6c3c8d729e87cf7d92ecb86f2c9d1574b4a')
# df = ts.pro_bar(ts_code='000001.SH', freq='30min', start_date='20190711', end_date='20190718')
df = ts.top_list()
df.to_excel('dp.xlsx')
