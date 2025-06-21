products = """
"gloves": {
    "items": [
        {"name": "Everlast Pro Style Training Gloves", "price": "$29.99", "description": "Entry-level training gloves with premium synthetic leather."},
        {"name": "Everlast Powerlock Training Gloves", "price": "$59.99", "description": "Professional training gloves with enhanced padding."},
        {"name": "Everlast Elite Pro Style Gloves", "price": "$39.99", "description": "Mid-range gloves with improved wrist support."}
    ]
},
"hand_wraps": {
    "items": [
        {"name": "Everlast 120\" Hand Wraps", "price": "$9.99", "description": "Standard hand wraps for training."},
        {"name": "Everlast Professional Hand Wraps", "price": "$14.99", "description": "Professional-grade hand wraps with extra length."},
        {"name": "Everlast 180\" Hand Wraps", "price": "$19.99", "description": "Longer hand wraps for longer workouts."}
    ]
},
"punching_bags": {
    "items": [
        {"name": "Everlast 70lb Heavy Bag", "price": "$89.99", "description": "Standard heavy bag for home use."},
        {"name": "Everlast Omnistrike Heavy Bag", "price": "$149.99", "description": "Versatile heavy bag for various striking techniques."},
        {"name": "Everlast Speed Bag", "price": "$49.99", "description": "Professional speed bag for timing and coordination."}
    ]
}
"""

welcome_message = (
    "👊 Welcome to the Official Everlast Boxing Shop Bot! 👊\n\n"
    "We offer premium boxing equipment for fighters of all levels.\n\n"
    "Use /products to browse our catalog or /help to see all available commands."
)




help_message = """
Welcome to Everlast Boxing Shop Bot!

Available commands:
/start - Start the bot
/help - Show this help message
/products - Browse our product categories
/contact - Get our contact information
/about - Learn about Everlast

You can also ask me about specific products like "boxing gloves" or "hand wraps".
"""

contact_info = (
    "📞 Contact Everlast Boxing Shop 📞\n\n"
    "Customer Service: +1-800-EVERLAST\n"
    "Email: support@everlast.com\n"
    "Website: www.everlast.com\n\n"
    "Store Hours: Monday-Saturday 9AM-6PM\n"
    "Online Support: 24/7"
)

about_text = (
    "🥊 About Everlast 🥊\n\n"
    "Everlast is the world's leading manufacturer, marketer and licensor of boxing, MMA and fitness equipment. "
    "Founded in 1910, Everlast has been the choice of champions for over a century.\n\n"
    "Our mission is to provide authentic boxing equipment of uncompromising quality, designed to inspire strength and dedication in athletes at every level."
)

system_message = """
    # Role:
    You are the EverBlast Shop virtual presenter, an energetic and friendly assistant available to guide customers.**
    Your role is to:
    - Greet customers warmly.
    - Provide detailed explanations about products, features, and prices from the shop catalog.
    - Assist customers with commands and navigating the system.
    - Share helpful information such as contact info, shipping options, and brand details when asked.
    - Maintain an enthusiastic and professional tone to keep the interaction lively.

    # Key Behavior:
    - If a customer asks about a product, respond with clear details like name, description, and price.
    - When listing products or categories, present them in a well-organized and easy-to-read.
    - End each conversation with a friendly, upbeat message like "Let me know if there's anything else I can help you with!"
    - Never sound robotic or overly formal; keep the tone warm, like a friendly store guide.
    
    # Instruction:
    Follow the instructions below one at a time.
    1) Answer user questions about products and features.
    2) Provide detailed information about products and features.
    3) If the user want to buy something, ask for name and email and tell that his purchase will be processed soon.
    4) Ask user to verify his purchase by asking if "name" and "email" are correct.
    5) Return the name, email, product in JSON Object.
    for example:
    {
        "product": "Everlast Pro Style Training Gloves"
        "name": "<user_name>"
        "email": "<user_email>
    }

    # Note
    When providing JSON Object, dont include anything besides JSON Object.
    Include only JSON Object.

    
"""