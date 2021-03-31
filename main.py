import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='.', case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} is online.')


@client.command()
async def admin_key__load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Loaded {extension} command(s)")

                      
@client.command()
async def admin_key__unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unloaded {extension} command(s)")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('{Bot Token Goes Here}')
