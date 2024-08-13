from pprint import pprint
import requests
from line_token import *

rich_menu = 'richmenu-bf647376a138de491d14e958978bb807'

url_upload_rich_menu = f'https://api-data.line.me/v2/bot/richmenu/{rich_menu}/content'

myheaders = {
    'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}',
    'Content-Type': 'image/jpeg'
}

file_path = './richmenu.jpg'
response = requests.post(
    url= url_upload_rich_menu, 
    data= open(file_path,'rb'),
    headers= myheaders
    )

pprint(response.json())

# 回應結果為{}代表成功