from like_user_post import like_user_post
from comment_a_Post import comment_user_post
from get_user_post import get_user_post
from get_own_post import get_own_post
from get_user_info import get_user_info
import get_comment_post
from colorama import init
from colorama import Fore,Back,Style
init()
from trending import get_trending_tag_counts


show_menu = True
while show_menu:
    print(Fore.GREEN+Style.BRIGHT+'.....................Welcome ....TO......InstaBot..............')
    print(Fore.YELLOW+Style.BRIGHT+"\n...................MAke...... Your... Life.. Easy............\n\n")
    menu_choices = Fore.CYAN+Style.BRIGHT+"What do you want to do? \n 1. Like A Post \n 2. Comment on a post \n 3. Download Own Post \n 4. Download Friend's post \n 5. Get Friend Info. \n 6. Get Friend's comments\n 7. Count ur Tag\n\n"
    menu_choice = input(menu_choices)



    if (menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait liking Ur POst......")
            like_user_post(insta_username)
            print(Style.RESET_ALL)
            print("\n")
            print("\n")

        elif menu_choice == 2:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"wait work under process.......")
            comment_user_post(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
        elif menu_choice == 3:
            print (Fore.GREEN+Style.BRIGHT+"WAit Getting ur post.......\n")
            get_own_post()
            print 'Your image has been downloaded!....to.....C:\Users\DELL\PycharmProjects\instabot...'
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
        elif menu_choice == 4:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait Downloading user post......")
            get_user_post(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
        elif menu_choice == 5:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait getting information.....")
            get_user_info(insta_username)
            print 'Your image has been downloaded!....to.....C:\Users\DELL\PycharmProjects\instabot...'
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
        elif menu_choice == 6:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print("\n"+Fore.GREEN+Style.BRIGHT+"Wait getting information.....\n")
            get_comment_post.comment_user_post(insta_username)
            print (Style.RESET_ALL)
            print("\n")
            print("\n")
        if menu_choice == 7:
            tag = raw_input(Fore.RED+Style.BRIGHT+"Enter Tagname.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait counting Ur Tags......")
            get_trending_tag_counts(tag)
            print(Style.RESET_ALL)
            print("\n")
            print("\n")
        else:
            show_menu = False