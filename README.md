# Discord AutoBan
<p align="left">
    <a href="https://www.iconomi.com/register?ref=JdFzz">
        <img src="https://img.shields.io/badge/ICONOMI-Join-blue?logo=bitcoin&logoColor=white" alt="ICONOMI - The world’s largest crypto strategy provider">
    </a> <a href="https://www.buymeacoffee.com/Rikj000">
        <img src="https://img.shields.io/badge/-Buy%20me%20a%20Coffee!-FFDD00?logo=buy-me-a-coffee&logoColor=black" alt="Buy me a Coffee as a way to sponsor this project!">
    </a>
</p>

Discord Bot to automatically ban a user whose username contains a specific string.

Originally made by [@Whismirk](https://github.com/Whismirk) to counter the spam of bots pointing to [h0nde (Twitter)](https://twitter.com/h0nde)   
Improved by [@Rikj000](https://github.com/Rikj000) to counter the spam of bots pointing to the [fehu NFT project (Discord)](https://discord.gg/8bB837HRPb)

### Requirements
- If you don't have it yet, install [python](https://www.python.org/downloads/).
- Install `discord.py` via `pip` ([guide here](https://discordpy.readthedocs.io/en/stable/intro.html)).

### Usage

- If you don't have a dev app yet, create one on https://discord.com/developers/applications/.
- Create a bot for your app. Save its token for later.
- Grant privileged gateway intents to your newly made bot (just tick the options).
- Invite the bot on your server, with appropriate permissions (namely, read and ban).
- Then, in `autoban.py`, configure the `SETTINGS` section to your needs:

    - You can get `user_ids` by going into your Discord settings => Advanced => Enable Developer Mode.
    - Then right click on a user and at the bottom of the options menu you will be able to copy the `user_id`.

    ```python
    # === ↓ SETTINGS ↓ ============================================================
    target_strings = [
        'verification',
        'your_server_name_here',
        'your_moderator_name_here',
        'your_moderator_name_here',
        'whatever_other_words_that_need_banning',
    ]

    whitelisted_user_ids = [
        123456789123456789,  # your_moderator_user_id_here
        123456789123456789,  # your_moderator_user_id_here
    ]

    ban_reason = 'Verification, the server name or moderator names are not allowed in the username to prevent scammers.'
    bot_token = 'your_bot_token_here'
    # === ↑ SETTINGS ↑ ============================================================
    ```
- Finally, run `autoban.py` inside your terminal of choice.
    *(The bot will only work while the script is running)*
- **Optional:** A `Dockerfile` has been added to make running with [`docker`](https://www.docker.com/) possible 🙂
