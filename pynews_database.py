import json

import vk
import vk_auth


def read_data_from_database():
    with open('pynews_database.json') as f_obj:
        pynews_database = json.loads(f_obj.read())

    return pynews_database


def dump_new_pynews_to_database(new_pynews):
    with open('pynews_database.json', 'w') as outfile:
        json.dump(new_pynews, outfile)


def is_database_contains():
    try:
        open('pynews_database.json')
    except FileNotFoundError:
        return False
    else:
        return True


def create_new_pynews_database(api):
    new_pynews = list()
    new_pynews.append(api.newsfeed.search(q='Python language'))

    return new_pynews


def update_current_pynews_database(api):
    old_pynews_database = read_data_from_database()

    last_added_news_to_old_pynews_database = old_pynews_database[-1]
    page_for_searching = last_added_news_to_old_pynews_database['next_from']
    new_pynews_dict = api.newsfeed.search(
        q='Python language',
        start_from=page_for_searching
    )
    new_pynews = old_pynews_database
    new_pynews.append(new_pynews_dict)

    return new_pynews


def fetch_pynews_from_vk(api):
    if is_database_contains():
        new_pynews = create_new_pynews_database(api)
    else:
        new_pynews = update_current_pynews_database(api)

    return new_pynews


def main():
    api = vk_auth.fetch_vk_api()
    new_pynews = fetch_pynews_from_vk(api)
    dump_new_pynews_to_database(new_pynews)


if __name__ == '__main__':
    main()
