from like_user_post import like_user_post
from comment_a_Post import comment_user_post
from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info

show_menu = True
while show_menu:
    menu_choices = "What do you want to do? \n 1. Like A Post \n 2. Comment on a post \n 3. Download Own Post \n 4. Download Friend's post \n 5. Get Friend Info. \n 6. Close Application \n"
    menu_choice = input(menu_choices)

    if (menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            insta_username = raw_input("Enter Username.........\n")
            like_user_post(insta_username)

        elif menu_choice == 2:
            insta_username = raw_input("Enter Username.........\n")
            comment_user_post(insta_username)
        elif menu_choice == 3:
            print ("WAit Getting ur post.......\n")
            get_own_post()
        elif menu_choice == 4:
            insta_username = raw_input("Enter Username.........\n")
            get_user_post(insta_username)
        elif menu_choice == 5:
            insta_username = raw_input("Enter Username.........\n")
            get_user_info(insta_username)
        else:
            show_menu = False