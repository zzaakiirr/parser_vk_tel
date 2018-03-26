import os

import vk


def fetch_vk_api():
    vk_app_id = os.environ.get('vk_app_id')
    vk_login = os.environ.get('vk_login')
    vk_password = os.environ.get('vk_password')

    session = vk.AuthSession(
        app_id=vk_app_id,
        user_login=vk_login,
        user_password=vk_password
    )
    api = vk.API(session, v=5.73, lang='en')

    return api
