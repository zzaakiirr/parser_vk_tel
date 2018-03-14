import os
import json
import vk
import helpers


vk_app_id = os.environ.get('vk_app_id')
vk_login = os.environ.get('vk_login')
vk_password = os.environ.get('vk_password')

session = vk.AuthSession(
    app_id=vk_app_id, user_login=vk_login,
    user_password=vk_password)
api = vk.API(session, v=5.73, lang='en')


def fetch_news_from_vk():
    try:
        open('pynews_database.json')
    except FileNotFoundError:
        new_pynews_list = create_new_pynews_database()
    else:
        new_pynews_list = update_current_news_database()

    return new_pynews_list


def create_new_pynews_database():
    new_pynews_list = []
    new_pynews_list.append(api.newsfeed.search(q='Python language'))

    return new_pynews_list


def update_current_news_database():
    with open('pynews_database.json') as f_obj:
        old_pynews_database = json.loads(f_obj.read())
        new_pynews_dict = api.newsfeed.search(
            q='Python language',
            start_from=old_pynews_database[-1]['next_from'])
        new_pynews_list = old_pynews_database
        new_pynews_list.append(new_pynews_dict)

    return new_pynews_list


if __name__ == '__main__':
    new_pynews_list = fetch_news_from_vk()
    with open('pynews_database.json', 'w') as outfile:
        json.dump(new_pynews_list, outfile)
