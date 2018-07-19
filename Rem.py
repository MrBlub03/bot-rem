#TextBot by Mr.Blub

import discord
import random
import asyncio
import aiohttp
import time
import json
import os
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
from os import system
from pathlib import Path
from os import system
from pathlib import Path

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'))
bot.remove_command('help')

players = {}
queues = {}

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi there~ " + ctx.message.author)
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        await bot.say("Bye {}. See you later~".format(user.name))
        await bot.kick(user)
        print (ctx.message.author.name + " just kicked " + user.name)
    else:
        await bot.say("oh~ it looks like you don't have the power to do this~")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.ban_members:
        await bot.say("Goodbye {}, have fun~".format(user.name))
        await bot.ban(user)
        print (ctx.message.author.name + " just banned " + user.name)
    else:
        await bot.say("oh~ it looks like you don't have the power to do this~")

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Thats a no~',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command(pass_context=True)
async def blub(ctx, user: discord.Member):
	await bot.say('you have ben blubed ' + user.name)

@bot.command(
                description="Flips a coin for heads or tails",
                brief="Gives a 50/50 chance on winning",
                pass_context=True)
async def coinflip(context):
    possible_responses = [
        'Looks like it heads',
        'Oh, Its tails',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.event # MESSAGE SENT LOG TO THE CONSOLE
async def on_message(message):
    bot.process_commands(message)
    author = message.author
    content = message.content
    channel = message.channel
    print('{} (#{}): {}'.format(author, channel, content))

@bot.command(pass_context=True)
async def diceroll(context):
	possible_responses = [
		'Its 1',
		'looks like a 2',
		'You rolled a 3',
		'It a number 4',
		'You got 5',
		'Um....it a 6',
		]
	await bot.say(random.choice(possible_responses))

@bot.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(title="Commands", description="Command prefix is `?` | Use `?help` for a list of commands.", color=0x25affa)
	embed.add_field(name="General", value="`8ball`,`hello`,`coinflip`,`blub`,`info`,`serverinfo`,`invite`,`diceroll`,`shoot`,`pinged`,`whatsnew`", inline=False)
	embed.add_field(name="Moderation", value="`ban`,`kick`", inline=False)
	embed.add_field(name="Images", value="`doorstuck`,`cat`,`glare`,`cry`,`pat`,`smile`,`dance`,`hit`,`hug`,`sleep`,`tease`,`rezero`", inline=False)
	embed.add_field(name="Audio", value="`join`,`leave`,`play`,`skip`,`resume`,`queue`", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.send_message(ctx.message.author, "You want to invite me?!?! Wow, Thanks you so much~!!! Here's the link: https://discordapp.com/api/oauth2/authorize?client_id=437840611127590912&permissions=8&scope=bot")
    await bot.add_reaction(ctx.message, '\U0001F44D')

@bot.command(pass_context=True)
async def doorstuck(ctx):
	embed = discord.Embed(title='DoorStuck!!!', color=0x25affa)
	embed.set_image(url="http://www.cutecatgifs.com/wp-content/uploads/2015/04/fat_cat.gif")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cat(context):
	possible_responses = [
		'http://i.imgur.com/0xCeeJI.gif',
		'https://blazepress.com/.image/t_share/MTMxMTIxOTY0NDI4MzM1NTgy/funniest-cat-gifs-on-the-internet-46gif.gif',
		'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
		'https://cdn.shopify.com/s/files/1/0344/6469/files/tumblr_o1urocQubH1uuyy36o1_400_large.gif?13599955790670839483',
		'https://welovecatsandkittens.com/wp-content/uploads/2017/05/strives-for-perfection.gif',
		'http://bestanimations.com/Animals/Mammals/Cats/catgif/funny-cat-gif-5.gif',
		]
	await bot.say(random.choice(possible_responses))

@bot.command(pass_context=True)
async def shoot(ctx, user: discord.Member):
	embed = discord.Embed(title=ctx.message.author.name + ' shot ' + user.name, color=0x25affa)
	embed.set_image(url="http://forgifs.com/gallery/d/252560-2/Cat-sleeping-on-car-hood.gif")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def support(ctx):
	await bot.say('Oh~ you need help with something? The support is carried out here: https://discord.gg/peZ2d33')

@bot.command(pass_context=True)
async def pinged(ctx):
	embed = discord.Embed(title='WHO PINGED ME!!!', color=0x25affa)
	embed.set_image(url="https://cdn.discordapp.com/attachments/442120104701067284/442733577529196546/PING_BAD.gif")
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def glare(ctx, user: discord.Member):
	embed = discord.Embed(title=ctx.message.author.name + ' glared at ' + user.name, color=0x25affa)
	embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxtjerBAfA_qbE6WKNJi_vhRNE0b9o3s5-rSS2SCfMuHoh1Bpj")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cry(ctx):
	embed = discord.Embed(color=0x25affa)
	embed.set_image(url="https://media1.tenor.com/images/0566c05e5a211a3df88ce55e89a63661/tenor.gif?itemid=7142001")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def smile(ctx):
	embed = discord.Embed(color=0x25affa)
	embed.set_image(url="https://i1.wp.com/i.imgbox.com/zC7sdbG1.gif")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def dance(ctx):
	embed = discord.Embed(color=0x25affa)
	embed.set_image(url="https://media1.tenor.com/images/a1f39c7744e6d48331d8be89f73e6b18/tenor.gif?itemid=8907892")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hit(ctx, user: discord.Member):
	embed = discord.Embed(title=ctx.message.author.name + ' hit ' + user.name, color=0x25affa)
	embed.set_image(url="https://pa1.narvii.com/6288/0eae8d8b1381bef2f07d630e623a91e6896302c5_hq.gif")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
	embed = discord.Embed(title=ctx.message.author.name + ' hugged ' + user.name, color=0x25affa)
	embed.set_image(url="http://i.imgur.com/kcXjdsF.gif")
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def pat(ctx, user: discord.Member):
    possible_responses = [
        'https://i.imgur.com/MPCn4xf.gif',
        'https://thumbs.gfycat.com/IncompleteScientificIntermediateegret-max-1mb.gif',
    ]

    embed = discord.Embed(title=ctx.message.author.name + ' patted ' + user.name, color=0x25affa)
    embed.set_image(url=(random.choice(possible_responses)))
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def sleep(ctx):
    possible_responses = [
        'https://66.media.tumblr.com/9d2402a89a65764dcb590eb6526d81cc/tumblr_o6iha1rcUc1ta7pubo1_500.gif',
    ]

    embed = discord.Embed(title=ctx.message.author.name + ' fell asleep', color=0x25affa)
    embed.set_image(url=(random.choice(possible_responses)))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def tease(ctx, user: discord.Member):
    possible_responses = [
        'http://i.imgur.com/LGeJNsg.gif',
    ]

    embed = discord.Embed(title=ctx.message.author.name + ' teased ' + user.name, color=0x25affa)
    embed.set_image(url=(random.choice(possible_responses)))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def rezero(ctx):
    possible_responses = [
        'https://vignette.wikia.nocookie.net/rezero/images/0/02/Rem_Anime.png/revision/latest?cb=20160730213532',
        'https://78.media.tumblr.com/072484d6021e058f7d6d3912553f93e8/tumblr_oq4p23zvq41tlypw3o1_500.gif',
        'https://media2.giphy.com/media/fbJLRzpp3Jzxe/giphy.gif',
        'https://steamusercontent-a.akamaihd.net/ugc/103979035133260065/39A5F2A29ABBB5DE781F4E6B0B687D8168274135',
        'https://pa1.narvii.com/6542/0db8d684b8fd2008068d52b33faa84aa8fea73a7_hq.',
        'https://78.media.tumblr.com/1c1498ecf1eeafa2b6ce0342d7dd440f/tumblr_oc9xm4yqlX1ujwmbqo1_500.gif',
        'https://68.media.tumblr.com/01f357453e4180027a1e437342994018/tumblr_o5sm9iXHTU1ta7pubo1_500.gif',
        'https://68.media.tumblr.com/f06bcb470a0fe06f2086047dbe621b57/tumblr_omksxfzYbj1v14hqvo1_500.gif',
        'https://pa1.narvii.com/6279/fc7e12a9fb909b4d4c10cd0d9d670c44bd5c97ec_hq.gif',
        'http://pa1.narvii.com/6119/248ac41f76779ea721f6f5c2044fff04db34d226_hq.gif',
        'http://pa1.narvii.com/6528/5374aebd2662e125f56c3a55b9f2f7d6be9f0d70_hq.gif',
    ]

    embed = discord.Embed(title="Here's a re:zero picture", color=0x25affa)
    embed.set_image(url=(random.choice(possible_responses)))
    await bot.say(embed=embed)

@bot.event
async def on_member_join(member):
    channel = member.server.get_channel('422949315502276608')
    fmt = 'Welcome to the {1.name} Discord Server, {0.mention}, please read  the rules and enjoy your stay'
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(member):
    chennel = member.server.get_channel('422949315502276608')
    fmt = '{0.mention} has left/been kicked from the server'
    await bot.send_message(chennel, fmt.format(member, member.server))

@bot.command(pass_context=True)
async def shutdown(ctx):
    if ctx.message.author.id == "252634093743898654":
        await bot.say("Oh~ I guess I will see you later~ :smile:")
        await bot.logout()
    else:
        await bot.say("Oh~ I'm sorry but you are not the owner~")

@bot.command(pass_context = True)
async def clear(ctx, number):
	if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == '252634093743898654':
		mgs = [] #Empty list to put all the messages in the log
		number = int(number) #Converting the amount of messages to delete to an integer
		async for x in bot.logs_from(ctx.message.channel, limit = number):
			mgs.append(x)
		await bot.delete_messages(mgs)
	else:
		bot.say("It looks like you can't do this~")

@bot.command(pass_context=True)
async def loggish1(ctx):
    embed = discord.Embed(title="Loggish eating a cheeto", color=0x25affa)
    embed.set_image(url="https://cdn.discordapp.com/attachments/451234111500189696/451248216906661889/unknown.png")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def loggish2(ctx):
    embed = discord.Embed(color=0x25affa)
    embed.set_image(url="https://media.discordapp.net/attachments/451234111500189696/451251133428531210/unknown.png?width=945&height=559")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def whatsnew(ctx):
    embed = discord.Embed(title="Newest Updates", description="See The New Features and What is Coming Up", color=0x25affa)
    embed.add_field(name="V0.7 (What I'm Working On)", value="Fix some of the `image` commands as some of the gifs are now missing", inline=False)
    embed.add_field(name="V0.6", value="Made the bot have some music functions, Added `Join` `Leave` `Play` `Queue` `resume` and `skip` commands", inline=False)
    embed.add_field(name="V0.5", value="Added some secret commands that show some `special` stuff", inline=False)
    await bot.say(embed=embed)

@bot.event
async def on_ready():
	print('--Login--')
	print('Name: ' + bot.user.name)
	print('ID: ' + bot.user.id)
	print('------------READY------------')
	await bot.change_presence(game=discord.Game(name='Do ?help for commands'))

bot.run(os.environ.get('TOKEN'))
