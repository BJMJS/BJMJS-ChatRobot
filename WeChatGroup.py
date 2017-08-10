# conding:utf-8
"""
Function:itchat tuling chatrobot
Author:Evan
"""
import itchat
import requests

KEY = "5826c2f85c344d33906939a89854704c"
UID = "TestRobot"

def get_reply(msg):
    api_tuling='http://www.tuling123.com/openapi/api'
    data = {
    'key':KEY,
    'info':msg,
    'userid':UID,
    }
    ret = requests.post(api_tuling, data=data).json()
    return ret.get('text')

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        defaultmsg=msg['Text']
        return get_reply(defaultmsg)

itchat.auto_login(hotReload=True)
itchat.run()
