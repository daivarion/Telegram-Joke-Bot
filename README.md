# 😂 Joke Bot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge\&logo=python)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-Telegram-blue?style=for-the-badge\&logo=telegram)
![aiohttp](https://img.shields.io/badge/aiohttp-HTTP%20Client-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A small Telegram bot that delivers random Chuck Norris jokes.

---

## ⚙️ How It Works

The bot provides a simple interface for getting random Chuck Norris jokes.

When the user starts the bot, it displays a button for requesting a joke.

Pressing **Get a joke** sends a request to the Chuck Norris API and displays the returned joke.

The **Next joke** button can be used to request another joke without restarting the bot.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/daivarion/daivy-chuck-norris-bot.git
cd daivy-chuck-norris-bot
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory:

```env
TOKEN=your_telegram_bot_token
```

> 💡 **How to get a token?**
> 1. Open Telegram and find the **@BotFather** bot
> 2. Send the `/newbot` command
> 3. Follow the instructions and copy your token

Run the bot:

```bash
python bot.py
```

## 📖 Documentation

* [python-telegram-bot](https://docs.python-telegram-bot.org/)
* [aiohttp](https://docs.aiohttp.org/)
* [Chuck Norris API](https://api.chucknorris.io/)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

🌙 **Daivy**

*Building small things for a digital world.*

💜

</div>
