from pprint import pprint
import requests
from line_token import *

richMenuId = "richmenu-bf647376a138de491d14e958978bb807"

url_upload_rich_menu = f'https://api.line.me/v2/bot/user/all/richmenu/{richMenuId}'

my_headers = {
    'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}'
}

response = requests.post(url = url_upload_rich_menu, headers = my_headers)

pprint(response.text)