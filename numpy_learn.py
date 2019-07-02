import os
from collections import Iterable
from random import choice

import PIL.Image as Image
import numpy as np
import collections
from _collections_abc import __all__

# resource_dir = os.path.join(os.path.dirname(__file__), "resource")
# image = Image.open(os.path.join(resource_dir, "wechat.jpg"))
# alice_coloring = np.array(image)

from abc import abstractmethod
import abc


class StrBig:
    @abstractmethod
    def test(self):
        pass

    def __iter__(self, *args, **kwargs):
        print('__iter__')
        return str.__iter__(self, *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        print('__getitem__')
        return str.__getitem__(self, *args, **kwargs)


class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

    def __init__(cls, value):
        return super(PositiveInteger, cls).__init__(abs(value))

    def __len__(self):
        return False

from array import  array
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

print(sorted(rows,key=lambda item:item['fname']))

# print( id(t))
# print(t_2)
# print(id(t_2))


print(len('的'))