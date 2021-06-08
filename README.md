# AutoBan
Discord bot to automatically ban a user whose username contains a specific string.

### Usage

- If you don't have a dev app yet, create one on https://discord.com/developers/applications/.
- Create a bot for your app.
- Grant priviliged gateway intents to your newly made bot (just tick the options).
- Copy the bot's token and save it for later.
- Invite the bot on your server, with appropriate permissions (namely, read and ban).

Next :
- If you don't have it yet, install [python](https://www.python.org/downloads/).
- Install discord.py via pip ([guide here](https://discordpy.readthedocs.io/en/stable/intro.html)).

Then, in autoban.py, removing the [ ] brackets :
- Replace '[your_target_string]' with the specific word(s) you want the bot the ban. **/!\ It is case insensitive by default, you need to remove '.lower()' if you don't want it to be.**
- Replace '[your_bot_token_here]' with your bot's private token.
- Replace '[your_ban_reason_here]' with... self explanatory.

Finally, run autoban.py inside your terminal of choice.
The bot will only work while the script is running.

Originally made to counter the spam of bots pointing to https://twitter.com/h0nde.
