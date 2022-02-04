import discord
from discord import Member
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

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

ban_reason = 'Verification, the server name or moderator names are not allowed in the username to prevent imposing scammers.'
bot_token = 'your_bot_token_here'
# === ↑ SETTINGS ↑ ============================================================

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    """
    Executes when the Bot is ready
    """

    print('We have logged in as {0.user}'.format(bot))


async def check_member(member: Member):
    """
    Checks the member names against illegal strings, bans if illegal names are found

    :param member: (Member) Object of said member
    """

    print(f'Checking member {member.name}...')
    member_names = [member.name, member.nick, member.display_name]
    member_banned = False

    if member.id not in whitelisted_user_ids:
        for target_string in target_strings:
            if member_banned is False:
                for member_name in member_names:

                    if (member_name is not None) and (target_string in member_name.lower()):
                        print(f'{member.name} matches the target string ({target_string})!')

                        try:
                            print(f'Banning {member.name}!')
                            await member.ban(reason=ban_reason)
                            member_banned = True
                            break
                        except:
                            print(f'Failed to ban {member.name}... :c')
    else:
        print(f'Member {member.name} is in whitelist, ignoring...')

    if member_banned is False:
        print(f'No need to ban {member.name}, does not match the target strings!')


@bot.event
async def on_member_join(member: Member):
    """
    Executes when a new member joins the server

    :param member: (Member) Object of said member
    """

    await check_member(member=member)


bot.run('[your_bot_token_here]')
