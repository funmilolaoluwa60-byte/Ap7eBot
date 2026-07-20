from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu():
    """Return the main inline keyboard menu."""
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
