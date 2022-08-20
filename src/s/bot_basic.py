# This example requires the 'members' and 'message_content' privileged intents to function.
from src.main import get_secret_key
import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='`', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left, right):
    """Adds two numbers together."""
    try:
        res = float(left) + float(right)
    except:
        res = 'invalid'
    await ctx.send(res)


@bot.command()
async def evaluate(ctx, *expr):
    """Adds two numbers together."""
    print(expr)
    try:
        res = f'{" ".join(expr)} = {eval(" ".join(expr))}'
    except:
        res = 'invalid'
    await ctx.send(res)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def math(ctx, arg: str, left: int, right: int):
    if arg == 'add':
        await ctx.send(left + right)
    elif arg == 'sub':
        await ctx.send(left - right)
    elif arg == 'mul':
        await ctx.send(left * right)
    elif arg == 'div':
        await ctx.send(left / right)
    else:
        await ctx.send(f'unknown {arg}')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    messages = [f'yes, {ctx.subcommand_passed} is cool', f'no, {ctx.subcommand_passed} is not cool']
    if ctx.invoked_subcommand is None:
        await ctx.send(random.choice(messages))


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


@cool.command(name='shirt')
async def _shirt(ctx):
    messages = ['yes, the shirt is cool', 'no, the shirt is not cool']
    await ctx.send(random.choice(messages))


def main():
    bot.run(get_secret_key())
