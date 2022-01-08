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

    print(f'New member {member.name}, joined the server!')

    if '[your_target_string]' in member.name.lower():
        print(f'{member.name} matches the target string!')

        try:
            print(f'Banning {member.name}!')
            await member.ban(reason='[your_ban_reason_here]')
        except:
            print(f'Failed to ban {member.name}... :c')

    else:
        print(f'No need to ban {member.name}, does not match the target string!')

bot.run('[your_bot_token_here]')
