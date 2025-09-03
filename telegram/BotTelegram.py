import token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       update.message.reply_text('Hello! I am your bot. How can I help you today?')

def main():
       application = ApplicationBuilder().token(token).build()

       application.add_handler(CommandHandler("start", start))

       application.run_polling()

if __name__ == '__main__':
    main()