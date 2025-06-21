import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import all_text as text
from openai import OpenAI



# Initialize LLM with your api_key
client = OpenAI(api_key='YOUR API KEY')


TOKEN = "TELEGRAM BOT TOKEN" # Bot's specific Token
USERNAME = "TELEGRAM BOT USERNAME" # Bot's specific Username


conversation_history = [
    {'role': 'system', 'content': text.system_message},
    {'role': 'system', 'content': text.products}
]


# LLM Chat
def chat_with_llm():


    # Conversation history exists?
    global conversation_history
    if 'conversation_history' not in globals():
        conversation_history = []


    # Send the entire history to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_history
    )

    # Store LLM response in history
    llm_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": llm_response})

    return llm_response






# Handle commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text.welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text.help_message)


async def products_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(chat_with_llm())


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text.contact_info)


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text.about_text)





# Handle message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input: str = update.message.text

    conversation_history.append({"role": "user", "content": user_input})
    response: str = chat_with_llm()

    try:
        # Try to parse the response as JSON
        parsed_response = json.loads(response)
        if isinstance(parsed_response, dict):  # Ensure the response is a JSON object
            print("Valid JSON Object received.")

            # Some actions with JSON


            await update.message.reply_text('Thank you for your purchase, we will send you a confirmation email shortly.')
        else:
            print("Sorry, something went wrong. Please try to buy later or contact support.")



    except json.JSONDecodeError:
        # If parsing fails, it's not valid JSON
        await update.message.reply_text(response)






# Handle error
async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

    # Send the error message to the user
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Sorry, something went wrong. Please try again later or use /help to see available commands."
        )



# Putting all together
if __name__ == '__main__':
    print("Starting Everlast Boxing Shop Bot...")

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('products', products_command))
    app.add_handler(CommandHandler('contact', contact_command))
    app.add_handler(CommandHandler('about', about_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(handle_error)

    # Check the chat for updates with 3-second intervals for better responsiveness
    print(f"Bot started successfully! Username: @{USERNAME}")
    app.run_polling(poll_interval=3)
