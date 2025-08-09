from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# এখানে তোমার BotFather থেকে পাওয়া TOKEN দাও
TOKEN = "8436700730:AAECBJs3IoJsfBP9J9h55QYNs35nyTwRKfk"

# /start কমান্ডের জন্য হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো! আমি তোমার Simple Chatbot 🤖")

# যেকোনো মেসেজ রিপ্লাই দেওয়ার জন্য
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"তুমি লিখেছো: {user_message}")

# মেইন ফাংশন
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot চলছে... Ctrl+C দিয়ে বন্ধ করো।")
    app.run_polling()

if __name__ == "__main__":
    main()