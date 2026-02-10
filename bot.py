import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ChatJoinRequestHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

CHANNELS = [
    -1003708594569,
    -1003797237946,
    -1003585811000,
    -1003737422554,
]

PHOTO_FILE_ID = "AgACAgUAAxkBAAMDaYr-66ojnCvF701cJ1NknwABL6uaAAIgD2sbaa5ZVBdxyTFJYbB0AQADAgADeQADOgQ"

VIDEO_FILE_ID = "BAACAgUAAxkBAAMGaYsBMV20nnbb4rsaPbLn1MRIHCsAApcrAALyjiBVj1XTQUYPxK86BA"

join_requests = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💖 Haan mujhe video chahiye", callback_data="want_video")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=PHOTO_FILE_ID,
        caption="Kya tumhe meri exclusive video chahiye? 😘",
        reply_markup=reply_markup
    )

async def show_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    buttons = []

    for ch in CHANNELS:
        invite = await context.bot.create_chat_invite_link(
            chat_id=ch,
            creates_join_request=True
        )

        buttons.append(
            [InlineKeyboardButton("🔐 Join Channel", url=invite.invite_link)]
        )

    buttons.append(
        [InlineKeyboardButton("✅ Maine Request Bhej Di", callback_data="check")]
    )

    reply_markup = InlineKeyboardMarkup(buttons)

    await query.message.reply_text(
        "Sabhi 4 channels me join request bhejo 👇",
        reply_markup=reply_markup
    )

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.chat_join_request.from_user.id
    chat_id = update.chat_join_request.chat.id

    if user_id not in join_requests:
        join_requests[user_id] = set()

    join_requests[user_id].add(chat_id)

async def check_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if user_id in join_requests:
        if set(CHANNELS).issubset(join_requests[user_id]):
            await query.message.reply_video(
                video=VIDEO_FILE_ID,
                caption="🎉 Thank you! Ye lo tumhari video."
            )
            return

    await query.message.reply_text(
        "❌ Abhi tak sab channels me request nahi bheji."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    app.add_handler(CallbackQueryHandler(show_channels, pattern="want_video"))
    app.add_handler(CallbackQueryHandler(check_request, pattern="check"))

    app.run_polling()

if __name__ == "__main__":
    main()




    
