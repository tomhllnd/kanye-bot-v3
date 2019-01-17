import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import asyncio
import time
import random

cyberContents = []
with open('cyber.txt') as f:
    for line in f:
        cyberContents.append(line.strip())
nsbContents = []
with open('nsb.txt') as f:
    for line in f:
        nsbContents.append(line.strip())
soleContents = []
with open('sole.txt') as f:
    for line in f:
        soleContents.append(line.strip())
pdContents = []
with open('pd.txt') as f:
    for line in f:
        pdContents.append(line.strip())

print(cyberContents)
print(nsbContents)
print(soleContents)
print(pdContents)

facts = ['I gave Donald the pass','We came into a broken world. And were the cleanup crew.','If you have the opportunity to play this game of life you need to appreciate every moment. a lot of people don’t appreciate the moment until it’s passed.','We all self-conscious. I’m just the first to admit it.','If I was just a fan of music, I would think that I was the number one artist in the world.','Love your haters, they’re your biggest fans.','I love it','Every man loves men. Facts.','The prettiest people do the ugliest things.']
Client = discord.Client()
client = commands.Bot(command_prefix = "kanye, ")

@client.event
async def on_ready():
    print("Im ready")
    while True:
        await client.change_presence(game=Game(name='for ur commands ( ͠° ͟ʖ ͠°)', type = 3))


@client.event
async def on_message(message):
    if message.content == "kanye, ping":
        randomd = random.randint(0,10)
        if randomd == 10:
            await client.send_message(message.channel, "fuck off")
        else:
            await client.send_message(message.channel, "pong")
    if message.content.startswith("kanye, fees "):
        userAmountPounds = message.content[11:]
        userAmountPennies = int(userAmountPounds)*100
        print(userAmountPennies)
        paypalOutput = round((((userAmountPennies * 0.969) - 20) / 100) ,2)
        print('Paypal:',paypalOutput)
        ebayOutput = round(((((userAmountPennies * 0.9) * 0.969) - 20) / 100) ,2)
        print('Ebay:',ebayOutput)
        depopOutput = round(((((userAmountPennies * 0.9) * 0.969) - 20) / 100) ,2)
        print('Depop:',depopOutput)
        bumpOutput = round(((((userAmountPennies * 0.94) * 0.969) - 20) / 100) ,2)
        print('Bump:',bumpOutput)
        stockx1Output = round(((userAmountPennies * 0.875) / 100) ,2)
        print('StockX Lvl1:',stockx1Output)
        stockx2Output = round(((userAmountPennies * 0.88) / 100) ,2)
        print('StockX Lvl2:',stockx2Output)
        stockx3Output = round(((userAmountPennies * 0.885) / 100) ,2)
        print('StockX Lvl3:',stockx3Output)
        stockx4Output = round(((userAmountPennies * 0.89) / 100) ,2)
        print('StockX Lvl4:',stockx4Output)
        embed = discord.Embed(title=f'Fees Calculated for £{userAmountPounds}', color=0x2fe14e)
        embed.add_field(name='Paypal', value=f'£{paypalOutput}', inline=False)
        embed.add_field(name='Bump', value=f'£{bumpOutput}', inline=False)
        embed.add_field(name='Depop', value=f'£{depopOutput}', inline=False)
        embed.add_field(name='Ebay', value=f'£{ebayOutput}', inline=False)
        embed.add_field(name='StockX Seller Level 1', value=f'£{stockx1Output}', inline=False)
        embed.add_field(name='StockX Seller Level 2', value=f'£{stockx2Output}', inline=False )
        embed.add_field(name='StockX Seller Level 3', value=f'£{stockx3Output}', inline=False)
        embed.add_field(name='StockX Seller Level 4', value=f'£{stockx4Output}', inline=False)
        embed.set_author(name="Kanye's Fee Calculator", icon_url="https://cdn.discordapp.com/attachments/533238248781250563/534686598172770304/Energy-Appraiser-Certification-Registration-Fees-Icon.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/533238248781250563/534687466540630016/image0.jpg")
        embed.set_footer(text="Kanye Bot made by Plug#5464")
        await client.send_message(message.channel,embed=embed)
    if message.content.startswith("kanye, fact"):
        embed = discord.Embed(color=0x2fe14e)
        embed.add_field(name=facts[random.randint(0,(len(facts)-1))], value='- Kanye West', inline=False)
        embed.set_footer(text="Kanye Bot made by Plug#5464")
        await client.send_message(message.channel,embed=embed)
    if message.content.startswith("kanye, help"):
        embed = discord.Embed(color=0x2fe14e)
        embed.set_author(name="Hey, I'm Kanye.", icon_url="https://cdn.discordapp.com/attachments/533238248781250563/535116197591646218/help.png")
        embed.add_field(name='__Fee Calculator__', value='Beckon me with `kanye, fees <amount>` and I will calculate the fees each of the sites you dirty resellers will take', inline=False)
        embed.add_field(name='__Ping__', value='Check if im running and online with `kanye, ping`. If you spam it, Ill get hella triggered ( ͡☉ ͜ʖ ͡☉)', inline=False)
        embed.add_field(name='__Fact__', value='Use `kanye, fact` for an intersting quote or fact by me', inline=False)
        embed.add_field(name='__Check__', value='Checks if a site it supported by a bot. Use `kanye, check <pd/cyber/sole/nsb> <sitename>`. Dont actually link the site, just type its name an alternatives to its name and remove all spaces. i.e. ExtraButter and ExtraButterNY', inline=False)
        embed.set_footer(text="Kanye Bot made by Plug#5464")
        await client.send_message(message.channel,embed=embed)
    if message.content.startswith("kanye, check "):
        userInput = message.content[12:]
        userInput = userInput.split()
        message1 = await client.send_message(message.channel,f'Opening list {userInput[0]}.txt...')
        message2 = await client.send_message(message.channel,f'Searching for {userInput[1]} in {userInput[0]}.txt...')
        if userInput[0].lower() == 'nsb':
            if userInput[1].lower() in [x.lower() for x in nsbContents]:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':white_check_mark: {userInput[1]} is definatley supported by NikeShoeBot', value='as it was found in list of supported sites on their website', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
            else:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':bangbang: {userInput[1]} is probably not supported by NikeShoeBot', value='however it may be due to a misspelling, so check their website. Try an alternative name (i.e instead of ExtraButterNY, try ExtraButter)', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
        if userInput[0].lower() == 'cyber':
            if userInput[1].lower() in [x.lower() for x in cyberContents]:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':white_check_mark:{userInput[1]} is definatley supported by Cybersole', value='as it was found in list of supported sites on their website', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
            else:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':bangbang: {userInput[1]} is probably not supported by Cybersole', value='however it may be due to a misspelling, so check their website. Try an alternative name (i.e instead of ExtraButterNY, try ExtraButter)', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
        if userInput[0].lower() == 'pd':
            if userInput[1].lower() in [x.lower() for x in pdContents]:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':white_check_mark: {userInput[1]} is definatley supported by Project Destroyer', value='as it was found in list of supported sites on their website', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
            else:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':bangbang: {userInput[1]} is probably not supported by Project Destroyer', value='however it may be due to a misspelling, so check their website. Try an alternative name (i.e instead of ExtraButterNY, try ExtraButter)', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
        if userInput[0].lower() == 'sole':
            if userInput[1].lower() in [x.lower() for x in soleContents]:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':white_check_mark: {userInput[1]} is definatley supported by SoleAIO', value='as it was found in list of supported sites on their website', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)
            else:
                embed = discord.Embed(color=0x2fe14e)
                embed.add_field(name=f':bangbang: {userInput[1]} is probably not supported by SoleAIO', value='however it may be due to a misspelling, so check their website. Try an alternative name (i.e instead of ExtraButterNY, try ExtraButter)', inline=False)
                embed.set_footer(text="Kanye Bot made by Plug#5464")
                await client.send_message(message.channel,embed=embed)
                await asyncio.sleep(0.5) 
                await client.delete_message(message1)
                await asyncio.sleep(0.5) 
                await client.delete_message(message2)

             


@client.event
async def on_member_join(member):
    if member.server.id == '510211732757676052':
        embed = discord.Embed(title="pluggduk Patreon", url='http://patreon.com/pluggduk', color=0x2fe14e)
        embed.set_author(name="Welcome to pluggdUK.")
        embed.add_field(name='Welcome', value='We are a UK-based cook group, who look forward to helping you make profit. We charge a small fee of £15 per month, which relative to other cook groups, is very small.\n ', inline=False)
        embed.add_field(name='Features', value='We offer 24/7 advice, groupbuys (recently offered members chance to buy NSB for $425, now selling at $1k), **Free** Supreme slots and **very** cheap Shopify slots on bots like Cyber, Instant homemade restock monitors, REsell Predicitons, accurate early links, and much more. ', inline=False)
        embed.add_field(name='Become a Member', value='In order to become a paying member, you need to click on the link to our patreon above, and become the Chef tier. After that, you need to link your discord with patreon, and you will recieve your role.', inline=False)
        embed.set_footer(text="Kanye Bot made by Plug#5464")
        await client.send_message(member, embed=embed)
        






client.run(os.getenv('TOKEN'))
