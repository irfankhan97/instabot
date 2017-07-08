import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post


def like_user_post(insta_username):
    media_id = get_user_post(insta_username)
    request_url = (BASE_URL + "media/"+media_id+"/likes")
    payload = {"access_token" : APP_ACCESS_TOKEN}
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print '\n...Like was successful!....'
    else:
        print 'Your like was unsuccessful. Try again!'



#like_user_post(insta_username="radhika12344")
