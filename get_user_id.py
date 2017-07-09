import requests
from constants import *
from colorama import *
init()

def get_user_id(insta_username):
    #function logic
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print Fore.RED+Style.BRIGHT+'Status code other than 200 received!'
        exit()
