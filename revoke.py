import os
import re
import sqlite3
import time

import itchat
import requests
from itchat.content import *

# 定义一个字典，保存消息的信息。
msg_dict = {}

# 创建一个目录，用于存放消息临时文件。
rec_tmp_dir = r'./rec_tmp/'
if not os.path.exists(rec_tmp_dir):
    os.mkdir(rec_tmp_dir)

face_bug = None
table_name = 'chat_history'
tmp_dir = os.path.join(os.path.dirname(__file__), "rec_tmp")
db_name = os.path.join(tmp_dir, 'wechat.db')


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True,
                     isGroupChat=False, isMpChat=False)
def handler_receive_msg(msg):
    """
    注册消息接收器
    """
    global face_bug
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    msg_id = msg['MsgId']
    msg_time = msg['CreateTime']
    msg_from = (itchat.search_friends(userName=msg['FromUserName']))['NickName']
    msg_content = None
    msg_share_url = None

    if msg['Type'] in [TEXT, FRIENDS]:
        msg_content = msg['Text']
    elif msg['Type'] in [RECORDING, ATTACHMENT, VIDEO, PICTURE]:
        msg_content = msg['FileName']
        msg['Text'](rec_tmp_dir + msg['FileName'])
    elif msg['Type'] == CARD:
        msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"
    elif msg['Type'] == MAP:
        x, y, location = re.search(r'<location x="(.*?)" y="(.*?)".*label= "(.*?)".*', msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()
        else:
            msg_content = location
    elif msg['Type'] == SHARING:
        msg_content = msg['Text']
        msg_share_url = msg['Url']
    face_bug = msg_content

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        '''insert into %s (msg_id,user_name,nick_name,type,status,
            create_time,text,content) values (?,?,?,?,?,?,?,?)''' % table_name,
        (msg_id, msg['FromUserName'], msg_from, msg['Type'], msg['Status'],
         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg_time)), msg_content, msg['Content']))
    cursor.close()
    conn.commit()
    conn.close()

    msg_dict.update({
        msg_id: {
            "msg_from": msg_from, "msg_time": msg_time,
            "msg_time_rec": msg_time_rec, "msg_type": msg["Type"],
            "msg_content": msg_content, "msg_share_url": msg_share_url
        }
    })

    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        if msg['Type'] in [RECORDING, ATTACHMENT, VIDEO, PICTURE]:
            msg['Text'](rec_tmp_dir + msg['FileName'])
            return '@fil@%s' % (rec_tmp_dir + msg['FileName'])
        else:
            json = {
                'reqType': 0,
                'perception': {
                    'inputText': {
                        'text': msg.Text
                    }
                },
                'userInfo': {
                    'apiKey': 'dc9244f1a958457d9ae3c9f0379de4e2',
                    'userId': '1',
                }
            }
            r = requests.post('http://openapi.tuling123.com/openapi/api/v2', json=json)
            data = r.json()
            return '%s（%s）' % (data['results'][0]['values']['text'], 'Octopus')


@itchat.msg_register([NOTE])
def send_msg_helper(msg):
    """
    注册撤回
    """
    global face_bug
    if re.search(r'<replacemsg><!\[CDATA\[.*? 撤回了一条消息\]\]></replacemsg>', msg['Content']) is not None:
        old_msg_id = re.search(r'<msgid>(.*?)</msgid>', msg['Content']).group(1)
        old_msg = msg_dict.get(old_msg_id, {})
        if len(old_msg_id) < 11:
            itchat.send_file(rec_tmp_dir + face_bug, toUserName='filehelper')
            os.remove(rec_tmp_dir + face_bug)
        else:
            msg_body = old_msg.get('msg_time_rec') + "\n" + old_msg.get('msg_from') + " 撤回了 " \
                       + old_msg.get('msg_type') + " 消息\n" + old_msg.get('msg_content')
            if old_msg['msg_type'] == SHARING:
                msg_body += "\n就是这个连接->" + old_msg.get('msg_share_url')
            itchat.send(msg_body, toUserName='filehelper')
            if old_msg["msg_type"] in [PICTURE, RECORDING, VIDEO, ATTACHMENT]:
                # file = '@fil@%s' % (rec_tmp_dir + old_msg['msg_content'])
                # itchat.send(msg=file, toUserName='filehelper')
                itchat.send_file(rec_tmp_dir + face_bug, toUserName='filehelper')
                os.remove(rec_tmp_dir + old_msg['msg_content'])
            msg_dict.pop(old_msg_id)


def create_table():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    create_tb_cmd = '''CREATE TABLE IF NOT EXISTS %s
       (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       msg_id VARCHAR(50),
       user_name VARCHAR(50),
       nick_name VARCHAR(50),
       type VARCHAR(50),
       status INT,
       create_time TIMESTAMP,
       text TEXT,
       content TEXT
       );''' % table_name
    cursor.execute(create_tb_cmd)
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    itchat.auto_login(True)
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]['UserName']
    itchat.run(True)
