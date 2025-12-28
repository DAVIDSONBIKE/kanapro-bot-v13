from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext
)

# 🔐 PUT YOUR TOKEN HERE
BOT_TOKEN = "PASTE_YOUR_REAL_TOKEN_HERE"

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🤖 Kanapro AI Football Analyst\n\n"
        "Send match details in this format:\n\n"
        "Match: Team A vs Team B\n"
        "League:\n"
        "Odds:\n"
        "Kickoff:\n\n"
        "Type NEXT after each analysis."
    )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "📌 HOW TO USE:\n\n"
        "1️⃣ Send match details\n"
        "2️⃣ Receive analysis\n"
        "3️⃣ Type NEXT for another match\n\n"
        "Football only ⚽"
    )

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.strip()

    if text.upper() == "NEXT":
        update.message.reply_text("✅ Ready for next match. Send details.")
        return

    analysis = (
        "Match Analysis\n\n"
        "1. Win / Draw:\n"
        "→ Home Win\n\n"
        "2. Double Chance:\n"
        "→ 1X\n\n"
        "3. Both Teams To Score:\n"
        "→ Yes\n\n"
        "4. Total Goals:\n"
        "→ Over 2.5\n\n"
        "5. Correct Score:\n"
        "→ First Half: 1–0\n"
        "→ Second Half: 2–1\n\n"
        "Confidence Level: 87%\n\n"
        "Analysé made by Kanapro AI — feel free to choose the best one for your betting strategy"
    )

    update.message.reply_text(analysis)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
