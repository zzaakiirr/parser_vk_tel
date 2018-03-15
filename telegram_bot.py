from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import pynews_database
import vk_post_helpers


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        "Hello, I'm a parser. What can I do?\nI find news about Python " +
        "(programming language) in social site http://vk.com " +
        "and send them to you here!\nJust put down '/pynews'")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def pynews(bot, update):
    new_pynews = pynews_database.fetch_pynews_from_vk()
    random_post = vk_post_helpers.get_random_post_from_database(
        new_pynews)
    post_link = vk_post_helpers.create_post_link(random_post)
    pynews_database.dump_new_pynews_to_database(new_pynews)
    update.message.reply_text(post_link)


def main():
    """Start the bot."""
    telegram_bot_access_token = os.environ.get('telegram_bot_access_token')
    updater = Updater(telegram_bot_access_token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("pynews", pynews))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
