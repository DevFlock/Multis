import discord
from discord.ext import commands
import json

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

def setup(client):
    client.add_cog(cog(client))