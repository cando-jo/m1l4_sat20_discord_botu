import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
    
@bot.command()
async def rastgele_cumle(ctx, index_sayisi): 
    liste = ["Welcome to Kodland", "I love programming", "I like football"]
    await ctx.send(liste[int(index_sayisi)])
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE5ODMyNzc2Njk3MDUzMTg1MA.Gr9nJW.dAEhikQ4ucIDqkGiQmuJLDkln25Wr9lRi23fsU")

