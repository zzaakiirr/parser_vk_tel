import os
import json
import vk

new_pynews_list = []

vk_app_id = os.environ.get('vk_app_id')
vk_login = os.environ.get('vk_login')
vk_password = os.environ.get('vk_password')

session = vk.AuthSession(
    app_id=vk_app_id, user_login=vk_login,
    user_password=vk_password, scope='wall, messages')
api = vk.API(session, v=5.73, lang='en')

try:
    open('pynews_database.json')
except FileNotFoundError:
    new_pynews_list.append(api.newsfeed.search(q='Python language'))
else:
    with open('pynews_database.json') as f_obj:
        old_pynews_database = json.loads(f_obj.read())
        new_pynews_dict = api.newsfeed.search(
            q='Python language',
            start_from=old_pynews_database[-1]['next_from'])
        new_pynews_list = old_pynews_database
        new_pynews_list.append(new_pynews_dict)

with open('pynews_database.json', 'w') as outfile:
    json.dump(new_pynews_list, outfile)
