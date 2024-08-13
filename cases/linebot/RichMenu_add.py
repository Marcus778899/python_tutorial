from pprint import pprint
import requests
from line_token import *

# 新增Rich Menu的網址
url_add_rich_menu = f'https://api.line.me/v2/bot/richmenu'

# 聊天機器人名稱
chatbot_name = '情緒選單'

# spec & setting
str_raw = '''
{
    "size":{
        "width":2500,
        "height":1686
    },
    "selected":false,
    "name":"my rich menu",
    "chatBarText":"''' + chatbot_name + '''",
    "areas":[
        {
        "bounds":{
            "x":0,
            "y":0,
            "width":833.333,
            "height":843
        },
        "action":{
            "type":"message",
            "text":"喜歡"
        }
        },
        {
        "bounds":{
            "x":833.333,
            "y":0,
            "width":833.333,
            "height":843
        },
        "action":{
            "type":"message",
            "text":"悲傷"
        }
        },
        {
        "bounds":{
            "x":1666.666,
            "y":0,
            "width":833.333,
            "height":843
        },
        "action":{
            "type":"message",
            "text":"厭惡"
        }
        },
        {
        "bounds":{
            "x":0,
            "y":843,
            "width":833.333,
            "height":843
        },
        "action":{
            "type":"message",
            "text":"憤怒"
        }
        },
        {
        "bounds":{
            "x":833.333,
            "y":843,
            "width":833.333,
            "height":843
        },
        "action":{
            "type":"message",
            "text":"幸福"
        }
        },
        {
        "bounds":{
            "x":1666.666,
            "y":843,
            "width":833.333,
            "height":843
        },
        "action":{
            "type":"message",
            "text":"其它"
        }
        }
    ]
}
'''

str_raw = str_raw.encode('utf-8')

my_headers = {
    'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

response = requests.post(url_add_rich_menu, headers=my_headers, data=str_raw)

pprint(response.text)