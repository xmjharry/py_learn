from bs4 import BeautifulSoup
import requests
import sqlite3
import os
import json
import collections
import re
import bs4

headers = {
    'cookie': 'ff_supports_webp=1; ff_supports_animateWebP=1; _zap=edb3ceb2-ac82-46ff-b08b-b822934be698; _xsrf=uXylySoC94Ka9SN36WtBrSd12c4XWE0w; d_c0="ABDhyKJUxg6PTkALaeRNoPIviWx9ROso4qo=|1546607910"; z_c0="2|1:0|10:1546607935|4:z_c0|92:Mi4xc2JNSUFBQUFBQUFBRU9ISW9sVEdEaVlBQUFCZ0FsVk5QNnNjWFFDdGxLZVZ6OXFjNUVNNmlPM1dTTUVmcUk3UzZR|514c1b52fde8a5a12af3cab07c9486e18c80dd1254b341e0c2b3abd8fd8d5ea9"; tst=r; __utma=51854390.760980014.1551881890.1551881890.1551881890.1; __utmz=51854390.1551881890.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20130307=1^3=entry_date=20130307=1; q_c1=864c5e634b08492f98cd5a20ddc5fdff|1557541770000|1547049087000',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}

table_name = 'mate'
db_dir = os.path.join(os.path.dirname(__file__), "rec_tmp")
db_path = os.path.join(db_dir, "zhihu_scrapy.db")
limit = 20
contene_list = list()
maxlen = 60

Answer = collections.namedtuple('Answer',
                                'ask_id answer_id content zhihu_user_id_encryption url_token name avatar_url gender')


def fetch_answer_list(ask_id: int):
    page = 1
    while True:
        if len(contene_list) >= maxlen:
            insert_dat()
            break
        offset = (page - 1) * limit
        url = f'''https://api.zhihu.com/v4/questions/{ask_id}/answers?limit=
                    {limit}&offset={offset}&reverse_order=0&show_detail=1'''
        content = requests.get(url, headers=headers).content
        content = json.loads(content)
        data = content['data']
        if len(data) > 0:
            for item in data:
                fetch_answer_content(ask_id, item['id'])
        else:
            break
        page = page + 1


tag_content = ''
user = re.compile(r'"user":{.*?,"isPrivacy":.+?,')


def fetch_answer_content(ask_id: int, answer_id: int):
    url = f'https://www.zhihu.com/appview/v2/answer/{answer_id}'
    content = requests.get(url, headers=headers).content

    userinfo = user.findall(str(content, encoding='utf-8'))
    if re.findall(r'"name":"匿名用户"', str(content, encoding='utf-8')):
        userinfo = json.loads('{' + userinfo[0][:len(userinfo[0]) - 1] + '}')
    else:
        userinfo = json.loads('{' + userinfo[0][:len(userinfo[0]) - 1] + '}}}')
    user_json = userinfo['user']
    key = list(user_json.keys())[0]
    userinfo = user_json[key]

    zhihu_user_id_encryption = userinfo['id']
    url_token = userinfo['urlToken']
    name = userinfo['name']
    avatar_url = userinfo['avatarUrl']
    gender = userinfo['gender']

    soup = BeautifulSoup(content)
    paginator = soup.find('div', class_=re.compile(r'RichText ztext AnswerPage-richText.*'))
    global tag_content
    tag_content = ''
    iteration_fetch_tag_content(paginator)
    contene_list.append(
        Answer(ask_id, answer_id, tag_content, zhihu_user_id_encryption, url_token, name, avatar_url, gender))


def iteration_fetch_tag_content(father_tag):
    global tag_content
    if isinstance(father_tag, bs4.element.Tag):
        if father_tag.name == 'figure':
            for tag in father_tag.contents:
                if tag.name == 'img':
                    src = tag['data-actualsrc']
                    tag_content += f'<image src="{src}"/></br>'
        elif father_tag.name == 'a' and father_tag.get('target') == '_blank':
            href = father_tag['href']
            tag_content += f'<p><a href="{href}">linkCard</a><p/></br>'
        elif len(father_tag.contents) > 0:
            for tag in father_tag.children:
                iteration_fetch_tag_content(tag)
        else:
            pass
    elif isinstance(father_tag, bs4.element.NavigableString):
        tag_content += f'<p>{father_tag}<p/></br>'
    else:
        pass


def insert_dat():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for answer in contene_list:
        cursor.execute(
            '''insert into %s (ask_id,answer_id,content,zhihu_user_id_encryption, url_token, name, avatar_url, gender) values (?,?,?,?,?,?,?,?)''' % table_name,
            (answer.ask_id, answer.answer_id, answer.content, answer.zhihu_user_id_encryption, answer.url_token,
             answer.name, answer.avatar_url, answer.gender))
    cursor.close()
    conn.commit()
    conn.close()


def create_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_tb_cmd = '''CREATE TABLE IF NOT EXISTS %s
           (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           ask_id INT,
           answer_id INT,
           zhihu_user_id_encryption VARYING(50),
           url_token VARYING(50),
           name VARYING(50),
           avatar_url TEXT,
           gender INT,
           content TEXT
           );''' % table_name
    cursor.execute(create_tb_cmd)
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    ask_id = 275359100
    create_db()
    fetch_answer_list(ask_id)
    # fetch_answer_content(ask_id, 546675004)
