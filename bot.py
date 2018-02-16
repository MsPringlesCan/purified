import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import random
import requests 
import asyncio
import chalk


startup_extensions = ["Music"]
bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print ("Launched on:")
    print (bot.user.name)
    print ("ID: 412162236371566595")
    print ("~~~~~~~~~~~~~~~~~")
	
@bot.command(pass_context=True)
async def h(ctx):	
	embed = discord.Embed(title="My Commands!!", description="Heres all the commands I could find..", color=0x00FF00)
	embed.add_field(name="~~~~", value="!help", inline=True)
	embed.add_field(name="~~~~", value="!ping", inline=True)
	embed.add_field(name="~~~~", value="!about", inline=True)
	embed.add_field(name="~~~~", value="!owner", inline=True)
	embed.add_field(name="~~~~", value="!contact")
	embed.add_field(name="~~~~", value="!info")
	embed.add_field(name="~~~~", value="!invite : \n*My invite to your server*")
	await ctx.send(embed=embed) 
	
@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(":ping_pong: pong!")
 
@bot.command(pass_context=True)
async def summon(ctx):
    voice_channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(voice_channel)

 
@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="Purified Music (Beta)", description="Purified Music (Beta) is still under construction, stay tuned! ♥", color=0xe51e1e)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def owner(ctx):
	embed = discord.Embed(title="Owner", description="The owner is >Purity âœ© | ~Neptune âœ©#1234", color=0x00FF00)
	embed.add_field(name="Contact", value="Type `!contact` to get further assistance if needed!")
	await ctx.send(embed=embed)
	
@bot.command(pass_context=True)
async def contact(ctx):
	embed = discord.Embed(title="Help me", description="If you need help contact >Purity âœ© | ~Neptune âœ©#1234, or type `!help`", color=0x00FF00)
	embed.add_field(name="Can't contact her?", value="Join the discord at, https://discord.gg/5gfWT2N and contact a staff member to get her attention!")
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name="Made by Purity")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
	try:
		await ctx.send("*Wham!*... {} just got their ass kicked out! :wave:".format(user.name))
		await ctx.guild.kick(user)	
	except:
		embed = discord.Embed(title=":exclamation: Error", description=" :warning: I could not kick this user, I do not have the proper permissions! \n*(Move me visually above who you want to kick)*", color=0xe51e1e)
		await ctx.send(embed=embed)
		
@bot.command(pass_context=True)
async def invite(ctx):
	embed = discord.Embed(title="Click me, I wanna join your server!", color=0x00FF00, url="https://discordapp.com/oauth2/authorize?&client_id=412162236371566595&scope=bot&permissions=12659727")
	embed.add_field(name="Thanks!", value=":exclamation: Thank you for checking out my *moist* link", inline=True)
	await ctx.send(embed=embed)
	
bot.run("NDEyMTYyMjM2MzcxNTY2NTk1.DWIXGw.SLmBMLmCGa6eI7CwkwJH3REnKw0")