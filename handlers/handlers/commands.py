from telegram import Update
from telegram.ext import ContextTypes
from keyboards.inline import get_main_menu

# ── START COMMAND ──
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message with inline keyboard when /start is issued."""
    user = update.effective_user
    welcome_text = (
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to @Ap7eBot — your personal assistant for quick tasks and useful information.\n\n"
        "📌 I can help you with:\n"
        "• Daily tips and reminders\n"
        "• Quick calculations\n"
        "• Fun facts and inspiration\n\n"
        "👇 Tap a button below to get started!"
    )
    await update.message.reply_text(welcome_text, reply_markup=get_main_menu())

# ── HELP COMMAND ──
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when /help is issued."""
    help_text = (
        "🆘 *How to use @Ap7eBot*\n\n"
        "Here are the available commands:\n"
        "/start - Start the bot and see the main menu\n"
        "/help - Show this help message\n"
        "/about - Learn more about this bot\n\n"
        "You can also tap the buttons below the chat to explore features!\n\n"
        "💡 *Tip:* This bot is regularly updated with new features."
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# ── ABOUT COMMAND ──
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send information about the bot when /about is issued."""
    about_text = (
        "📖 *About @Ap7eBot*\n\n"
        "This bot was created to provide quick and useful information right inside Telegram.\n\n"
        "🔹 *Purpose:* Help users with daily tasks and entertainment\n"
        "🔹 *Features:* Interactive menus, quick responses, and more\n"
        "🔹 *Privacy:* No data is stored or shared with third parties\n\n"
        "Thank you for using @Ap7eBot! 🙌"
    )
    await update.message.reply_text(about_text, parse_mode="Markdown")

# ── BUTTON CALLBACK HANDLER ──
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button presses."""
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
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries aren't.",
            "A day on Venus is longer than a year on Venus.",
            "Honey never spoils—archaeologists found 3000-year-old honey.",
            "The Eiffel Tower can grow 15 cm taller in summer."
        ]
        import random
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
            "✉️ *Email:* support@ap7ebot.com (example)\n"
            "🐦 *Twitter:* @Ap7eBot (example)\n\n"
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
