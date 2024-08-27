from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Substitua pelo seu token
TOKEN = '7159297970:AAHpBu5Suzq_zGkmj6X-7b3sLmRy6-xFBiQ'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou um bot.')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
