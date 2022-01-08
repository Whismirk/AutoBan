import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    """
    Executes when the Bot is ready
    """

    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_member_join(member):
    """
    Executes when a new member joins the server

    :param member: Object of new member joining the server
    """

    print('New member !')
    if '[your_target_string]' in member.name.lower():
        print('Found the target !')
        try:
            print('Banning the target !')
            await member.ban(reason='[your_ban_reason_here]')
        except:
            print('Could not ban the target :(')
    else:
        print('New member is not the target...')


bot.run('[your_bot_token_here]')
