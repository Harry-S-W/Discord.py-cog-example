import discord
import json
from discord.ext import commands


class Example(commands.Cog): # Creating class for cog

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Custom Command Online')

    @commands.command()
    async def custom(self, ctx):
    await ctx.send('Example for cogs!')


def setup(client):
    client.add_cog(Example(client))  # Adding cog
