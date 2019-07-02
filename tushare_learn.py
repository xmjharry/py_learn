import tushare as ts
from matplotlib import pyplot as plt
import numpy as np

TOKEN = '04beaad46e3ff10b1970c6c3c8d729e87cf7d92ecb86f2c9d1574b4a'
ts.set_token(TOKEN)
pro = ts.pro_api()
df = pro.daily(ts_code='002463.SZ', start_date='20190101', end_date='20190529')
df.to_json('./rec_tmp/stock.json',orient='records')
df = df.iloc[::-1, :]
df.to_excel('./rec_tmp/stock.xlsx')
print(df.close)
with open('./rec_tmp/stock.txt', mode='w', encoding='utf-8') as f:
    f.write(str(df))

