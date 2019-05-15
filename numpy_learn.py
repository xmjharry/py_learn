import os
from collections import Iterable
from random import choice

import PIL.Image as Image
import numpy as np


# resource_dir = os.path.join(os.path.dirname(__file__), "resource")
# image = Image.open(os.path.join(resource_dir, "wechat.jpg"))
# alice_coloring = np.array(image)


class StrBig(str):
    def __iter__(self, *args, **kwargs):
        print('__iter__')
        return str.__iter__(self, *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        print('__getitem__')
        return str.__getitem__(self,*args, **kwargs)

iter()
for c in StrBig('ABCD'):
    print(c)
