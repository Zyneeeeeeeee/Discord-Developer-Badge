# 🤖 My Awesome Discord Bot 🎉

Welcome to **My Awesome Discord Bot**! This bot is built using the Nextcord library and provides a slash command to get a "Discord Developer Badge."

## 🚀 How to Use the Bot

1. **Prerequisites:** Before running the bot, you'll need to have the following:
   - Python 3.8 or higher installed.
   - Discord bot token (You can get it from the [Discord Developer Portal](https://discord.com/developers/applications)).

2. **Installation:**
   - Clone this repository to your local machine.
   - Install the required dependencies using `pip install -r requirements.txt`.

3. **Setting Up Your Bot Token:**
   - Open the `config.py` file and replace `"Your Bot Token Goes Here!"` with your actual bot token.

4. **Running the Bot:**
   - Execute `python main.py` in your terminal to start the bot.
   - The bot will log in to Discord and display a message when it's ready.

5. **Inviting the Bot to Your Server:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and find your bot.
   - Copy the Client ID of your bot and replace `<YOUR_CLIENT_ID>` in the following URL: `https://discord.com/oauth2/authorize?client_id=<YOUR_CLIENT_ID>&scope=bot+applications.commands`.
   - Visit the URL in your web browser and select the server where you want to add the bot.

6. **Using the Bot:**
   - Once the bot is in your server, simply type `/get` in any text channel.
   - The bot will respond with a message containing information about the Discord Developer Badge.

## 📝 Additional Information

- **Bot Version:** v0.0.1
- **Library Used:** Nextcord
- **Author:** Zyneeeeeeeee
- **Contributing:** If you want to contribute to this project, feel free to submit a pull request!
- **Issues:** If you encounter any bugs or have suggestions, please open an issue in this repository.
