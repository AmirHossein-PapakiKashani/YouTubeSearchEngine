from googleapiclient.discovery import build
import telebot

# Set up the YouTube API client
api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyDLckUBZaoSoNNNK-Np0UtqHyGOElZPx3M"  # Replace with your actual API key

youtube = build(api_service_name, api_version, developerKey=api_key)

# Set up the Telegram bot
bot_token = "5995708641:AAFFquQIw7ssHU2nE4CaBHlXuA5-QhjBvmA"  # Replace with your Telegram bot token
telegram_bot = telebot.TeleBot(bot_token)

@telegram_bot.message_handler(commands=['search'])
def handle_search_command(message):
    # Extract the search query from the command
    search_query = message.text.replace('/search', '').strip()

    # Make a request to the YouTube API
    request = youtube.search().list(
        part="id,snippet",
        q=search_query,
        type="video",
        maxResults=10
    )

    response = request.execute()

    # Process the response
    for item in response['items']:
        video_id = item['id']['videoId']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        video_title = item['snippet']['title']
        message = f"{video_title}\n{video_link}"
        telegram_bot.send_message(chat_id=5995708641, text=message)

# Start the bot
telegram_bot.polling()
