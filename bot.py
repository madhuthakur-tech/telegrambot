import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

CHANNELS = [
    "https://t.me/+xiDyyJTIWccxYzll",
    "https://t.me/+K3jud7ThW4Q4NDQ1",
    "https://t.me/+-s8gGlM-BcY1NDll",
    "https://t.me/+_YmoMrDZ0oliMTll",
]

VIDEO_LINK = "https://t.me/yourchannel1/10"  # yaha apni video post link

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💖 Haan mujhe video chahiye", callback_data="want_video")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Hello! Bot running successfully ✅\n\nKya tumhe meri exclusive video chahiye? 😘",
        reply_markup=reply_markup
    )

async def want_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    buttons = []
    for link in CHANNELS:
        buttons.append([InlineKeyboardButton("🔐 Join Channel", url=link)])

    buttons.append([InlineKeyboardButton("✅ Done (Video Do)", callback_data="send_video")])

    await query.message.reply_text(
        "Pehle in sab channels ko join karo 👇",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.reply_text(
        f"🎥 Ye lo tumhari video:\n{VIDEO_LINK}"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(want_video, pattern="want_video"))
    app.add_handler(CallbackQueryHandler(send_video, pattern="send_video"))

    app.run_polling()

if __name__ == "__main__":
    main()





    
