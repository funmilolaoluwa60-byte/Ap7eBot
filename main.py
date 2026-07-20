import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
)

from config import TELEGRAM_BOT_TOKEN
from handlers.commands import start_command, help_command, about_command, button_callback

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("No token provided! Set TELEGRAM_BOT_TOKEN in environment.")
        return

    logger.info("Starting @Ap7eBot...")

    # Create the Application
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))

    # Register callback handler for inline buttons
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the bot (long polling)
    logger.info("Bot is running. Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
