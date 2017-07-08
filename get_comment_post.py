import json
import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post
def comment_user_post(insta_username):
    media_id = get_user_post(insta_username)
    print(media_id)
    #  message = raw_input("Enter ur comment....\n")
    # payload = {"access_token" : APP_ACCESS_TOKEN, "message":message}
    request_url = (BASE_URL + "media/" + media_id + "/comments?access_token=" + APP_ACCESS_TOKEN)
    get_a_comment = requests.get(request_url).json()
    print json.dumps(get_a_comment, indent=4, sort_keys=True)
    print 'GET request url : %s' % (request_url)
    print(get_a_comment['meta']['code'])
    if get_a_comment['meta']['code'] == 200:
        print(get_a_comment['data'][0]['text'])
    else:
        print('not successful')


#comment_user_post(insta_username="radhika12344")


