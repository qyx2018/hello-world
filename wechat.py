import itchat
import itchat.content as itcontent

'''
具体实现功能：使用本程序必须先关注微信号xiaoice-ms,这是微软的微信机器人。将别人发送过来的消息转发给AI，再将AI回复消息转回去，
过年自动回复消息，还有更多说不清楚，看下去才能知道，请保持耐心。
'''

# 登录网页微信，hotReload=True 能让登录时间加长
itchat.auto_login(hotReload=True)

# 记录公众号机器人小冰的UserName
mps = itchat.search_mps(name='小冰')
AI = mps[0]['UserName']
# print(AI)

# 记录自己的UserName，不然发送消息会发两遍
username = itchat.get_friends()
user = username[0]['UserName']
# print(username)

# 记录好友列表里好友的 UserName
friendsname = [friend['UserName'] for friend in username if friend['UserName'] != user]
# print(friendsname)

groupname = itchat.get_chatrooms()
groups = [group['UserName'] for group in groupname]

# 这个说来话长~~，有兴趣的可以去上网查查
@itchat.msg_register(itcontent.TEXT,isFriendChat=True,isMpChat=True,isGroupChat=True)
def simple_reply(msg,FriendList=[]):
    
    Fromuser = msg['FromUserName']
    
    # 如果是AI而且列表不为空，就将AI发给自己的消息转发给发送消息者
    if msg['FromUserName'] == AI and FriendList:
        # print(msg['FromUserName'])
        itchat.send(msg['Text'], toUserName=FriendList[-1])
    
    # 私聊消息运行下面程序
    elif Fromuser in friendsname:
        if '新年' in msg['Text']:
            return '新年快乐，祝您身体健康，万事胜意。'
        
        # 记录发送消息者入FriendList中
        elif Fromuser not in FriendList and msg['Text'] == '小小冰真漂亮':
            FriendList.append(Fromuser)
            return '通信建立成功'
           
        # 第一次发送消息过来，回复以下内容
        elif Fromuser in FriendList:
            if msg['Text'] in ['小小冰再见', '小小冰晚安', '小小冰下次聊']:
                FriendList.remove(Fromuser)
                return '再见，和您聊天十分开心，希望您今天过得愉快！'
            else:
                FriendList.append(Fromuser)
                itchat.send(msg['Text'], toUserName=AI)

        else:
            text = '''Mr.D先生现在不在，我是助手AI，有要事请拨打号码：xxxxxxxxxxx。如果想和我聊天，那就大声地说"小小冰真漂亮
                        （回复‘小小冰再见/小小冰晚安/小小冰下次聊’可结束此次聊天。）"'''
            return text

    # 群聊消息运行下面程序    
    elif Fromuser in groups:
        if msg.isAt:  
            if '新年' in msg['Content']:
                return '新年快乐，祝您身体健康，万事胜意。'
            elif Fromuser not in FriendList and msg['Content'] == '小小冰真漂亮':
                FriendList.append(Fromuser)
                return '通信建立成功'
            elif Fromuser in FriendList:
                if msg['Content'] in ['小小冰再见', '小小冰晚安', '小小冰下次聊']:
                    FriendList.remove(Fromuser)
                    return '再见，和您聊天十分开心，希望您今天过得愉快！'
                else:
                    FriendList.append(Fromuser)
                    itchat.send(msg['Content'], toUserName=AI) 
            else:
                text = '''Mr.D先生现在不在，我是助手AI，有要事请拨打号码：xxxxxxxxxxx。如果想和我聊天，那就大声地说"小小冰真漂亮
                        （回复‘小小冰再见/小小冰晚安/小小冰下次聊’可结束此次聊天。）"'''
                return text  
        
        elif msg['Text'] == '小小冰真漂亮':
            FriendList.append(Fromuser)
            return '通信建立成功'
 
        elif Fromuser in FriendList:
            if msg['Text'] in ['小小冰再见', '小小冰晚安', '小小冰下次聊']:
                FriendList.clear()
                return '再见，和您聊天十分开心，希望您今天过得愉快！'
            elif '新年' in msg['Text']:
                return '新年快乐，祝您身体健康，万事胜意。'
            else:
                FriendList.append(Fromuser)
                itchat.send(msg['Text'], toUserName=AI)  

    # 如果是自己发送消息，则清空列表
    elif Fromuser == user:
        FriendList.clear()
        
    # 其他公众号信息，就通知一声给微信文件助手
    else:
        itchat.send('公众号信息', toUserName='filehelper')

# 不具备转发图片与语音功能，提醒消息来源处
@itchat.msg_register([itcontent.PICTURE,itcontent.RECORDING,itcontent.VIDEO,itcontent.MAP],isFriendChat=True,isGroupChat=True,isMpChat=True)
def return_text(msg):
    text = '我不具备识别语音与图片等功能，请说普通话。'
    return text

itchat.run()
