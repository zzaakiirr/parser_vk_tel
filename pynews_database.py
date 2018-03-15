import os
import json
import vk


vk_app_id = os.environ.get('vk_app_id')
vk_login = os.environ.get('vk_login')
vk_password = os.environ.get('vk_password')

session = vk.AuthSession(
    app_id=vk_app_id, user_login=vk_login,
    user_password=vk_password)
api = vk.API(session, v=5.73, lang='en')


def dump_new_pynews_to_database(new_pynews):
    with open('pynews_database.json', 'w') as outfile:
        json.dump(new_pynews, outfile)


def fetch_pynews_from_vk():
    try:
        open('pynews_database.json')
    except FileNotFoundError:
        new_pynews = create_new_pynews_database()
    else:
        new_pynews = update_current_pynews_database()

    return new_pynews


def create_new_pynews_database():
    new_pynews = []
    new_pynews.append(api.newsfeed.search(q='Python language'))

    return new_pynews


def update_current_pynews_database():
    with open('pynews_database.json') as f_obj:
        old_pynews_database = json.loads(f_obj.read())

    last_added_news_to_old_pynews_database = old_pynews_database[-1]
    page_for_searching = last_added_news_to_old_pynews_database['next_from']
    new_pynews_dict = api.newsfeed.search(
        q='Python language',
        start_from=page_for_searching)
    new_pynews = old_pynews_database
    new_pynews.append(new_pynews_dict)

    return new_pynews


if __name__ == '__main__':
    new_pynews = fetch_pynews_from_vk()
    dump_new_pynews_to_database(new_pynews)
