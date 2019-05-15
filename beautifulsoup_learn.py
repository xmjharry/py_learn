import collections
import os
import PIL.Image as Image
import jieba
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, ImageColorGenerator

sid = 20495023


def get_data():
    start = 0
    limit = 20
    tag_list = list()
    while True:
        url = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=%s&sort=new_score&status=P' % (
            sid, start, limit)
        content = requests.get(url).content
        soup = BeautifulSoup(content)
        paginator = soup.select('div#paginator')
        if paginator:
            start = start + limit
            tag_list.extend(soup.select('span.short'))
        else:
            break
    return tag_list


if __name__ == '__main__':
    tag_list = get_data()
    data = [tag.string for tag in tag_list]
    content = ''.join(data)
    content = jieba.cut(content)
    content = collections.Counter(content)
    content = list(content.items())
    content.sort(key=lambda item: item[1], reverse=True)
    # content = filter(lambda item: item[1] > 1, content)
    content = [key for key, value in content if len(key.strip()) > 1]
    content = ' '.join(content)
    resource_dir = os.path.join(os.path.dirname(__file__), "resource")
    tmp_dir = os.path.join(os.path.dirname(__file__), "rec_tmp")
    alice_coloring = np.array(Image.open(os.path.join(resource_dir, "wechat.jpg")))
    my_wordcloud = WordCloud(background_color='white', max_words=2000, mask=alice_coloring,
                             max_font_size=40, random_state=42,
                             font_path=os.path.join(resource_dir, './SimHei.ttf')).generate(content)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
