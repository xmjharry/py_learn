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
