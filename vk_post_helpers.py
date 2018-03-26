from random import randint

import pynews_database


def get_random_post_from_database(pynews_database):
    last_pynews_in_database = pynews_database[0]
    posts_list = last_pynews_in_database['items']
    random_post = posts_list[randint(0, len(posts_list))]
    return random_post


def create_post_link(post):
    author_id = post['from_id']
    post_id = post['id']
    link = 'https://vk.com/wall{author_id}_{post_id}'.format(
        author_id=author_id,
        post_id=post_id
    )
    return link
