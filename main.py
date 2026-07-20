import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token - get from environment
import os
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

# ── COMMANDS ──
async def start_command(update: Update, context):
    user = update.effective_user
    welcome_text = (
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to @Ap7eBot — your personal assistant!\n\n"
        "📌 I can help you with:\n"
        "• Daily tips\n"
        "• Fun facts\n"
        "• And more!\n\n"
        "👇 Tap a button below!"
    )
    await update.message.reply_text(welcome_text, reply_markup=get_main_menu())

async def help_command(update: Update, context):
    await update.message.reply_text(
        "🆘 *Help*\n\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/about - Learn about this bot",
        parse_mode="Markdown"
    )

async def about_command(update: Update, context):
    await update.message.reply_text(
        "📖 *About*\n\n"
        "A useful Telegram bot created with ❤️\n\n"
        "🔹 No data is stored\n"
        "🔹 Completely free to use",
        parse_mode="Markdown"
    )

# ── BUTTON HANDLER ──
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "menu_daily":
        await query.edit_message_text(
            "📅 *Daily Tip*\n\nTake 5 minutes to plan your day!\n\n🔙 Tap 'Main Menu' to go back.",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )
    elif data == "menu_funfact":
        facts = ["Octopuses have three hearts.", "Bananas are berries.", "Honey never spoils."]
        await query.edit_message_text(
            f"🧠 *Fun Fact*\n\n{random.choice(facts)}\n\n🔙 Tap 'Main Menu' to go back.",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )
    elif data == "menu_contact":
        await query.edit_message_text(
            "📬 *Contact*\n\nEmail: support@example.com\n\n🔙 Tap 'Main Menu' to go back.",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )
    elif data == "menu_help":
        await query.edit_message_text(
            "🆘 *Help*\n\nCommands: /start, /help, /about\n\n🔙 Tap 'Main Menu' to go back.",
            parse_mode="Markdown",
            reply_markup=get_main_menu()
        )

# ── MAIN ──
def main():
    if not TOKEN:
        logger.error("No token provided! Set TELEGRAM_BOT_TOKEN environment variable.")
        return
    
    logger.info("Starting bot...")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CallbackQueryHandler(button_callback))
    
    logger.info("Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
