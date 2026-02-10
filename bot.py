import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ChatJoinRequestHandler,
    ContextTypes,
)

# =========================
# BOT TOKEN
# =========================
TOKEN = os.getenv("BOT_TOKEN")

# =========================
# VIDEO FILE ID (apna daal)
# =========================
VIDEO_FILE_ID = "BAACAgUAAxkBAAMGaYsBMV20nnbb4rsaPbLn1MRIHCsAApcrAALyjiBVj1XTQUYPxK86BA"

# =========================
# START COMMAND
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello!\n\n"
        "Private channel join request bhejo.\n"
        "Request jaise hi jayegi, video mil jayegi 😈🔥"
    )

# =========================
# JOIN REQUEST HANDLER
# =========================
async def join_request_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    user_id = user.id
    channel_name = update.chat_join_request.chat.title

    try:
        await context.bot.send_video(
            chat_id=user_id,
            video=VIDEO_FILE_ID,
            caption=f"✅ Request received in: {channel_name}\n\n🎥 Ye lo tumhari video 🔥"
        )
    except Exception as e:
        print("Error sending video:", e)

# =========================
# MAIN
# =========================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(join_request_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()









    
