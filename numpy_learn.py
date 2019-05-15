import os
from collections import Iterable

import PIL.Image as Image
import numpy as np

resource_dir = os.path.join(os.path.dirname(__file__), "resource")
image = Image.open(os.path.join(resource_dir, "wechat.jpg"))
alice_coloring = np.array(image)
