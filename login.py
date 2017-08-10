# conding:utf-8
"""
Function:itchat tuling chatrobot
Author:Evan
"""
import itchat,time
import requests
KEY = "5826c2f85c344d33906939a89854704c"
UID = "TestRobot"
"""
msg = ""
ret = requests.post(api_tuling,data=data).json()
print(ret.get('text'))
"""
def get_reply(msg):
	api_tuling = 'http://www.tuling123.com/openapi/api'
	data = {
	'key':KEY,
	'info':msg,
	'userid':UID,
	}
	ret = requests.post(api_tuling,data).json()
	return ret.get('text')


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    fileDir = '%s%s'%(msg['Type'], int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received'%msg['Type'], msg['FromUserName'])
    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.get_contract()
    itchat.send_msg('Nice to meet you!I am a chatrobot', msg['RecommendInfo']['UserName'])

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])
"""
return get_reply(defaultmsg)
"""

@itchat.msg_register('Text')
def text_reply(msg):
	defaultmsg = msg['Text']
	reply = get_reply(defaultmsg)
	if msg['Text'] == "Jesus":
	return 'For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.He is the way, and the truth, and the life. No one comes to the Father except through me.'
	else 
	return reply
"""
	itchat.send('Content',toUserName=%UserName)
	print(itchat.get_friends()[Num])
	nickname = itchat.get_friends()[Num]["NickName"]
	username = itchat.get_friends()[Num]["UserName"]
	itchat.search_friends(name="%UserName")
"""
itchat.auto_login(hotReload=True)
itchat.run()
