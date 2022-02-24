import logging
from telegram import *
from telegram.ext import *
import Responses
import config


API_KEY = "Api_Key"

#set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    #starts the conversation
    update.message.reply_text("Hello There, I'm Arnold the Accountability Bot. After your First checkin using the /checkin command I\'ll check back in with you the next day around the same time.")


def help_command(update, context):
    #instructs to dm creator for assistance
    update.message.reply_text("Contact @twistalon for help")


def Checkin(update, context):
    #checkin for workout

    message = 'Did You Workout Today? \'yes\' or \'no\''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


    checkin_handler = CommandHandler('Checkin', Checkin)
    Dispatcher.add_handler(checkin_handler)
    updater.start_polling()

def checkintimer(bot,job_queue, update):
    job_queue.run_repeating(Checkin(), 5, context=bot.send_message(chat_id=update.effective_chat.id))


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'user ({update.message.chat.id}) says: {text}')
    response = Responses.get_response(text)

    #bot response
    update.message.reply_text(response)

def error(update, context):
    logging.error(f'update{update} caused error {context.error}')


if __name__  == "__main__":
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher


    #commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('Checkin', Checkin))

    #messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    #log all errors
    dp.add_error_handler(error)

    #running the bot
    updater.start_polling(1.0)
    updater.idle
