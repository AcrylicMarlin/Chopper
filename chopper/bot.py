import os
import typing

from discord.ext import commands
import discord
import asqlite
from dotenv import load_dotenv
load_dotenv()
on_ready_message = """
------------------------
- ChopperBot is ready! -
- Latency: {0}ms       -
- ID: {1}              -
- Number of users: {2} -
------------------------"""

class Chopper(commands.Bot):

    important_channels: typing.Dict[str, discord.TextChannel]
    def __init__(self, *, 
        intents:discord.Intents,
        status:discord.Status,
        activity:discord.Activity):
        super().__init__(self, intents=intents, status=status, activity=activity)



    async def on_ready(self):
        self.guild = self.get_guild(1225527100870758571)
        self.important_channels = {
            "welcome": self.guild.get_channel(1225527101357162587),
            "goodbye": self.guild.get_channel(1225527101357162590),
            "levels": self.guild.get_channel(1227241618138988697)
        }
        latency = round(self.latency * 1000)
        ID = self.user.id
        users = len(self.users)
        print(on_ready_message.format(latency, ID, users))



    # async def setup_hook(self):
        
    async def run(self):

        try:
            async with self:
                token = ''
                try:
                    token = os.getenv("TOKEN")
                except TypeError:
                    token = os.environ["TOKEN"]
                await self.start(os.getenv("TOKEN"))

        except KeyboardInterrupt:
            await self.close()
    