from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
            print("New member !")
            if "twitter.com/h0nde" in member.name.lower():
                print("Found h0nde !")
                try:
                    print("Banning h0nde!")
                    await member.ban(reason="h0nde, more like h0ndegenerate.")
                except:
                    print("Couldn't ban him :(")
            else:
                print("But it's not h0nde...")

bot.run('[your_bot_token_here]')
