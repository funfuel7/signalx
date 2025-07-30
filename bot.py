from telegram.ext import Updater, CommandHandler
from suggest import get_trade_suggestions
from config import TELEGRAM_BOT_TOKEN

def start(update, context):
    update.message.reply_text("🤖 Bot is live and ready. Use /scan or /suggest or /startloop.")

def suggest(update, context):
    suggestions = get_trade_suggestions()
    for s in suggestions:
        update.message.reply_text(s)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("suggest", suggest))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
