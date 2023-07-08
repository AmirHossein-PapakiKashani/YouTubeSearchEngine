import telebot

# Set up the Telegram bot
bot_token = "5995708641:AAFFquQIw7ssHU2nE4CaBHlXuA5-QhjBvmA"  # Replace with your Telegram bot token
telegram_bot = telebot.TeleBot(bot_token)

@telegram_bot.message_handler(commands=['get_user_id'])
def handle_get_user_id(message):
    user_id = message.chat.id
    telegram_bot.reply_to(message, f"Your user ID is: {user_id}")

# Start the bot
telegram_bot.polling()
