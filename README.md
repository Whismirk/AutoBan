# Discord AutoBan
Discord Bot to automatically ban a user whose username contains a specific string.

Originally made to counter the spam of bots pointing to https://twitter.com/h0nde.

### Requirements
- If you don't have it yet, install [python](https://www.python.org/downloads/).
- Install `discord.py` via `pip` ([guide here](https://discordpy.readthedocs.io/en/stable/intro.html)).

### Usage

- If you don't have a dev app yet, create one on https://discord.com/developers/applications/.
- Create a bot for your app. Save its token for later.
- Grant privileged gateway intents to your newly made bot (just tick the options).
- Invite the bot on your server, with appropriate permissions (namely, read and ban).
- Then, in `autoban.py`, removing the `[ ]` brackets :
  - Replace `[your_target_string]` with the specific word(s) you want the bot the ban.
      **⚠️ It is case-insensitive by default, you need to remove `.lower()` if you don't want it to be.**
  - Replace `[your_bot_token_here]` with your bots private token.
  - Replace `[your_ban_reason_here]` with... self-explanatory.
- Finally, run `autoban.py` inside your terminal of choice.

The bot will only work while the script is running.
