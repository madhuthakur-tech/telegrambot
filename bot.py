import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_IDS = [
    -1003708594569,
    -1003797237946,
    -1003585811000,
    -1003737422554,
]

CHANNEL_LINKS = [
    "https://t.me/+_YmoMrDZ0oliMTll",
    "https://t.me/+-s8gGlM-BcY1NDll",
    "https://t.me/+az-lgmrUAnU1MzQ1",
    "https://t.me/+Ltw6NlDYtaQ5OWE1",
]

PHOTO_FILE_ID = "AgACAgUAAxkBAAMDaYr-66ojnCvF701cJ1NknwABL6uaAAIgD2sbaa5ZVBdxyTFJYbB0AQADAgADeQADOgQ"
VIDEO_FILE_ID = "BAACAgUAAxkBAAMGaYsBMV20nnbb4rsaPbLn1MRIHCsAApcrAALyjiBVj1XTQUYPxK86BA"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💖 Haan mujhe video chahiye", callback_data="want_video")]
    ]

    await update.message.reply_photo(
        photo=PHOTO_FILE_ID,
        caption="Kya tumhe meri exclusive video chahiye? 😘",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def want_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("Join karo phir verify dabao ✅")

    buttons = []
    for link in CHANNEL_LINKS:
        buttons.append([InlineKeyboardButton("🔐 Join Channel", url=link)])

    buttons.append([InlineKeyboardButton("✅ Verify", callback_data="verify")])

    await query.message.reply_text(
        "Pehle 4 channels me join request bhejo 👇\n\nPhir Verify dabao ✅",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    await query.answer("Checking... ⏳")

    not_joined = []

    for channel_id in CHANNEL_IDS:
        try:
            member = await context.bot.get_chat_member(channel_id, user_id)

            if member.status in ["left", "kicked"]:
                not_joined.append(channel_id)

        except Exception as e:
            not_joined.append(channel_id)

    if not_joined:
        await query.message.reply_text(
            "❌ Tumne abhi tak sab channels join nahi kiye.\n\n⚠️ Pehle join karo phir Verify dabao."
        )
        return

    await query.message.reply_video(
        video=VIDEO_FILE_ID,
        caption="🎉 Verified! Ye lo tumhari video 😘"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(want_video, pattern="want_video"))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()







    
