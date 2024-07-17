# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name="hi")
async def hi(ctx):
    print("hi")
    await ctx.send(f"hi <@{ctx.author.id}>")


@bot.command(name="foo")
async def foo(ctx, *arg):
    await ctx.send(" ".join(arg))


@bot.slash_command(
    name="first_slash",
)
async def first_slash(ctx,):
    await ctx.respond("You executed the slash command!")


@bot.slash_command(name="add",)
async def add(ctx, a: discord.Option(int), b: discord.Option(int)):
    await ctx.respond(a + b)


# create a user command for the supplied guilds
@bot.user_command(name="Account Creation Date")
# user commands return the member
async def account_creation_date(ctx, member: discord.Member):
    await ctx.respond(
        f"{member.name}'s account was created on {member.created_at}")


@bot.message_command(name="Get Message ID")
# message commands return the message
async def get_message_id(ctx, message: discord.Message):
    await ctx.respond(f"Message ID: `{message.id}`")

bot.run(os.getenv("hi"))
