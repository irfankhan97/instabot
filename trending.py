import json
import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post
from colorama import *
init()

def get_trending_tag_counts(tag):
    #print(media_id)
    #  message = raw_input("Enter ur comment....\n")
    # payload = {"access_token" : APP_ACCESS_TOKEN, "message":message}
    request_url = (BASE_URL + "tags/" + tag + "?access_token=" + APP_ACCESS_TOKEN)
    get_a_comment = requests.get(request_url).json()
    if get_a_comment['meta']['code'] == 200:
        print(Fore.CYAN+Style.BRIGHT+"Here is your tag...Popularity\n")
        print(Fore.GREEN+Style.BRIGHT+">>> "+str(get_a_comment['data']['media_count'])+" <<<")

        print (Style.RESET_ALL)
    else:
        print(Fore.RED+Style.BRIGHT+'not successful')

