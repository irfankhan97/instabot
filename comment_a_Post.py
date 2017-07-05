import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post

username = "radhika12344"

def like_user_post(insta_username):
    media_id = get_user_post(insta_username)
    request_url = (BASE_URL + "/media/&s/comments") % (media_id)
    message = raw_input("enter ur comment")
    payload = {"access_token" : APP_ACCESS_TOKEN, "message":message}
    post_a_comment = requests.post(request_url,payload).json()
    if post_a_comment['meta']['code']== 200:
        print("Post comment successfully")
    else :
        print('comment has not posted')

like_user_post(username)


