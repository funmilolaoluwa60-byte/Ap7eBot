import os
import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ── KEYBOARD ──
def get_main_menu():
    keyboard = [
        [
            InlineKeyboardButton("📅 Daily Tip", callback_data="menu_daily"),
            InlineKeyboardButton("🧠 Fun Fact", callback_data="menu_funfact"),
        ],
        [
            InlineKeyboardButton("📬 Contact", callback_data="menu_contact"),
            InlineKeyboardButton("🆘 Help", callback_data="menu_help"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

# ── COMMAND HANDLERS ──
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to @Ap7eBot — your personal assistant!\n\n"
        "📌 I can help you with:\n"
        "• Daily tips and reminders\n"
        "• Fun facts and inspiration\n"
        "• Quick assistance\n\n"
        "👇 Tap a button below to get started!"
    )
    await update.message.reply_text(welcome_text, reply_markup=get_main_menu())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🆘 *Help*\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/about - Learn about this bot\n\n"
        "💡 Tap any button to explore features!"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "📖 *About @Ap7eBot*\n\n"
        "A useful Telegram bot created with ❤️\n\n"
        "🔹 *Purpose:* Help users with daily tasks\n"
        "🔹 *Privacy:* No data stored\n"
        "🔹 *Free:* Completely free to use\n\n"
        "Thank you for using @Ap7eBot! 🙌"
    )
    await update.message.reply_text(about_text, parse_mode="Markdown")

# ── BUTTON HANDLER ──
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    user = query.from_user

    if data == "menu_daily":
        await query.edit_message_text(
            f"📅 *Daily Tip for {user.first_name}*\n\n"
            "✨ *Tip of the day:* Take 5 minutes to plan your day—it boosts productivity!\n\n"
            "🔹 Break big tasks into small steps\n"
            "🔹 Prioritize the most important task first\n"
            "🔹 Stay hydrated and take short breaks\n\n"
            "Come back tomorrow for a new tip! 🌟",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )

    elif data == "menu_funfact":
        fun_facts = [
            "Octopuses have three hearts 🐙",
            "Bananas are berries, but strawberries aren't 🍌",
            "A day on Venus is longer than a year on Venus 🌌",
            "Honey never spoils—archaeologists found 3000-year-old honey 🍯",
            "The Eiffel Tower can grow 15 cm taller in summer 🗼"
        ]
        fact = random.choice(fun_facts)
        await query.edit_message_text(
            f"🧠 *Fun Fact for {user.first_name}*\n\n"
            f"📌 {fact}\n\n"
            "Tap below for more facts or return to the main menu! 🔄",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )

    elif data == "menu_contact":
        await query.edit_message_text(
            "📬 *Contact & Support*\n\n"
            "We're here to help! Here's how to reach us:\n\n"
            "✉️ *Email:* support@ap7ebot.com\n"
            "🐦 *Twitter:* @Ap7eBot\n\n"
            "📌 *Feedback is always welcome!*\n"
            "Tell us what features you'd like to see next.\n\n"
            "🔙 Tap 'Main Menu' to go back.",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )

    elif data == "menu_help":
        help_text = (
            "🆘 *Help & Support*\n\n"
            "Here are the available commands:\n"
            "/start - Start the bot\n"
            "/help - Show this help\n"
            "/about - Learn more about the bot\n\n"
            "📌 Tap any button to explore features!\n"
            "🔙 Tap 'Main Menu' to go back."
        )
        await query.edit_message_text(
            help_text,
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )

# ── MAIN ──
def main():
    if not TOKEN:
        logger.error("❌ No token provided! Set TELEGRAM_BOT_TOKEN environment variable.")
        return

    logger.info("🚀 Starting @Ap7eBot...")
    
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Start the bot
    logger.info("✅ Bot is running! Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
