import discord
import asyncio
from discord.ext import commands
import urllib.request, urllib.parse, urllib.error
import json

bot = commands.Bot(command_prefix='.')
serviceurl = 'https://api.covid19india.org/state_district_wise.json?'

@bot.listen()
async def on_message(message):
    if ((str(message.channel) == "🤳➤selfies") or (str(message.channel) == "🛡➤show-off-your-art")) and message.content != "" and message.author.id != 612661190878822402:
        await message.delete()
        name = message.author.mention
        response = f"Go to appropriate channel Mr.{name}, you can not send messages here."
        await message.channel.send(response, delete_after = 10)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def substract(ctx, a: int, b: int):
    await ctx.send(a-b)

@bot.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a/b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

# @bot.command()
# async def bump(ctx):
#     await ctx.send("!d bump")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    # give info about you here
    embed.add_field(name="ROHIT SHARMA", value="RO-HITMAN")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<612661190878822402>)")
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="hitman bot", description="A Very Nice bot. List of commands are:", color=0xeee657)
    embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=True)
    embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name=".subtract X Y", value="Gives the difference between **X** and **Y**", inline=False)
    embed.add_field(name=".divide X Y", value="Gives the division of **X** by **Y**", inline=False)
    embed.add_field(name=".greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=".cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the bot", inline=False)
    # embed.add_field(name="$bump", value="Will bump this server", inline=False)
    embed.add_field(name=".help", value="Gives this message", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def covid(ctx, state: str, city: str):
    site = urllib.request.urlopen(serviceurl)
    data = site.read().decode()
    stateName = state
    cityName = city
    
    js = json.loads(data)
    try:
        totalConfirmed = js[stateName]["districtData"][cityName]["confirmed"]
        totalActive = js[stateName]["districtData"][cityName]["active"]
        totalDeceased = js[stateName]["districtData"][cityName]["deceased"]
    except:
        string = '.covid "State Name" "District Name"'
        embed = discord.Embed(title="", description="", color=0xeee657)
        embed.add_field(name="Command", value=string, inline=True)
        embed.add_field(name="Note", 
                        value="Please make sure starting alphabet of district and state name are in capital.", 
                        inline=False)
        embed.add_field(name="Example", 
                        value=string, 
                        inline=False)
        await ctx.send(embed=embed)


    embed = discord.Embed(title="Covid-19 cases: ", description="", color=0xeee657)
    embed.add_field(name="Total Confirmed: ", value=totalConfirmed, inline=True)
    embed.add_field(name="Total Active: ", value=totalActive, inline=False)
    embed.add_field(name="Total Deaths", value=totalDeceased, inline=False)
    await ctx.send(embed=embed)

bot.run(os.getenv('BOT_TOKEN'))
