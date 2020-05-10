"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    PollHandler,
    Filters,
)
from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def fetch_response(update, context):
    """Echo the user message."""
    response = update.message.text
    if response.startswith("sleep-"):
        update.message.reply_text(response.split('-')[1])
        measure_me(update, context, state='body')
    elif response.startswith("body-"):
        update.message.reply_text(response.split('-')[1])
        measure_me(update, context, state='mind')
    elif response.startswith("mind-"):
        update.message.reply_text(response.split('-')[1])
        measure_me(update, context, state='motivation')
    elif response.startswith("motivation-"):
        update.message.reply_text(response.split('-')[1])
        measure_me(update, context, state='dream')
    elif response.startswith("dream-"):
        update.message.reply_text(response.split('-')[1])
        measure_me(update, context, state='done')
    else:
        update.message.reply_text(update.message.text)

def measure_me(update, context, state='sleep'):
    """Starts the user poll."""
    if state == 'sleep':
        custom_keyboard = [
            ['sleep-7', 'sleep-8', 'sleep-9'],
            ['sleep-4', 'sleep-5', 'sleep-6'],
            ['sleep-1', 'sleep-2', 'sleep-3'],
        ]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="How did you sleep today?", reply_markup=reply_markup)
    elif state == 'body':
        custom_keyboard = [
            ['body-7', 'body-8', 'body-9'],
            ['body-4', 'body-5', 'body-6'],
            ['body-1', 'body-2', 'body-3'],
        ]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="How does your body feel?", reply_markup=reply_markup)
    elif state == 'mind':
        custom_keyboard = [
            ['mind-7', 'mind-8', 'mind-9'],
            ['mind-4', 'mind-5', 'mind-6'],
            ['mind-1', 'mind-2', 'mind-3'],
        ]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="How does your mind feel?", reply_markup=reply_markup)
    elif state == 'motivation':
        custom_keyboard = [
            ['motivation-7', 'motivation-8', 'motivation-9'],
            ['motivation-4', 'motivation-5', 'motivation-6'],
            ['motivation-1', 'motivation-2', 'motivation-3'],
        ]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="How motivated are you today?", reply_markup=reply_markup)
    elif state == 'dream':
        custom_keyboard = [
            ['dream-Yes', 'dream-No']
        ]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Any dreams today?", reply_markup=reply_markup)
    elif state == 'done':
        reply_markup = ReplyKeyboardRemove()
        update.message.reply_text(text="Measurement completed", reply_markup=reply_markup)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.environ.get('API_TOKEN'), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("measure_me", measure_me))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, fetch_response))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
