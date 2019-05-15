import os
import re

import PIL.Image as Image
import itchat
import jieba
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator

itchat.auto_login(True)
friends = itchat.get_friends(update=True)[0:]
tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile(r"1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)
# 拼接字符串
text = "".join(tList)
wordlist_jieba = jieba.cut(text)
wl_space_split = " ".join(wordlist_jieba)
resource_dir = os.path.join(os.path.dirname(__file__), "resource")
tmp_dir = os.path.join(os.path.dirname(__file__), "rec_tmp")
alice_coloring = np.array(Image.open(os.path.join(resource_dir, "wechat.jpg")))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path=os.path.join(resource_dir, './SimHei.ttf')).generate(wl_space_split)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 保存图片 并发送到手机
# my_wordcloud.to_file(os.path.join(tmp_dir, "wechat_cloud.png"))
# itchat.send_image(os.path.join(tmp_dir, "wechat_cloud.png"), 'filehelper')
