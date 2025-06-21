# Telegram Shop Bot

A Telegram bot for an Everlast Boxing Shop that allows users to browse products, get information, and simulate purchases. This project is designed for presentation purposes and demonstrates the integration of Telegram Bot API with OpenAI's GPT models.

## Features

- Interactive product catalog browsing
- Product information and pricing
- Simulated purchase process
- Conversational AI powered by OpenAI's GPT-4o
- Command-based navigation

## Note on Database

This project does not use a database because it is designed for presentation purposes only. In a production environment, a database would be implemented to store:
- User information
- Order history
- Product inventory
- Transaction records

## Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (from BotFather)
- OpenAI API Key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/TelegramShopBot.git
   cd TelegramShopBot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your API keys:
   - Open `shop_bot.py`
   - Replace `'YOUR API KEY'` with your OpenAI API key
   - Replace `'TELEGRAM BOT TOKEN'` with your Telegram bot token
   - Replace `'TELEGRAM BOT USERNAME'` with your bot's username

## Usage

1. Start the bot:
   ```
   python shop_bot.py
   ```

2. Open Telegram and search for your bot using its username

3. Start interacting with the bot using the following commands:
   - `/start` - Start the bot
   - `/help` - Show help message
   - `/products` - Browse product categories
   - `/contact` - Get contact information
   - `/about` - Learn about Everlast

4. You can also chat with the bot naturally to ask about products or initiate a purchase.

## Project Structure

- `shop_bot.py` - Main bot implementation
- `all_text.py` - Contains text content and product data
- `requirements.txt` - Project dependencies

## How It Works

The bot uses OpenAI's GPT-4o model to understand user queries and provide appropriate responses. It maintains a conversation history to provide context-aware interactions. When a user initiates a purchase, the bot collects their information and returns it as a JSON object (in a real application, this would be stored in a database).

## License

[MIT License](LICENSE)