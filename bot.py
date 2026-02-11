from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "APNA_REAL_BOT_TOKEN_YAHAN_DALO"

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        await update.message.reply_text(f"FILE_ID:\n{update.message.video.file_id}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.VIDEO, get_file_id))

app.run_polling()










    
