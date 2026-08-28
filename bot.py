import logging
import os

import aiohttp
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

load_dotenv()


JOKE_API_URL = 'https://api.chucknorris.io/jokes/random'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def get_joke() -> str:
    """Fetch a random Chuck Norris joke from the API."""
    try:
        timeout = aiohttp.ClientTimeout(total=10)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(JOKE_API_URL) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('value', 'Joke not found!')

                logger.error('Joke API returned status %s.', response.status)
                return 'Error retrieving the joke.'
    except aiohttp.ClientError:
        logger.exception('Error connecting to the joke API.')
        return 'Error retrieving the joke.'
    except Exception:
        logger.exception('Unexpected error while retrieving the joke.')
        return 'Error retrieving the joke.'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command and display the main menu."""
    logger.info('User used /start.')

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('Get a joke', callback_data='get_joke')]
    ])

    await update.message.reply_text(
        'Hello! Press the button to get a joke. 😂',
        reply_markup=keyboard,
    )


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses and send a random joke."""
    query = update.callback_query

    await query.answer()

    if query.data == 'get_joke':
        logger.info('User requested a joke.')

        joke = await get_joke()

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton('Next joke', callback_data='get_joke')]
        ])

        await query.edit_message_text(
            joke,
            reply_markup=keyboard,
        )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE,) -> None:
    """Log errors and notify the user when possible."""
    logger.error('Error while processing the update.', exc_info=context.error,)

    if isinstance(update, Update) and update.message:
        try:
            await update.message.reply_text("An error occurred. We're already looking into it.")
        except Exception:
            logger.exception('Error notifying the user.')


def main() -> None:
    """Create the Telegram application and start polling."""
    token = os.getenv('TOKEN')

    if not token:
        raise ValueError('TOKEN is not set in the environment.')

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_error_handler(error_handler)

    logger.info('Bot is starting...')

    app.run_polling()


if __name__ == '__main__':
    main()