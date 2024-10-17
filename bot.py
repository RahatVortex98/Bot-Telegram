from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace 'YOUR_TOKEN' with your bot's API token
Token: Final = 'Your TOKEN'
BOT_USERNAME: Final = 'Your BOT NAME'

# Function to handle the /start command - baby bot introduction
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Oh hi there! 🍼 Goo goo ga ga! I’m just a wittle bot baby. How can I help you today? 👶✨')

# Function to handle the /help command - baby bot offering help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hiya! I’m a wittle bot baby, but I’m here to help! Type /start to get started! "
        "For other things, just tell me what you need, and I'll do my bestest to help you! Goo goo ga ga! ✨")

# Function to handle any custom command typed by the user
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# Function to process user messages and provide baby-like responses
def help_response(text: str) -> str:
    # Convert the incoming text to lowercase for easier comparison
    processed: str = text.lower()

    # Check for specific phrases and respond in a baby-like tone
    if "hello" in processed:
        return 'Hiya! Goo goo ga ga! I’m good, thanks for asking! 👶✨'

    if 'how are you' in processed:
        return 'I’m doing all wight! How about you? 👶💕'

    if 'i love you' in processed:
        return 'Aww, I wuv you too, mommy! 💖 Goo goo ga ga!'

    if 'good morning' in processed:
        return 'Mowning, mommy! Did you sweep well? ☀️ Goo goo!'

    if 'good night' in processed:
        return 'Nite nite, mommy! Don’t wet the bed! 😴💤 Goo goo ga!'

    if 'what are you doing' in processed:
        return 'I’m pwaying wif my toys! Wuv to pway! What about you? 🎲👶'

    if 'thank you' in processed:
        return 'You’re welcome, mommy! Goo goo, always here to help! 😇'

    if 'mommy' in processed:
        return 'Oh,Mommy!Stay strong,I will be there for you!  Goo goo ga ga! 💕👶'

    if 'hungry' in processed:
        return 'Oooh, I hungwy too! Can we have some milkies? 🍼 Goo goo!'

    if 'are you okay' in processed:
        return 'I’m otay, mommy! I’m just a wittle bot baby! Goo goo! 🥺👶'

    if 'play' in processed:
        return 'Pwaytime! Yay! What should we pway today? 🧸🎉 Goo goo!'

    if 'bye' in processed:
        return 'Bye-bye, mommy! Come back soon! Wuv you! 👋💕 Goo goo!'

    # Default response if no match is found
    return 'I don’t understand what you’re saying, but I still wuv you! 💕 Goo goo ga ga!'

# Function to handle regular user messages (with baby bot personality)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_type: str = update.message.chat.type  # Get the chat type (e.g., 'private' or 'group')
    text: str = update.message.text  # Get the text of the message
    print(f'User ({update.message.chat.id}) in {chat_type}: "{text}"')  # Log the message details

    # If the message is in a group, and the bot's username is mentioned
    if chat_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()  # Remove bot's username from the message
            response: str = help_response(new_text)  # Process the cleaned-up message
        else:
            return  # If the bot's username isn't mentioned, ignore the message
    else:
        response: str = help_response(text)  # For private chats, process the message directly

    print('Bot:', response)  # Log the bot's response
    await update.message.reply_text(response)  # Send the bot's response back to the user

# Function to log and handle errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')  # Print the error details

if __name__ == '__main__':
    print('Starting Bot...')

    # Create the bot application using the provided token
    app = Application.builder().token(Token).build()

    # Add command handlers to respond to /start, /help, and custom commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Add a message handler to respond to regular text messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Add an error handler
    app.add_error_handler(error)

    print('Polling...')

    # Start polling (bot listens for updates every 3 seconds)
    app.run_polling(poll_interval=3)
