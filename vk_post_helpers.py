import pynews_database
from random import randint


def get_random_post_from_database(pynews_database):
    last_added_news_to_pynews_database = pynews_database[-1]
    last_added_posts_list = last_added_news_to_pynews_database['items']
    random_post = last_added_posts_list[randint(0, len(last_added_posts_list))]
    return random_post


def create_post_link(post):
    # Post link template: 'https://vk.com/wall<author_id>_<post_id>'
    link = 'https://vk.com/wall' + str(post['from_id']) + '_' + str(post['id'])
    return link
