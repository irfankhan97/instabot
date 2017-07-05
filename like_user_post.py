import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post

username = "radhika12344"

def like_user_post(insta_username):
    media_id = get_user_post(insta_username)
    request_url = (BASE_URL + "/media/&s/likes") % (media_id)
    payload = {"access_token" : APP_ACCESS_TOKEN}
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code']== 200:
        print("Post liked successfully")
    else :
        print('User does not exist')

like_user_post(username)


