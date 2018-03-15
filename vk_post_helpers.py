import pynews_database
from random import randint


def get_random_post_from_database(pynews_database):
    last_pynews_in_database = pynews_database[0]
    posts_list = last_pynews_in_database['items']
    random_post = posts_list[randint(0, len(posts_list))]
    return random_post


def create_post_link(post):
    # Post link template: 'https://vk.com/wall<author_id>_<post_id>'
    link = 'https://vk.com/wall' + str(post['from_id']) + '_' + str(post['id'])
    return link
